"""
Configuration file for Rice Field AI Monitor Bot
Contains FAQ responses and sample alerts
"""

# FAQ Dictionary with keyword-based responses
FAQ_DICT = {
    "weed": "🌾 **Weed Detection System (U-Net)**\n\n📡 **Input**: 5-channel multispectral images (Blue, Green, Red, Red Edge, NIR)\n🧠 **Model**: U-Net encoder-decoder architecture\n📊 **Accuracy**: >85% detection with segmentation masks\n🎯 **Output**: Precise weed location maps with confidence scores\n\nYou'll receive real-time alerts with GPS coordinates when weeds are detected!",
    
    "health": "🌱 **Crop Health Analysis System**\n\n📈 **Vegetation Indices Calculated**:\n• **NDVI** = (NIR - Red) / (NIR + Red) - Overall health indicator\n• **NDRE** = (NIR - Red Edge) / (NIR + Red Edge) - Nitrogen status\n• **GNDVI** = (NIR - Green) / (NIR + Green) - Biomass estimation\n\n💯 **Health Score**: 0-100 scale based on vegetation vigor\n🔍 **Outputs**: Health maps, stress detection, vegetation distribution analysis",
    
    "yield": "📊 **Yield Prediction Ensemble**\n\n🤖 **Models**: Random Forest + Gradient Boosting ensemble\n📥 **Input Features**:\n• Multispectral image analysis\n• NDVI and vegetation indices\n• Growth stage classification\n• Environmental data (weather patterns)\n\n📤 **Output**: Predicted yield (tons/hectare) with confidence intervals\n📈 Based on real-time health metrics and historical data",
    
    "fertilizer": "🧪 **Fertilization Analysis (CNN)**\n\n🔬 **Nutrient Predictions**:\n• **Nitrogen (N)**: 0-1 scale requirement level\n• **Phosphorus (P)**: 0-1 scale requirement level\n• **Potassium (K)**: 0-1 scale requirement level\n\n📊 **Analysis**: Texture analysis, spatial patterns, deficiency detection\n💯 **Health Score**: Overall plant vigor on 0-100 scale\n\nSite-specific recommendations for optimal crop nutrition!",
    
    "ndvi": "📈 **NDVI (Normalized Difference Vegetation Index)**\n\nFormula: NDVI = (NIR - Red) / (NIR + Red)\n\n**Scale**: -1 to +1\n• **>0.7**: Excellent vigor, healthy vegetation\n• **0.5-0.7**: Good health, monitor for stress\n• **0.3-0.5**: Stressed vegetation, intervention needed\n• **<0.3**: Critical condition, immediate action required\n\nHigher NDVI = Higher chlorophyll content and photosynthetic activity",
    
    "irrigation": "💧 **Smart Irrigation Monitoring**\n\n📡 **Tracking**: Soil moisture, weather forecasts, crop water requirements\n⚙️ **Optimization**: Water usage efficiency, prevent stress\n🌡️ **Thresholds**: Monitors temperature stress and moisture balance\n\nAutomated recommendations for optimal irrigation timing and volume",
    
    "disease": "🦠 **Disease Detection System**\n\n🔍 **Common Rice Diseases Detected**:\n• Rice Blast - Fungal infection on leaves\n• Rice Blight - Affects leaf sheaths and panicles\n• Sheath Rot - Degrades rice grain quality\n\n🤖 **Method**: Computer vision & CNN analysis\n⚠️ **Early Detection**: Identifies symptoms before significant crop loss\n💊 **Prevention**: Enables preventive fungicide treatment",
    
    "weather": "🌤️ **Integrated Weather Monitoring**\n\n📊 **Real-time Data**:\n• Temperature, Humidity, Rainfall, Wind patterns\n• Growth stage impact assessment\n• Pest pressure predictions\n\n🔮 **Forecasts**: Future conditions affecting crop growth\n⚡ **Alerts**: Critical weather events with automated recommendations"
}

