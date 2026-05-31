"""
Configuration settings for the Document Intelligence Chatbot frontend
"""

import os
from pathlib import Path

# API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))

# Storage Configuration
CONVERSATIONS_DIR = os.getenv("CONVERSATIONS_DIR", "conversations")
UPLOADS_DIR = os.getenv("UPLOADS_DIR", "uploads")

# UI Configuration
APP_TITLE = "Document Intelligence Chatbot"
APP_ICON = "🤖"
PAGE_LAYOUT = "wide"

# File Upload Configuration
ALLOWED_FILE_TYPES = ["pdf", "txt", "docx", "doc", "xlsx", "csv"]
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "50"))
MAX_FILES_PER_CONVERSATION = int(os.getenv("MAX_FILES_PER_CONVERSATION", "10"))

# Chat Configuration
MAX_CHAT_HISTORY = int(os.getenv("MAX_CHAT_HISTORY", "100"))
AUTO_CLEAR_HISTORY_DAYS = int(os.getenv("AUTO_CLEAR_HISTORY_DAYS", "30"))
ENABLE_CHAT_EXPORT = True
ENABLE_CONVERSATION_SEARCH = True

# Display Configuration
SHOW_FILE_UPLOAD_AREA = True
SHOW_CONVERSATION_HISTORY = True
SHOW_MESSAGE_TIMESTAMPS = True
ENABLE_MESSAGE_REACTIONS = False
DARK_MODE_ENABLED = False

# Performance Configuration
ENABLE_STREAMING_RESPONSES = False
AUTO_SAVE_INTERVAL = 5  # seconds
CONVERSATION_CLEANUP_INTERVAL = 3600  # seconds

# Appearance Configuration
THEME_COLOR_USER = "#0084ff"
THEME_COLOR_ASSISTANT = "#11a37d"
THEME_COLOR_SYSTEM = "#f59e0b"

# Feature Flags
FEATURE_CONVERSATION_SHARING = False
FEATURE_VOICE_INPUT = False
FEATURE_IMAGE_SUPPORT = False
FEATURE_CODE_HIGHLIGHTING = True
FEATURE_TABLE_SUPPORT = True

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
ENABLE_LOGGING = True
LOG_FILE = "chatbot.log"

# Create required directories
Path(CONVERSATIONS_DIR).mkdir(parents=True, exist_ok=True)
Path(UPLOADS_DIR).mkdir(parents=True, exist_ok=True)


def get_config():
    """Get all configuration as dictionary"""
    return {
        "api": {
            "base_url": API_BASE_URL,
            "timeout": API_TIMEOUT,
        },
        "storage": {
            "conversations_dir": CONVERSATIONS_DIR,
            "uploads_dir": UPLOADS_DIR,
        },
        "ui": {
            "title": APP_TITLE,
            "icon": APP_ICON,
            "layout": PAGE_LAYOUT,
        },
        "files": {
            "allowed_types": ALLOWED_FILE_TYPES,
            "max_size_mb": MAX_FILE_SIZE_MB,
            "max_per_conversation": MAX_FILES_PER_CONVERSATION,
        },
        "chat": {
            "max_history": MAX_CHAT_HISTORY,
            "auto_clear_days": AUTO_CLEAR_HISTORY_DAYS,
            "export_enabled": ENABLE_CHAT_EXPORT,
            "search_enabled": ENABLE_CONVERSATION_SEARCH,
        },
        "features": {
            "conversation_sharing": FEATURE_CONVERSATION_SHARING,
            "voice_input": FEATURE_VOICE_INPUT,
            "image_support": FEATURE_IMAGE_SUPPORT,
            "code_highlighting": FEATURE_CODE_HIGHLIGHTING,
            "table_support": FEATURE_TABLE_SUPPORT,
        },
    }
