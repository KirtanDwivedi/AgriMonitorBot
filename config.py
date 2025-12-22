"""
Configuration file for Rice Field AI Monitor Bot
Contains FAQ responses and sample alerts
"""

# FAQ Dictionary with keyword-based responses (25+ common farmer questions)
FAQ_DICT = {
    # Core Analysis Systems
    "weed": "🌾 **Weed Detection System (U-Net)**\n\n📡 **Input**: 5-channel multispectral images (Blue, Green, Red, Red Edge, NIR)\n🧠 **Model**: U-Net encoder-decoder architecture\n📊 **Accuracy**: >85% detection with segmentation masks\n🎯 **Output**: Precise weed location maps with confidence scores\n\nYou'll receive real-time alerts with GPS coordinates when weeds are detected!",
    
    "health": "🌱 **Crop Health Analysis System**\n\n📈 **Vegetation Indices Calculated**:\n• **NDVI** = (NIR - Red) / (NIR + Red) - Overall health indicator\n• **NDRE** = (NIR - Red Edge) / (NIR + Red Edge) - Nitrogen status\n• **GNDVI** = (NIR - Green) / (NIR + Green) - Biomass estimation\n\n💯 **Health Score**: 0-100 scale based on vegetation vigor\n🔍 **Outputs**: Health maps, stress detection, vegetation distribution analysis",
    
    "yield": "📊 **Yield Prediction Ensemble**\n\n🤖 **Models**: Random Forest + Gradient Boosting ensemble\n📥 **Input Features**:\n• Multispectral image analysis\n• NDVI and vegetation indices\n• Growth stage classification\n• Environmental data (weather patterns)\n\n📤 **Output**: Predicted yield (tons/hectare) with confidence intervals\n📈 Based on real-time health metrics and historical data",
    
    "fertilizer": "🧪 **Fertilization Analysis (CNN)**\n\n🔬 **Nutrient Predictions**:\n• **Nitrogen (N)**: 0-1 scale requirement level\n• **Phosphorus (P)**: 0-1 scale requirement level\n• **Potassium (K)**: 0-1 scale requirement level\n\n📊 **Analysis**: Texture analysis, spatial patterns, deficiency detection\n💯 **Health Score**: Overall plant vigor on 0-100 scale\n\nSite-specific recommendations for optimal crop nutrition!",
    
    "ndvi": "📈 **NDVI (Normalized Difference Vegetation Index)**\n\nFormula: NDVI = (NIR - Red) / (NIR + Red)\n\n**Scale**: -1 to +1\n• **>0.7**: Excellent vigor, healthy vegetation\n• **0.5-0.7**: Good health, monitor for stress\n• **0.3-0.5**: Stressed vegetation, intervention needed\n• **<0.3**: Critical condition, immediate action required\n\nHigher NDVI = Higher chlorophyll content and photosynthetic activity",
    
    "irrigation": "💧 **Smart Irrigation Monitoring**\n\n📡 **Tracking**: Soil moisture, weather forecasts, crop water requirements\n⚙️ **Optimization**: Water usage efficiency, prevent stress\n🌡️ **Thresholds**: Monitors temperature stress and moisture balance\n\nAutomated recommendations for optimal irrigation timing and volume",
    
    "disease": "🦠 **Disease Detection System**\n\n🔍 **Common Rice Diseases Detected**:\n• Rice Blast - Fungal infection on leaves\n• Rice Blight - Affects leaf sheaths and panicles\n• Sheath Rot - Degrades rice grain quality\n\n🤖 **Method**: Computer vision & CNN analysis\n⚠️ **Early Detection**: Identifies symptoms before significant crop loss\n💊 **Prevention**: Enables preventive fungicide treatment",
    
    "weather": "🌤️ **Integrated Weather Monitoring**\n\n📊 **Real-time Data**:\n• Temperature, Humidity, Rainfall, Wind patterns\n• Growth stage impact assessment\n• Pest pressure predictions\n\n🔮 **Forecasts**: Future conditions affecting crop growth\n⚡ **Alerts**: Critical weather events with automated recommendations",
    
    # Growth Stage Questions
    "growth": "🌱 **Growth Stage Assessment**\n\n**Rice Growth Stages**:\n1. **Vegetative** (0-30 days) - Germination & seedling\n2. **Tillering** (30-60 days) - Shoot development\n3. **Heading** (60-75 days) - Panicle emergence\n4. **Flowering** (75-85 days) - Pollination & grain development\n5. **Maturity** (85-120 days) - Grain hardening\n\n📊 Our system identifies current stage from image analysis for optimal management timing.",
    
    "seedling": "🌱 **Seedling Stage Management**\n\n📅 **Duration**: 0-30 days after germination\n💧 **Water**: Keep paddy flooded 2-3 cm\n🌡️ **Temperature**: Optimal 25-30°C\n🧪 **Fertilizer**: 50% N applied at this stage\n⚠️ **Risks**: Damping off, seedling blight\n\n💡 **Recommendation**: Monitor moisture daily and watch for fungal infections.",
    
    "tillering": "🌾 **Tillering Stage (30-60 days)**\n\n📈 **Key Point**: Maximum nutrient uptake period\n💧 **Water Management**: Maintain 5 cm standing water\n🧪 **Fertilizer**: Apply remaining 50% N in 2-3 splits\n🔍 **Monitoring**: Count tillers/hill (target: 15-20)\n⚠️ **Watch for**: Insect pests, stem rot\n\n✅ **Best Practice**: Full weed control by 45 DAS (Days After Sowing)",
    
    "heading": "🌾 **Heading Stage (60-75 days)**\n\n📊 **Critical Period**: Panicle initiation to emergence\n💧 **Water**: Increase to 7-10 cm standing water\n🌤️ **Weather**: Monitor temperature (26-30°C optimal)\n⚠️ **Stress Risk**: High sensitivity to water stress\n🎯 **Focus**: No weeding, maintain water level\n\n📈 **System tracks**: Panicle emergence % and uniformity",
    
    "flowering": "🌸 **Flowering/Grain Filling (75-100 days)**\n\n🎯 **Critical**: Pollination & grain development\n💧 **Water**: Maintain 5 cm, then drain for ripening\n🌡️ **Temperature**: 25-28°C optimal (affects fertility)\n☀️ **Sunlight**: Needs 6-8 hours daily\n⚠️ **Risks**: High grain moisture loss, disease\n\n📊 **Monitor**: Grain filling progress via NDVI",
    
    "maturity": "🌾 **Maturity Stage (100-120 days)**\n\n💧 **Water**: Drain field for harvest\n🎨 **Color**: Panicles turn golden/brown\n📊 **Moisture**: Grain reaches 12-14% moisture\n✂️ **Harvest Window**: 5-7 days optimal\n⚠️ **Risk**: Over-ripening causes shattering\n\n📈 **Expected Yield**: Visible at this stage for final prediction",
    
    # Pest & Problem Management
    "pest": "🐛 **Pest Management System**\n\n**Common Rice Pests**:\n• **Stem Borers** - Larvae tunnel in stems\n• **Leaf Folders** - Wrap leaves for shelter\n• **Brown Plant Hoppers** - Suck plant sap\n• **Armyworms** - Chew leaves in clusters\n\n🔍 **Detection**: Our system identifies pest damage patterns\n💊 **Treatment**: Recommended pesticides per pest type\n🎯 **Timing**: Early intervention prevents 30-40% yield loss",
    
    "blast": "🦠 **Rice Blast Disease (Fungal)**\n\n**Symptoms**:\n• Diamond-shaped lesions on leaves\n• Gray center with brown borders\n• Affects leaf blade, neck, and panicle\n\n📊 **Risk Factors**: High humidity (>90%), temp 25-28°C\n💊 **Treatment**: Fungicides (Tricyclazole, Propiconazole)\n⚠️ **Severity**: Can cause 40-80% yield loss if untreated\n\n🔬 **Prevention**: Varietal resistance + chemical control",
    
    "blight": "🦠 **Bacterial Leaf Blight (BLB)**\n\n**Symptoms**:\n• Yellow-white lesions along leaf veins\n• V-shaped lesions starting from leaf tip\n• Progresses to entire leaf yellowing\n\n📊 **Conditions**: Warm (25-30°C), wet weather favors spread\n💧 **Water Role**: Infected water spreads bacteria\n💊 **Management**: Resistant varieties, drain infected water\n\n⚠️ **Impact**: 50-70% yield loss in severe cases",
    
    # Soil & Water Management
    "soil": "🌍 **Soil Health Analysis**\n\n📊 **Key Parameters**:\n• **pH**: 6.0-7.5 optimal for rice\n• **Organic Matter**: >2% is good\n• **Nitrogen**: 200-250 kg/ha requirement\n• **Phosphorus**: 40-60 kg/ha needed\n• **Potassium**: 40-60 kg/ha needed\n\n🔬 **Our System**: Analyzes deficiency patterns from multispectral imagery\n💡 **Action**: Recommends soil amendment & fertilizer timing",
    
    "water": "💧 **Water Management & Stress**\n\n**Water Stress Symptoms**:\n• Leaf rolling & wilting\n• Purple tinge to leaves\n• Reduced tiller number\n• Stunted growth\n\n📊 **Optimal Levels**:\n• Nursery: 5 cm standing water\n• Vegetative: 5 cm standing water\n• Reproductive: 7-10 cm standing water\n• Maturity: Drain field\n\n💡 **Our Detection**: Identifies water stress via vegetation indices",
    
    "nitrogen": "🧬 **Nitrogen Deficiency**\n\n**Symptoms**:\n• Yellowing starts from older leaves\n• Pale green/yellow color\n• Reduced tiller number\n• Stunted growth\n\n📊 **NDRE Index**: Shows nitrogen status accurately\n💊 **Treatment**: Split N application (3-4 times)\n• 25% at tillering\n• 40% at panicle initiation\n• 35% at heading\n\n⚠️ **Impact**: Can reduce yield by 30-40%",
    
    "phosphorus": "🧬 **Phosphorus Deficiency**\n\n**Symptoms**:\n• Purple/dark red coloration\n• Delayed maturity\n• Poor panicle development\n• Reduced grain filling\n\n📊 **Detection**: Unusual leaf discoloration patterns\n💊 **Solution**: Apply 40-60 kg/ha at planting\n🕐 **Timing**: Pre-transplant incorporation\n\n⚠️ **Effect**: Delays ripening by 2-3 weeks",
    
    "potassium": "🧬 **Potassium Deficiency**\n\n**Symptoms**:\n• Scorching on leaf margins\n• Brown streaks on stems\n• Weak straw, lodging risk\n• Poor root development\n\n📊 **Visibility**: Shows weak plant structure\n💊 **Application**: 40-60 kg/ha, split in 2 doses\n🕐 **Timing**: At tillering and heading stages\n\n⚠️ **Problem**: Causes lodging even at moderate winds",
    
    # Harvesting & Yield
    "harvest": "✂️ **Harvesting Guide**\n\n📊 **Ripeness Indicators**:\n• Panicles bend down due to grain weight\n• 80% of grains turned golden/brown\n• Grain moisture 12-14%\n• Straw turns yellow\n\n⏰ **Best Time**: Early morning when damp (reduces shattering)\n✂️ **Method**: Manual or mechanical harvester\n📊 **Timing**: Harvest within 5-7 days of maturity\n\n💡 **Our Prediction**: Estimates exact harvest date 30 days in advance",
    
    "storage": "🏪 **Post-Harvest Storage**\n\n📊 **Moisture Control**: Keep at 12-14% for storage\n🌡️ **Temperature**: Store below 20°C if possible\n🌫️ **Humidity**: <70% relative humidity\n💨 **Ventilation**: Ensure good air circulation\n🐛 **Pest Control**: Use appropriate fumigants\n\n⚠️ **Risk**: Poor storage can lead to 5-10% quality loss",
    
    # Advanced Topics
    "remote": "🛰️ **Multispectral Remote Sensing**\n\n📡 **5-Channel Imaging**:\n• Blue: 450-520 nm - Water absorption\n• Green: 520-600 nm - Chlorophyll peak\n• Red: 630-690 nm - Chlorophyll absorption\n• Red Edge: 700-750 nm - Vegetation boundary\n• NIR: 750-900 nm - Leaf scattering\n\n📊 **Indices Generated**: NDVI, NDRE, GNDVI, NDBI\n🎯 **Resolution**: Pixel-level analysis for precision agriculture",
    
    "organic": "🌿 **Organic Rice Farming**\n\n🚫 **No Synthetic**: Zero chemical fertilizers or pesticides\n🌱 **Methods**:\n• Green manure / Legume incorporation\n• Compost & farmyard manure (5-10 tons/ha)\n• Biological pest control (neem, trichoderma)\n• Mechanical weeding\n\n📊 **Yield**: 10-20% lower than conventional\n💰 **Premium**: 20-40% higher market price\n\n✅ **Sustainability**: Preserves soil health long-term",
    
    "climate": "🌍 **Climate-Smart Agriculture**\n\n⚠️ **Challenges**: Erratic rainfall, heat stress, flooding\n💡 **Strategies**:\n• Choose climate-resilient varieties\n• Adjust sowing dates (shift 10-15 days)\n• Mulching to retain moisture\n• Raised beds for flood-prone areas\n• Drip irrigation for drought conditions\n\n📈 **Benefit**: Increase resilience while maintaining yield",
    
    "price": "💰 **Market & Pricing Information**\n\n📊 **Factors Affecting Price**:\n• Grain quality (head rice %, size)\n• Moisture content (12-14% best)\n• Impurity levels (<3% ideal)\n• Market demand & season\n• Government support price\n\n💡 **Timing**: Prices typically higher off-season\n📱 **Updates**: Check daily market rates from authorized sources",
    
    "quality": "✨ **Rice Quality Standards**\n\n📊 **Grading Parameters**:\n• **Head Rice**: Unbroken kernels (>70% premium)\n• **Color**: White, uniform, free from discoloration\n• **Moisture**: 12-14% (storage stability)\n• **Impurities**: <3% (broken, stones, foreign matter)\n• **Chalky Grains**: <10% (affects clarity)\n\n🎯 **Our System**: Predicts final quality from growth monitoring"
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
