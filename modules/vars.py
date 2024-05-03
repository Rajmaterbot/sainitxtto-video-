from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = "16712603"
API_HASH = "62e7bdb76c9d12f90021a5a90bb2402f"
BOT_TOKEN = "6824877465:AAEVT3DeNAJDvIrKkH8u3TUu7jjx9YN8lWI"
OWNER_ID = "1227089641"
SUDO_USERS = list(map(int, getenv("SUDO_USERS","1227089641").split()))
