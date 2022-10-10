# FILES BELONGS TO @rocks_fighters 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
SESSION = os.getenv("SESSION", "")
OWNER = os.getenv("OWNER", "")
SUPPORT = os.getenv("SUPPORT", "opraidmaster")
SUDO_USERS = os.getenv("SUDO_USERS", "")
