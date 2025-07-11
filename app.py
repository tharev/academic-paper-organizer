"""
Academic Paper Organizer - AI-Powered Research Management System
Main Flask Application

This application provides an intelligent academic paper organization system
with AI-powered features for paper analysis, categorization, and management.
"""

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import json
import requests
from datetime import datetime
from paper_manager import PaperManager
from ai_processor import AIProcessor
from database import db, User, Paper, Category, Tag
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
