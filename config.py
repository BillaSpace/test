import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot configuration
TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID', '5960968099'))

# Validate required environment variables
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required")

if ADMIN_ID == 0:
    raise ValueError("ADMIN_ID environment variable is required")

# Optional: Add other configuration variables
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
