#!/usr/bin/env python3
"""
Repository Setup Automation Script for Slow Productivity AI Project
This script automates the creation of a new GitHub repository with all necessary initial files.
"""

import os
import subprocess
import requests
import json
from pathlib import Path

# GitHub API Configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME")
REPO_NAME = "slow-productivity-ai"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_github_repository():
    """Create a new GitHub repository"""
    print(f"Creating GitHub repository: {REPO_NAME}...")
    
    api_url = "https://api.github.com/user/repos"
    payload = {
        "name": REPO_NAME,
        "description": "Automating Knowledge & Task Management with Offline Hugging Face, n8n & Obsidian",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True,
        "auto_init": True
    }
    
    response = requests.post(api_url, headers=HEADERS, data=json.dumps(payload))
    
    if response.status_code == 201:
        print(f"Repository created successfully: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
        return True
    else:
        print(f"Failed to create repository. Status code: {response.status_code}")
        print(f"Response: {response.json()}")
        return False

def initialize_local_repository():
    """Initialize local git repository and add remote"""
    print("Setting up local repository...")
    
    # Create project directory
    repo_path = Path(REPO_NAME)
    repo_path.mkdir(exist_ok=True)
    os.chdir(repo_path)
    
    # Initialize git
    subprocess.run(["git", "init"], check=True)
    
    # Add remote
    subprocess.run(["git", "remote", "add", "origin", 
                   f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"], check=True)
    
    # Create main branch
    subprocess.run(["git", "checkout", "-b", "main"], check=True)
    
    print("Local repository initialized successfully.")

def create_project_structure():
    """Create the initial project structure with directories"""
    print("Creating project structure...")
    
    directories = [
        "src/nlp_pipeline",
        "src/obsidian_integration",
        "src/n8n_workflows",
        "docs",
        "tests",
        "data/sample_transcripts",
        "data/sample_emails",
        "data/sample_notes",
        "presentation"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("Project structure created successfully.")

def create_readme():
    """Create README.md file"""
    readme_content = """# Slow Productivity AI

Automating Knowledge & Task Management with Offline Hugging Face, n8n & Obsidian

## Overview

This project implements a slow productivity AI approach, inspired by Cal Newport, that leverages offline, 
open-source automation using Hugging Face, n8n, and Obsidian. By structuring knowledge into meaningful 
tasks without disrupting deep work, we can create a sustainable, low-distraction workflow—working smarter, 
not just faster.

## Components

- **Hugging Face Transformers**: Local NLP for extracting insights from notes, emails, and transcripts
- **n8n**: Self-hosted automation workflows to connect data sources
- **Obsidian**: Knowledge management with structured notes
- **GitHub Issues**: Task management integrated with knowledge base

## Getting Started

[Installation and setup instructions will be added]

## Documentation

See the [docs](./docs) directory for detailed documentation.

## License

[MIT License](LICENSE)
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    print("README.md created successfully.")

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg
.env
.venv
venv/
ENV/

# Obsidian
.obsidian/workspace.json
.obsidian/plugins/
.obsidian/themes/
.obsidian/snippets/

# n8n
.n8n/

# Node.js
node_modules/
npm-debug.log
yarn-debug.log
yarn-error.log

# IDEs and editors
.idea/
.vscode/
*.swp
*.swo
*~

# OS-specific
.DS_Store
Thumbs.db
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    
    print(".gitignore created successfully.")

def create_requirements_file():
    """Create requirements.txt file"""
    requirements_content = """# Core dependencies
transformers==4.30.2
torch==2.0.1
numpy==1.24.3
pandas==2.0.2
scikit-learn==1.2.2

# NLP specific
nltk==3.8.1
spacy==3.6.0

# API and integration
requests==2.31.0
fastapi==0.98.0
uvicorn==0.22.0

# Testing
pytest==7.3.1
pytest-cov==4.1.0

# Documentation
mkdocs==1.4.3
mkdocs-material==9.1.17
"""
    
    with open("requirements.txt", "w") as f:
        f.write(requirements_content)
    
    print("requirements.txt created successfully.")

def create_dockerfile():
    """Create Dockerfile for containerization"""
    dockerfile_content = """FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Command to run when container starts
CMD ["python", "src/app.py"]
"""
    
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)
    
    print("Dockerfile created successfully.")

def create_github_workflow():
    """Create GitHub Actions workflow for CI/CD"""
    os.makedirs(".github/workflows", exist_ok=True)
    
    workflow_content = """name: CI/CD Pipeline

on:
  push:
    branches: [ main, development ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        pip install pytest pytest-cov
    - name: Test with pytest
      run: |
        pytest --cov=src
"""
    
    with open(".github/workflows/ci-cd.yml", "w") as f:
        f.write(workflow_content)
    
    print("GitHub Actions workflow created successfully.")

def initial_commit():
    """Make initial commit and push to GitHub"""
    print("Making initial commit...")
    
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial repository setup"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    
    print("Initial commit pushed to GitHub.")

def main():
    """Main function to run all setup steps"""
    if not GITHUB_TOKEN:
        print("ERROR: GITHUB_TOKEN environment variable not set. Please set it and try again.")
        return
    
    if not GITHUB_USERNAME:
        print("ERROR: GITHUB_USERNAME environment variable not set. Please set it and try again.")
        return
    
    # Execute steps
    if create_github_repository():
        initialize_local_repository()
        create_project_structure()
        create_readme()
        create_gitignore()
        create_requirements_file()
        create_dockerfile()
        create_github_workflow()
        initial_commit()
        
        print("\nRepository setup complete!")
        print(f"Repository URL: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
        print("\nNext steps:")
        print("1. Clone the repository: git clone https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git")
        print("2. cd into the repository: cd {REPO_NAME}")
        print("3. Create a virtual environment: python -m venv venv")
        print("4. Activate the virtual environment: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)")
        print("5. Install dependencies: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
