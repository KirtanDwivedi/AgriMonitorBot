"""
Configuration file for Rice Field AI Monitor Bot
Contains FAQ responses and sample alerts
"""

# FAQ Dictionary with keyword-based responses
FAQ_DICT = {
    "weed": "🌾 Our AI system uses multi-spectral imaging and CNN models on Jetson Nano to detect weeds with over 85% accuracy. You will receive real-time alerts with GPS locations when weeds are detected in your field.",
    
    "health": "🌱 Crop health is assessed using NDVI and other vegetation indices from multi-spectral images, analyzed by our advanced AI models. We monitor chlorophyll content, water stress, and overall plant vigor.",
    
    "yield": "📊 Yield prediction is based on our proprietary AI model that analyzes historical data, real-time plant health metrics, weather conditions, and growth stage progression to provide accurate forecasts.",
    
    "fertilizer": "🧪 Our system provides site-specific fertilization recommendations using soil analysis, plant tissue testing, and AI-driven nutrient optimization to improve soil health and maximize crop yield.",
    
    "ndvi": "📈 NDVI (Normalized Difference Vegetation Index) measures plant health on a scale from -1 to +1. Values closer to +1 indicate healthier vegetation with higher chlorophyll content and better photosynthetic activity.",
    
    "irrigation": "💧 Our smart irrigation system monitors soil moisture, weather forecasts, and crop water requirements to optimize water usage and prevent both water stress and over-irrigation.",
    
    "disease": "🦠 Disease detection uses computer vision to identify early symptoms of common rice diseases like blast, blight, and sheath rot, enabling preventive treatment before significant crop loss.",
    
    "weather": "🌤️ Integrated weather monitoring provides real-time and forecast data including temperature, humidity, rainfall, and wind patterns that affect crop growth and pest pressure."
}

# Sample alerts for testing the push notification system
SAMPLE_ALERTS = {
    "weed": """
🚨 **URGENT WEED ALERT** 🚨

📍 **Location**: Field Alpha, Sector B-5
🕐 **Detected**: 15 minutes ago
🎯 **Confidence**: 89%

🔍 **Details**: New weed cluster detected covering approximately 12 m² area.

📱 **View Details**: http://your-dashboard.com/alert123

⚡ **Immediate Action Required**: Deploy targeted herbicide treatment within 24 hours to prevent spread.
    """,
    
    "disease": """
🚨 **DISEASE ALERT** 🚨

🦠 **Disease Type**: Early blast symptoms detected
📍 **Location**: Northern quadrant, Grid N4-N6
🕐 **Detected**: 30 minutes ago

📊 **Affected Area**: ~8% of monitored region
🎯 **Confidence**: 91%

💊 **Recommended Treatment**: Apply fungicide spray immediately
📱 **Full Report**: http://your-dashboard.com/disease456
    """,
    
    "irrigation": """
💧 **IRRIGATION ALERT** 💧

⚠️ **Soil Moisture**: Below optimal threshold
📍 **Location**: Eastern sectors E1-E8
🕐 **Detected**: 1 hour ago

📊 **Current Level**: 22% (Optimal: 35-45%)
🌡️ **Temperature**: 34°C (High stress conditions)

💡 **Action**: Initiate irrigation cycle within 2 hours
📱 **Monitor**: http://your-dashboard.com/irrigation789
    """,
    
    "health": """
📉 **CROP HEALTH ALERT** 📉

🌾 **NDVI Drop Detected**: Significant decline in vegetation index
📍 **Location**: Southern plot, Grid S2-S5
🕐 **Detected**: 45 minutes ago

📊 **NDVI Change**: 0.78 → 0.61 (22% decline)
🔍 **Possible Causes**: Nutrient deficiency or water stress

🔬 **Investigation**: Soil sampling recommended
📱 **Details**: http://your-dashboard.com/health321
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
