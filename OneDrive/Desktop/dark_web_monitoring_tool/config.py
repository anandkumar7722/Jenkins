from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
HIBP_API_KEY = os.getenv("HIBP_API_KEY")


# config.py

# Email configuration for sending alerts
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"

# Database configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "dark_web_monitoring"

# API and service configurations (example API keys)
HIBP_API_KEY = "your_hibp_api_key"  # If using HaveIBeenPwned API
USER_AGENT = "dark-web-monitor-tool"
