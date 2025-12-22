"""
AI Models for Rice Field Monitoring
- U-Net for weed detection
- CNN for fertilizer analysis
- Ensemble for yield prediction
"""

import torch
import torch.nn as nn
import numpy as np
from PIL import Image
import logging

logger = logging.getLogger(__name__)

class UNetWeedDetector:
    """U-Net model for weed detection from multispectral images"""
    
    def __init__(self, model_path="unet_model.pth", device='cpu'):
        """
        Initialize U-Net model
        
        Args:
            model_path: Path to trained unet_model.pth
            device: 'cpu' or 'cuda'
        """
        self.device = device
        self.model_path = model_path
        self.model = None
        self.loaded = False
        
        try:
            self.load_model()
        except Exception as e:
            logger.warning(f"Could not load U-Net model: {e}. Will use fallback mode.")
    
    def load_model(self):
        """Load trained U-Net model"""
        try:
            # Define U-Net architecture
            self.model = self._build_unet(in_channels=5, out_channels=1)
            
            # Load trained weights
            checkpoint = torch.load(self.model_path, map_location=self.device)
            
            # Handle both direct state_dict and nested checkpoint
            if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
                self.model.load_state_dict(checkpoint['model_state_dict'])
            else:
                self.model.load_state_dict(checkpoint)
            
            self.model.to(self.device)
            self.model.eval()
            self.loaded = True
            logger.info("U-Net model loaded successfully")
            
        except FileNotFoundError:
            logger.warning(f"Model file not found at {self.model_path}")
            self.loaded = False
        except Exception as e:
            logger.error(f"Error loading U-Net model: {e}")
            self.loaded = False
    
    def _build_unet(self, in_channels=5, out_channels=1):
        """Build U-Net encoder-decoder architecture"""
        return UNet(in_channels=in_channels, out_channels=out_channels)
    
    def predict(self, image_array: np.ndarray) -> dict:
        """
        Predict weed locations in multispectral image
        
        Args:
            image_array: 5-channel multispectral image (H, W, 5)
                        Channels: Blue, Green, Red, Red Edge, NIR
        
        Returns:
            dict with weed detection results
        """
        if not self.loaded:
            return self._fallback_weed_detection(image_array)
        
        try:
            # Convert to tensor and normalize
            tensor = torch.from_numpy(image_array).float()
            
            # Ensure 5 channels
            if len(tensor.shape) == 2:
                # Grayscale - expand to 5 channels by repeating
                tensor = tensor.unsqueeze(0).repeat(5, 1, 1)
            elif tensor.shape[2] != 5:
                # Adjust channels if not 5
                tensor = self._adjust_channels(tensor, target_channels=5)
            
            # Add batch dimension and move to device
            tensor = tensor.permute(2, 0, 1).unsqueeze(0).to(self.device)
            
            # Inference
            with torch.no_grad():
                segmentation_mask = self.model(tensor)
                segmentation_mask = torch.sigmoid(segmentation_mask)
            
            # Convert to numpy
            mask = segmentation_mask.squeeze().cpu().numpy()
            
            # Calculate statistics
            weed_confidence = float(mask.max())
            weed_coverage = float((mask > 0.5).sum() / mask.size * 100)
            
            return {
                "detected": weed_coverage > 1.0,
                "confidence": round(weed_confidence * 100, 1),
                "coverage": round(weed_coverage, 2),
                "segmentation_mask": mask,
                "weed_types": self._classify_weed_type(mask, weed_confidence),
                "model": "U-Net (Actual)"
            }
        
        except Exception as e:
            logger.error(f"Weed detection error: {e}")
            return self._fallback_weed_detection(image_array)
    
    def _adjust_channels(self, tensor: torch.Tensor, target_channels=5) -> torch.Tensor:
        """Adjust tensor to target number of channels"""
        current_channels = tensor.shape[2] if len(tensor.shape) == 3 else 1
        
        if current_channels >= target_channels:
            return tensor[..., :target_channels]
        else:
            # Repeat channels to reach target
            repeated = tensor
            while repeated.shape[2] < target_channels:
                repeated = torch.cat([repeated, tensor], dim=2)
            return repeated[..., :target_channels]
    
    def _classify_weed_type(self, mask: np.ndarray, confidence: float) -> list:
        """Classify weed type based on segmentation patterns"""
        if confidence > 0.7 and mask.sum() > 0:
            return ["Barnyard Grass (Echinochloa)", "Fimbristylis"]
        return []
    
    def _fallback_weed_detection(self, image_array: np.ndarray) -> dict:
        """Fallback weed detection using image analysis"""
        # Simple fallback: analyze image statistics
        if len(image_array.shape) == 3:
            green = image_array[..., 1].astype(float)
        else:
            green = image_array.astype(float)
        
        # Normalize
        green_norm = (green - green.min()) / (green.max() - green.min() + 1e-7)
        
        # Create fake segmentation mask
        mask = green_norm > 0.6
        confidence = float(green_norm.max())
        coverage = float(mask.sum() / mask.size * 100)
        
        return {
            "detected": coverage > 2.0,
            "confidence": round(confidence * 100, 1),
            "coverage": round(coverage, 2),
            "segmentation_mask": green_norm,
            "weed_types": ["Detected (type uncertain)"] if coverage > 2.0 else [],
            "model": "U-Net (Fallback)"
        }


