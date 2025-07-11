"""
Configuration settings for Academic Paper Organizer
AI-powered academic paper organization and management system
"""

import os
from pathlib import Path

# Base Configuration
class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///academic_papers.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File upload settings
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx'}
    
    # AI API Settings
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    FELLOU_AI_API_KEY = os.environ.get('FELLOU_AI_API_KEY')
    FELLOU_AI_BASE_URL = os.environ.get('FELLOU_AI_BASE_URL', 'https://api.fellou.ai')
    
