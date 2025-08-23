import os
import logging
import asyncio
from typing import Dict, List
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import FAQ_DICT, SAMPLE_ALERTS

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# File to store subscriber chat IDs
SUBSCRIBERS_FILE = "subscribers.txt"

class RiceFieldBot:
    def __init__(self):
        self.subscribers = self.load_subscribers()
    
    def load_subscribers(self) -> List[int]:
        """Load subscriber chat IDs from file"""
        try:
            with open(SUBSCRIBERS_FILE, 'r') as f:
                return [int(line.strip()) for line in f if line.strip()]
        except FileNotFoundError:
            return []
        except Exception as e:
            logger.error(f"Error loading subscribers: {e}")
            return []
    
    def save_subscribers(self) -> None:
        """Save subscriber chat IDs to file"""
        try:
            with open(SUBSCRIBERS_FILE, 'w') as f:
                for chat_id in self.subscribers:
                    f.write(f"{chat_id}\n")
        except Exception as e:
            logger.error(f"Error saving subscribers: {e}")
    
    def add_subscriber(self, chat_id: int) -> bool:
        """Add a new subscriber"""
        if chat_id not in self.subscribers:
            self.subscribers.append(chat_id)
            self.save_subscribers()
            return True
        return False
    
    def remove_subscriber(self, chat_id: int) -> bool:
        """Remove a subscriber"""
        if chat_id in self.subscribers:
            self.subscribers.remove(chat_id)
            self.save_subscribers()
            return True
        return False
    
    def find_response(self, message: str) -> str:
        """Find appropriate response based on keywords in message"""
        message_lower = message.lower()
        
        # Check for specific keyword combinations first
        if any(word in message_lower for word in ["weed", "weeds"]):
            if "alert" in message_lower or "detected" in message_lower:
                return "🌾 **Weed Alert Status**: Our latest multi-spectral scan detected weeds in Sector B-5.\n\n📍 **Location**: GPS: https://maps.google.com/?q=13.0827,80.2707\n\n🎯 **Recommended Action**: Targeted herbicide application within 48 hours\n\n📊 **Detection Confidence**: 87%\n\nType 'weed details' for comprehensive analysis report."
            else:
                return FAQ_DICT.get("weed", "No specific information available about weeds.")
        
        elif any(word in message_lower for word in ["health", "crop health", "ndvi"]):
            return "🌱 **Crop Health Report**:\n\n📈 **Overall NDVI Index**: 0.72 (Good vigor)\n\n⚠️ **Issue Detected**: Minor nitrogen deficiency in northern plot (Grid N3-N7)\n\n📊 **Health Distribution**:\n• Excellent: 45% of field\n• Good: 35% of field\n• Fair: 15% of field\n• Poor: 5% of field\n\n🔗 Detailed report available on your dashboard."
        
        elif any(word in message_lower for word in ["yield", "prediction", "harvest"]):
            return "📊 **Yield Prediction Analysis**:\n\n🌾 **Predicted Yield**: 6.2 tons/hectare\n\n🔬 **Variety**: Basmati (Premium grade)\n\n📅 **Harvest Window**: 45-50 days from today\n\n📈 **Confidence Level**: 92%\n\n💰 **Expected Revenue**: ₹2,48,000 per hectare (at current market rates)\n\nBased on current health metrics, weather patterns, and historical data."
        
        elif any(word in message_lower for word in ["action", "actions", "recommend", "do", "next"]):
            return "📋 **Recommended Actions**:\n\n1️⃣ **Immediate** (Next 24-48h):\n   • Inspect weed cluster at Sector B-5\n   • Apply targeted herbicide treatment\n\n2️⃣ **This Week**:\n   • Soil amendment for nitrogen deficiency (Northern plot)\n   • Check irrigation system pressure\n\n3️⃣ **Next 15 days**:\n   • Scheduled re-scan for progress monitoring\n   • Fertilizer application based on soil test\n\n🔔 **Next Alert**: Automated scan in 7 days"
        
        elif any(word in message_lower for word in ["fertilizer", "nutrition", "nutrient"]):
            return FAQ_DICT.get("fertilizer", "No specific fertilizer information available.")
        
        # Check individual keywords
        for keyword, response in FAQ_DICT.items():
            if keyword in message_lower:
                return response
        
        # Default response for unrecognized queries
        return "🤖 I'm your Rice Field AI assistant. I can help with:\n\n• Weed detection alerts\n• Crop health status\n• Yield predictions\n• Fertilizer recommendations\n• Action recommendations\n\nTry asking: 'How is my crop health?' or 'Any weed alerts?'"

