import os

# Define files and optional initial content
files_with_content = {
    ".vscode/settings.json": '{}',
    ".github/workflows/ci.yml": """name: CI Setup

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Check Python version
      run: python --version
""",
    "requirements.txt": "pandas\nnumpy\nmatplotlib\nseaborn\nscipy\nstreamlit\n",
    "README.md": "# Solar Challenge Week 1\n\nProject for 10 Academy - AIM Week 0.",
    ".gitignore": "data/\n__pycache__/\n.ipynb_checkpoints/\n*.csv\n",
    "app/main.py": "# Streamlit app entry point\nimport streamlit as st",
    "app/utils.py": "# Utility functions for Streamlit app",
    "notebooks/.keep": "",
    "src/.keep": "",
    "scripts/.keep": "",
    "tests/.keep": ""
}

# Create files and necessary directories
for file_path, content in files_with_content.items():
    dir_path = os.path.dirname(file_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)

print("✅ All folders and files created with initial content.")
