# Installation Guide

## Prerequisites

Before installing the Market Data Framework, ensure you have:
- Python 3.8 or higher
- pip (Python package installer)
- git (for installation from GitHub)

## Installation Methods

### 1. Install from PyPI (Recommended for Users)
```bash
pip install market-data-framework
```

### 2. Install from GitHub (Recommended for Developers)

#### Option A: Direct Installation
```bash
pip install git+https://github.com/yourusername/market-data-framework.git
```

#### Option B: Clone and Install
```bash
# Clone the repository
git clone https://github.com/yourusername/market-data-framework.git

# Change to project directory
cd market-data-framework

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install package in editable mode
pip install -e .
```

### 3. Install from Source Distribution

#### Option A: Download Release
1. Go to https://github.com/yourusername/market-data-framework/releases
2. Download the latest release .tar.gz file
3. Install using pip:
```bash
pip install market-data-framework-x.x.x.tar.gz
```

#### Option B: Download ZIP
1. Go to https://github.com/yourusername/market-data-framework
2. Click 'Code' → 'Download ZIP'
3. Extract the ZIP file
4. Install using pip:
```bash
cd market-data-framework-main
pip install .
```

## Verification

After installation, verify it works:

```python
from market_data import DataFrequency, MarketDataRequest

# If no errors occur, installation was successful
print("Installation successful!")
```

## Configuration

1. Copy the example configuration:
```bash
cp config.example.py config.py
```

2. Edit `config.py` with your settings:
```python
ALPHA_VANTAGE_API_KEY = "your_api_key_here"
```

## Common Issues

### Missing Dependencies
If you see `ImportError`, ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Permission Issues
If you see permission errors:
```bash
# On Unix/Linux/MacOS:
sudo pip install market-data-framework

# Or install for current user only:
pip install --user market-data-framework
```

### Virtual Environment Issues
If you have problems with virtual environment:
```bash
# Remove existing venv
rm -rf venv  # On Windows: rmdir /s /q venv

# Create new venv
python -m venv venv

# Activate and install
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Updating

To update to the latest version:

```bash
# If installed from PyPI:
pip install --upgrade market-data-framework

# If installed from GitHub:
pip install --upgrade git+https://github.com/yourusername/market-data-framework.git
```

## Uninstalling

To remove the package:
```bash
pip uninstall market-data-framework
```