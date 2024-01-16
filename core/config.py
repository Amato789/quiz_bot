import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
ADMIN_ID = os.environ.get("ADMIN_ID")