# Initialize bot instance
rice_bot = RiceFieldBot()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    welcome_message = """
🌾 **Welcome to Rice Field AI Monitor** 🌾

🤖 Your intelligent farming assistant powered by AI and multi-spectral imaging.

**Available Commands:**
• `/help` - Show this help message
• `/subscribe` - Subscribe to field alerts
• `/unsubscribe` - Unsubscribe from alerts
• `/status` - Check subscription status

**Query Examples:**
• "Weed alert in my field?"
• "How is my crop health?"
• "What is the yield prediction?"
• "What actions should I take?"

💡 Just type your question in natural language - I'll understand!

Powered by Jetson Nano AI & Multi-spectral Imaging 🛰️
    """
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /help command"""
    await start_command(update, context)

async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /subscribe command"""
    chat_id = update.effective_chat.id
    
    if rice_bot.add_subscriber(chat_id):
        await update.message.reply_text(
            "✅ **Subscription Successful!**\n\n"
            "You will now receive automated alerts for:\n"
            "• Weed detection notifications\n"
            "• Crop health changes\n"
            "• Critical field conditions\n"
            "• Recommended actions\n\n"
            "Use `/unsubscribe` anytime to stop alerts.",
            parse_mode='Markdown'
        )
        logger.info(f"New subscriber: {chat_id}")
    else:
        await update.message.reply_text(
            "ℹ️ You are already subscribed to field alerts.\n\n"
            "Use `/unsubscribe` if you want to stop receiving notifications.",
            parse_mode='Markdown'
        )

async def unsubscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /unsubscribe command"""
    chat_id = update.effective_chat.id
    
    if rice_bot.remove_subscriber(chat_id):
        await update.message.reply_text(
            "✅ **Unsubscribed Successfully**\n\n"
            "You will no longer receive automated field alerts.\n\n"
            "Use `/subscribe` anytime to resume notifications.",
            parse_mode='Markdown'
        )
        logger.info(f"Subscriber removed: {chat_id}")
    else:
        await update.message.reply_text(
            "ℹ️ You are not currently subscribed to alerts.\n\n"
            "Use `/subscribe` to start receiving field notifications.",
            parse_mode='Markdown'
        )

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /status command"""
    chat_id = update.effective_chat.id
    is_subscribed = chat_id in rice_bot.subscribers
    
    status_message = f"""
📊 **Your Subscription Status**

🔔 **Alert Subscription**: {'✅ Active' if is_subscribed else '❌ Inactive'}
👥 **Total Subscribers**: {len(rice_bot.subscribers)}

**Last System Activity:**
• Weed scan: 2 hours ago
• Health analysis: 4 hours ago
• Weather sync: 1 hour ago

🤖 System Status: ✅ All monitoring systems operational
    """
    
    await update.message.reply_text(status_message, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular messages and provide responses based on keywords"""
    user_message = update.message.text
    response = rice_bot.find_response(user_message)
    
    await update.message.reply_text(response, parse_mode='Markdown')
    logger.info(f"Query from {update.effective_chat.id}: {user_message}")

async def send_alert(context: ContextTypes.DEFAULT_TYPE, alert_message: str) -> None:
    """Send alert to all subscribers (for testing and automated alerts)"""
    sent_count = 0
    failed_count = 0
    
    for chat_id in rice_bot.subscribers:
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=alert_message,
                parse_mode='Markdown'
            )
            sent_count += 1
            logger.info(f"Alert sent to {chat_id}")
        except Exception as e:
            logger.error(f"Failed to send alert to {chat_id}: {e}")
            failed_count += 1
    
    logger.info(f"Alert broadcast complete: {sent_count} sent, {failed_count} failed")

async def trigger_test_alert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Manually trigger a test alert (for testing purposes)"""
    if context.args and len(context.args) > 0:
        alert_type = context.args[0].lower()
        if alert_type in SAMPLE_ALERTS:
            alert_message = SAMPLE_ALERTS[alert_type]
            await send_alert(context, alert_message)
            await update.message.reply_text(
                f"✅ Test alert '{alert_type}' sent to {len(rice_bot.subscribers)} subscribers."
            )
        else:
            available_alerts = ", ".join(SAMPLE_ALERTS.keys())
            await update.message.reply_text(
                f"❌ Unknown alert type. Available: {available_alerts}"
            )
    else:
        # Send default weed alert
        alert_message = SAMPLE_ALERTS["weed"]
        await send_alert(context, alert_message)
        await update.message.reply_text(
            f"✅ Default weed alert sent to {len(rice_bot.subscribers)} subscribers."
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by Updates."""
    logger.error(f"Exception while handling an update: {context.error}")

def main() -> None:
    """Start the bot"""
    # Create Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("subscribe", subscribe_command))
    application.add_handler(CommandHandler("unsubscribe", unsubscribe_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("test_alert", trigger_test_alert))
    
    # Handle all text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Starting Rice Field AI Monitor Bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
