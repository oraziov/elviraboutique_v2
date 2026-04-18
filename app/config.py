import os
from dotenv import load_dotenv

load_dotenv()

SHOP = os.getenv("SHOP")
TOKEN = os.getenv("TOKEN")
API_VERSION = os.getenv("API_VERSION", "2024-01")