# Sample alerts for testing the push notification system
SAMPLE_ALERTS = {
    "weed": """
🚨 **U-NET WEED DETECTION ALERT** 🚨

📡 **Model**: U-Net Encoder-Decoder (5-channel multispectral)
📍 **Location**: Field Alpha, Sector B-5 (13.0827°, 80.2707°)
🕐 **Detected**: 15 minutes ago

📊 **Detection Analysis**:
• **Area Affected**: ~12 m²
• **Model Confidence**: 89%
• **Weed Type**: *Echinochloa crus-galli* (Barnyard Grass)
• **Segmentation Mask**: Generated with pixel-level accuracy

🎯 **Input Channels Used**: Blue, Green, Red, Red Edge, NIR

⚡ **Recommended Action**: Deploy targeted herbicide treatment within 24 hours to prevent spread.
📱 **View Segmentation Map**: http://your-dashboard.com/alert123
    """,
    
    "disease": """
🚨 **CNN DISEASE DETECTION ALERT** 🚨

🦠 **Detected Disease**: Rice Blast (Early Stage)
📍 **Location**: Northern quadrant, Grid N4-N6
🕐 **Detected**: 30 minutes ago

📊 **Analysis**:
• **Affected Area**: ~8% of monitored region
• **Confidence**: 91%
• **Symptom Pattern**: Characteristic lesions on leaf surfaces
• **Growth Stage Impact**: Early, intervention possible

💊 **Recommended Treatment**: Apply fungicide spray immediately
🔬 **Treatment Window**: 48 hours for maximum efficacy
📱 **Full Disease Report**: http://your-dashboard.com/disease456
    """,
    
    "health": """
📉 **MULTI-INDEX CROP HEALTH ALERT** 📉

📊 **Vegetation Indices Detected Decline**:
📍 **Location**: Southern plot, Grid S2-S5
🕐 **Detected**: 45 minutes ago

📈 **Index Changes**:
• **NDVI**: 0.78 → 0.61 (22% decline)
• **NDRE**: 0.72 → 0.58 (nitrogen stress indicated)
• **GNDVI**: 0.70 → 0.55 (biomass reduction)
• **Health Score**: 85 → 68 (significant drop)

🔍 **Possible Causes**: Nitrogen deficiency or water stress
🧪 **CNN Analysis**: Texture patterns suggest nutrient deficiency

💡 **Recommendations**:
1. Immediate nitrogen application (NDRE analysis)
2. Soil moisture check and irrigation if needed
3. Leaf tissue sampling for validation

📱 **Full Health Report**: http://your-dashboard.com/health321
    """,
    
    "fertilizer": """
🧪 **CNN FERTILIZATION ANALYSIS ALERT** 🧪

🔬 **Nutrient Requirement Predictions**:
📍 **Field Location**: Central growing area
🕐 **Analysis**: Latest multispectral scan

📊 **Predicted Requirements (0-1 scale)**:
• **Nitrogen (N)**: 0.72 → **HIGH DEFICIENCY** - Apply immediately
• **Phosphorus (P)**: 0.35 → Adequate, monitor
• **Potassium (K)**: 0.42 → Adequate, routine maintenance

💯 **Overall Health Score**: 68/100

🧠 **CNN Analysis Details**:
• Texture analysis: Chlorotic patterns detected
• Spatial patterns: Deficiency concentrated in patches
• Historical data: N-deficiency aligns with NDVI decline

🎯 **Recommended Action**: 
1. Apply 60 kg/ha Urea or equivalent nitrogen source
2. Consider foliar spray for rapid uptake
3. Re-assess in 10-12 days with multispectral imaging

📱 **Nutrient Report**: http://your-dashboard.com/fertilizer789
    """
}

# System configuration
BOT_CONFIG = {
    "max_subscribers": 1000,
    "alert_cooldown": 300,  # 5 minutes between similar alerts
    "default_scan_interval": 15,  # days
    "supported_languages": ["en", "hi", "ta"],
    "dashboard_base_url": "http://your-dashboard.com"
}

# Field monitoring thresholds
MONITORING_THRESHOLDS = {
    "ndvi_critical": 0.3,
    "ndvi_warning": 0.5,
    "ndvi_good": 0.7,
    "soil_moisture_min": 30,
    "soil_moisture_max": 70,
    "temperature_stress": 35,
    "weed_coverage_alert": 5  # percentage
}