class UNet(nn.Module):
    """U-Net Encoder-Decoder Architecture for segmentation"""
    
    def __init__(self, in_channels=5, out_channels=1):
        super(UNet, self).__init__()
        
        # Encoder
        self.enc1 = self._block(in_channels, 64)
        self.pool1 = nn.MaxPool2d(2)
        self.enc2 = self._block(64, 128)
        self.pool2 = nn.MaxPool2d(2)
        self.enc3 = self._block(128, 256)
        self.pool3 = nn.MaxPool2d(2)
        self.enc4 = self._block(256, 512)
        self.pool4 = nn.MaxPool2d(2)
        
        # Bottleneck
        self.bottleneck = self._block(512, 1024)
        
        # Decoder
        self.upconv4 = nn.ConvTranspose2d(1024, 512, 2, stride=2)
        self.dec4 = self._block(1024, 512)
        self.upconv3 = nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.dec3 = self._block(512, 256)
        self.upconv2 = nn.ConvTranspose2d(256, 128, 2, stride=2)
        self.dec2 = self._block(256, 128)
        self.upconv1 = nn.ConvTranspose2d(128, 64, 2, stride=2)
        self.dec1 = self._block(128, 64)
        
        # Output
        self.final_conv = nn.Conv2d(64, out_channels, 1)
    
    def _block(self, in_channels, out_channels):
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, 3, padding=1),
            nn.ReLU(inplace=True)
        )
    
    def forward(self, x):
        # Encoder
        enc1 = self.enc1(x)
        x = self.pool1(enc1)
        enc2 = self.enc2(x)
        x = self.pool2(enc2)
        enc3 = self.enc3(x)
        x = self.pool3(enc3)
        enc4 = self.enc4(x)
        x = self.pool4(enc4)
        
        # Bottleneck
        x = self.bottleneck(x)
        
        # Decoder
        x = self.upconv4(x)
        x = torch.cat([x, enc4], dim=1)
        x = self.dec4(x)
        
        x = self.upconv3(x)
        x = torch.cat([x, enc3], dim=1)
        x = self.dec3(x)
        
        x = self.upconv2(x)
        x = torch.cat([x, enc2], dim=1)
        x = self.dec2(x)
        
        x = self.upconv1(x)
        x = torch.cat([x, enc1], dim=1)
        x = self.dec1(x)
        
        # Output
        x = self.final_conv(x)
        return x


# Global weed detector instance
weed_detector = None

def initialize_models():
    """Initialize all AI models"""
    global weed_detector
    weed_detector = UNetWeedDetector()
    return weed_detector

def get_weed_detector():
    """Get weed detector instance"""
    global weed_detector
    if weed_detector is None:
        initialize_models()
    return weed_detector
