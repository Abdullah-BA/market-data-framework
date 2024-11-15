# GitHub Instructions

## Setting Up Your Repository

### 1. Initial Local Setup
```bash
# Initialize git in your project directory
git init

# Create initial commit
git add .
git commit -m "Initial commit"
```

### 2. Create GitHub Repository
1. Go to https://github.com
2. Click the '+' in the top right → 'New repository'
3. Fill in:
   - Repository name: `market-data-framework`
   - Description: "A flexible Python framework for fetching and managing financial market data"
   - Choose 'Public' or 'Private'
   - Check "Add a README file"
   - Choose "MIT License"
   - Add `.gitignore` template for Python

### 3. Connect Local to GitHub
```bash
# Add GitHub as remote repository
git remote add origin https://github.com/yourusername/market-data-framework.git

# Pull GitHub's initial setup (README, LICENSE, .gitignore)
git pull origin main --allow-unrelated-histories

# Push your code
git push -u origin main
```

### 4. Additional GitHub Setup

#### Add Repository Topics
Go to repository settings and add relevant topics:
- python
- finance
- trading
- market-data
- alpha-vantage
- yahoo-finance
- data-analysis

#### Create Branch Protection Rules
1. Go to Settings → Branches
2. Add rule for `main` branch:
   - Require pull request reviews
   - Require status checks to pass
   - Require up-to-date branches

#### Set Up GitHub Pages (Optional)
1. Go to Settings → Pages
2. Source: Deploy from a branch
3. Branch: main/docs

## Installing from GitHub

### Method 1: pip install directly from GitHub
```bash
# Latest version
pip install git+https://github.com/yourusername/market-data-framework.git

# Specific version/tag
pip install git+https://github.com/yourusername/market-data-framework.git@v1.0.0
```

### Method 2: Clone and Install
```bash
# Clone the repository
git clone https://github.com/yourusername/market-data-framework.git
cd market-data-framework

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in editable mode
pip install -e .
```

### Method 3: Download ZIP
1. Go to the GitHub repository
2. Click 'Code' → 'Download ZIP'
3. Extract the ZIP file
4. Open terminal in extracted directory
5. Run `pip install .`

## Maintaining Your Repository

### Creating a New Release
1. Update version in `setup.py`
2. Create and push tag:
```bash
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
```
3. Go to GitHub → Releases → Draft new release
4. Choose your tag
5. Add release notes
6. Publish release

### Updating Documentation
1. Update docs in `docs/` directory
2. Push changes to main branch
3. GitHub Pages will automatically update

### Managing Issues
1. Use labels effectively:
   - bug
   - enhancement
   - documentation
   - help wanted
2. Use issue templates
3. Respond promptly to issues

### Managing Pull Requests
1. Review code thoroughly
2. Ensure tests pass
3. Check code coverage
4. Verify documentation updates