#!/usr/bin/env python3
"""
Academic Paper Organizer - Example Workflow Script
==================================================

This script demonstrates how to use the Academic Paper Organizer
to automatically process, categorize, and manage research papers.

Author: Academic Paper Organizer Team
Date: 2025-01-07
"""

import os
import sys
import json
import requests
from datetime import datetime
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from models import User, Paper, Collection, Annotation
from config import Config
