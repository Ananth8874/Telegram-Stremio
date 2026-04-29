from os import getenv, path
from dotenv import load_dotenv

load_dotenv(path.join(path.dirname(path.dirname(__file__)), "config.env"))

class Telegram:
    API_ID = int(getenv("API_ID", "22977776"))
    API_HASH = getenv("API_HASH", "2ac7223d720bdeec757cbc88ced57224")
    BOT_TOKEN = getenv("BOT_TOKEN", "8224774305:AAHjHNJRMJQnBj8XZUZOcSmqCSzGGehaV8s")
    HELPER_BOT_TOKEN = getenv("HELPER_BOT_TOKEN", "")

    BASE_URL = getenv("BASE_URL", "https://tamizhzone.koyeb.app").rstrip('/')
    PORT = int(getenv("PORT", "8080"))

    PARALLEL = int(getenv("PARALLEL", "1"))
    PRE_FETCH = int(getenv("PRE_FETCH", "1"))

    AUTH_CHANNEL = [channel.strip() for channel in (getenv("AUTH_CHANNEL") or "-1003974332689").split(",") if channel.strip()]
    DATABASE = [db.strip() for db in (getenv("DATABASE") or "mongodb+srv://jeevanantham8157:1055221@tamizhzone.b0bx6bx.mongodb.net/?appName=TamizhZone, mongodb+srv://jeevanantham8157:1055221@itzheartbot1.63xqs.mongodb.net/?appName=Itzheartbot1").split(",") if db.strip()]

    TMDB_API = getenv("TMDB_API", "57d8345a6dd40ec2ca3cc43ba707457c")

    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
    UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "")

    OWNER_ID = int(getenv("OWNER_ID", "8537200428"))
    
    REPLACE_MODE = getenv("REPLACE_MODE", "true").lower() == "true"
    HIDE_CATALOG = getenv("HIDE_CATALOG", "false").lower() == "true"

    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "fyvio")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "fyvio")
    
    SUBSCRIPTION = getenv("SUBSCRIPTION", "false").lower() == "true"
    SUBSCRIPTION_GROUP_ID = int(getenv("SUBSCRIPTION_GROUP_ID", "0"))
    SUBSCRIPTION_URL = getenv("SUBSCRIPTION_URL", "https://t.me/")
    APPROVER_IDS = [int(x.strip()) for x in (getenv("APPROVER_IDS") or "").split(",") if x.strip().isdigit()]

    PROXY = getenv("Proxy", "false").lower() == "true"
    PROXY_TYPE = getenv("ProxyType", "HTTPS")
    HTTP_PROXY_URL = getenv("HTTP_Proxy_URL", "")
    SHOW_PROXY_AND_NON_PROXY_BOTH = getenv("SHOW_ProxyAndNonProxyBoth", "false").lower() == "true"
