# Overview

A Python Telegram bot for an AI-driven rice field monitoring system that serves as an information and alert interface for farmers. The bot provides real-time field status updates, answers farmer queries about crop health, weed detection, and yield predictions, and delivers automated alerts when critical conditions are detected in their fields.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Bot Framework
- **Telegram Bot API**: Uses python-telegram-bot library for handling commands and messages
- **Asynchronous Processing**: Built with asyncio for handling multiple concurrent user interactions
- **Command-based Interface**: Structured around specific commands (/start, /help, /subscribe, /unsubscribe)

## Query Processing
- **Keyword Matching**: Simple keyword-based response system using FAQ_DICT for instant farmer queries
- **Pre-defined Responses**: Structured answers covering weed detection, crop health, yield prediction, fertilization, and disease monitoring
- **Real-time Information**: Responses include specific field locations, confidence levels, and actionable recommendations

## Data Management
- **File-based Storage**: Uses simple text file (subscribers.txt) for storing subscriber chat IDs
- **In-memory Processing**: FAQ responses and alert templates stored in Python dictionaries for fast access
- **Persistent Subscriptions**: Subscriber data persists across bot restarts

## Alert System
- **Push Notifications**: Proactive alert delivery to subscribed users
- **Alert Templates**: Pre-formatted messages for different alert types (weed, disease, weather)
- **Targeted Messaging**: Alerts include GPS coordinates, confidence levels, and immediate action requirements

## AI Integration Interface
- **Multi-spectral Imaging**: References CNN models on Jetson Nano for weed detection (85% accuracy)
- **NDVI Analysis**: Vegetation index calculations for crop health assessment
- **Predictive Analytics**: Yield prediction based on historical data and real-time metrics

# External Dependencies

## Core Libraries
- **python-telegram-bot**: Telegram Bot API wrapper for message handling and bot operations
- **asyncio**: Python's built-in asynchronous I/O framework for concurrent operations

## AI/ML References
- **Jetson Nano**: Edge computing platform for running CNN models
- **Multi-spectral Imaging**: Hardware for capturing vegetation indices and crop analysis
- **NDVI Sensors**: Equipment for normalized difference vegetation index calculations

## Data Sources
- **Weather APIs**: Integration points for real-time weather data and forecasts
- **GPS Systems**: Location tracking for field mapping and alert positioning
- **Soil Sensors**: IoT devices for moisture and nutrient monitoring

## Future Integrations
- **Web Dashboard**: HTTP endpoints referenced in alert messages for detailed reporting
- **Database Systems**: Scalable storage solutions for replacing file-based subscriber management
- **Google Maps API**: For GPS coordinate visualization in alerts