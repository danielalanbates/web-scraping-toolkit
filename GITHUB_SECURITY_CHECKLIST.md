# GitHub Security & Publishing Checklist

⚠️ **IMPORTANT: Read this BEFORE uploading ANY project to GitHub!**

---

## 🚨 Security Requirements (MANDATORY)

### Before Committing ANY Code:

#### 1. **Remove ALL API Keys and Secrets**
- ❌ OpenAI API keys
- ❌ Anthropic API keys
- ❌ AWS credentials
- ❌ Database passwords
- ❌ Email passwords (SMTP)
- ❌ OAuth tokens
- ❌ GitHub Personal Access Tokens
- ❌ Discord webhooks
- ❌ Stripe/payment API keys
- ❌ Any service API credentials

#### 2. **Remove ALL Personal Information**
- ❌ Email addresses (replace with placeholder)
- ❌ Phone numbers
- ❌ Home addresses
- ❌ Full names (use placeholder)
- ❌ Personal photos/images with metadata
- ❌ SSH keys
- ❌ SSL certificates
- ❌ Local file paths with username

#### 3. **Remove Sensitive Data Files**
- ❌ `config.json` with real credentials
- ❌ `.env` files (commit `.env.example` instead)
- ❌ `auth.json` or authentication files
- ❌ Database backups (.sql, .db files)
- ❌ Log files with sensitive info
- ❌ User data or customer information

---

## ✅ Security Checklist

Use this checklist for EVERY project before GitHub upload:

### Step 1: Search for API Keys
```bash
# Search for common API key patterns
grep -r "sk-" . --exclude-dir={node_modules,.git,venv,.venv}
grep -r "API_KEY" . --exclude-dir={node_modules,.git,venv,.venv}
grep -r "SECRET" . --exclude-dir={node_modules,.git,venv,.venv}
grep -r "TOKEN" . --exclude-dir={node_modules,.git,venv,.venv}
grep -r "password" . --exclude-dir={node_modules,.git,venv,.venv}
```

### Step 2: Check for Email Addresses
```bash
# Search for email addresses
grep -r "@gmail.com\|@yahoo.com\|@outlook.com" . --exclude-dir={node_modules,.git,venv,.venv}
```

### Step 3: Review Configuration Files
```bash
# List all config files
find . -name "config.json" -o -name ".env" -o -name "auth.json" -o -name "credentials.json"
```

### Step 4: Check Git History
```bash
# See what's staged
git status

# Review all changes
git diff --cached

# Check file sizes (large files might be data)
git ls-files | xargs ls -lh | sort -k5 -hr | head -20
```

---

## 📝 Required Files for Every Project

### 1. `.gitignore` (MANDATORY)
```gitignore
# Secrets and credentials
.env
.env.*
!.env.example
config.json
auth.json
credentials.json
secrets.json
*.pem
*.key
*.p12

# API keys
*apikey*
*api_key*
*api-key*

# Personal data
*.db
*.sqlite
*.sqlite3
user_data/
backups/

# Logs
*.log
logs/

# System
.DS_Store
__pycache__/
*.pyc
node_modules/
venv/
.venv/
```

### 2. `.env.example` (REQUIRED)
```bash
# Copy your .env but replace with placeholders
API_KEY=your_api_key_here
EMAIL=your_email@example.com
PASSWORD=your_password_here
```

### 3. `README.md` (REQUIRED)
- Setup instructions
- How to configure secrets
- Link to your GitHub profile

### 4. `LICENSE` (REQUIRED)
- MIT License (default)
- Or appropriate license for your project

---

## 🔧 Sanitizing Your Code

### Replace Email Addresses
```bash
# Find and replace in all files
find . -type f -name "*.py" -o -name "*.js" -o -name "*.md" | xargs sed -i '' 's/danielalanbates@gmail.com/your-email@example.com/g'
```

### Replace API Keys
```python
# Before (BAD):
api_key = "sk-abc123xyz789"

# After (GOOD):
api_key = os.getenv("OPENAI_API_KEY")
```

### Replace Personal Paths
```python
# Before (BAD):
path = "/Users/daniel/Documents/project"

# After (GOOD):
path = os.path.expanduser("~/Documents/project")
# Or even better:
path = os.path.join(os.getcwd(), "data")
```

---

## 🌐 GitHub Publishing Standards

### All Projects Should:

1. **Use Your GitHub Account**
   - Repository owner: `danielalanbates`
   - Update all URLs to: `https://github.com/danielalanbates/PROJECT-NAME`

2. **Have Professional README**
   ```markdown
   # Project Name

   [![Build Status](badge)]
   [![License: MIT](badge)]

   Description of your project

   ## Installation
   ...

   ## Configuration
   Create `.env` file:
   ```
   API_KEY=your_key
   ```

   ## Usage
   ...

   ## License
   MIT - See LICENSE file
   ```

3. **Include Contact Info**
   - Email: `danielalanbates@gmail.com` (or placeholder)
   - GitHub: `https://github.com/danielalanbates`

4. **Add Badges** (if applicable)
   - Build status
   - License
   - Python/Node version
   - Last commit

---

## 🚀 Publishing Workflow

### Safe Publishing Process:

1. **Clone Project to Safe Location**
   ```bash
   # Work in a clean copy
   cp -r MyProject MyProject-github
   cd MyProject-github
   ```

2. **Run Security Scan**
   ```bash
   # Use our security checker
   python3 /path/to/security_scanner.py .
   ```

3. **Initialize Git**
   ```bash
   git init
   git add .gitignore .env.example
   ```

4. **Review Every File**
   ```bash
   # Check each file manually
   git add -p  # Interactive staging
   ```

5. **Commit and Push**
   ```bash
   git commit -m "Initial commit"
   gh repo create project-name --public --source=. --push
   ```

---

## 🛡️ If You Accidentally Committed Secrets

### Immediate Actions:

1. **Rotate ALL Exposed Credentials**
   - Generate new API keys
   - Change passwords
   - Revoke tokens

2. **Remove from Git History**
   ```bash
   # Install BFG Repo Cleaner
   brew install bfg

   # Remove sensitive file from history
   bfg --delete-files config.json

   # Or remove text patterns
   bfg --replace-text passwords.txt

   # Force push (WARNING: destructive)
   git reflog expire --expire=now --all
   git gc --prune=now --aggressive
   git push --force
   ```

3. **Report to GitHub**
   - GitHub will scan and notify if secrets found
   - Follow their instructions

---

## 📋 Pre-Upload Checklist

Copy this for every project:

- [ ] Searched for API keys (`grep -r "sk-"`)
- [ ] Searched for passwords (`grep -r "password"`)
- [ ] Searched for email addresses
- [ ] Removed `config.json` (added to .gitignore)
- [ ] Created `.env.example` (without real values)
- [ ] Created/updated `.gitignore`
- [ ] Reviewed all commits (`git log --oneline`)
- [ ] Checked diff before pushing (`git diff origin/main`)
- [ ] Updated README with GitHub URLs
- [ ] Added LICENSE file
- [ ] Replaced personal paths
- [ ] Removed logs and debug files
- [ ] No hardcoded credentials in code
- [ ] All secrets use environment variables
- [ ] Tested `.env.example` setup instructions

---

## 🔍 Automated Security Scanner

Create `security_scanner.py` in parent directory:

```python
#!/usr/bin/env python3
"""
Security scanner for detecting secrets before GitHub upload
"""
import os
import re
from pathlib import Path

PATTERNS = {
    'API Key': r'(sk-[a-zA-Z0-9]{32,}|api[_-]?key["\s:=]+[a-zA-Z0-9]{20,})',
    'Password': r'password["\s:=]+[^"\s]{8,}',
    'Email': r'[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|outlook|hotmail)\.com',
    'AWS Key': r'AKIA[0-9A-Z]{16}',
    'GitHub Token': r'ghp_[a-zA-Z0-9]{36}',
    'OpenAI Key': r'sk-[a-zA-Z0-9]{48}',
    'JWT': r'eyJ[a-zA-Z0-9-_]+\.eyJ[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+',
}

EXCLUDE_DIRS = {'.git', 'node_modules', 'venv', '.venv', '__pycache__', 'dist', 'build'}
EXCLUDE_FILES = {'.gitignore', 'security_scanner.py', 'GITHUB_SECURITY_CHECKLIST.md'}

def scan_file(filepath):
    """Scan a file for potential secrets"""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for name, pattern in PATTERNS.items():
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    issues.append({
                        'type': name,
                        'file': filepath,
                        'line': line_num,
                        'match': match.group()[:50]
                    })
    except Exception as e:
        pass
    return issues

def scan_directory(path):
    """Scan all files in directory"""
    all_issues = []
    for root, dirs, files in os.walk(path):
        # Exclude certain directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for filename in files:
            if filename in EXCLUDE_FILES:
                continue

            filepath = os.path.join(root, filename)
            issues = scan_file(filepath)
            all_issues.extend(issues)

    return all_issues

if __name__ == '__main__':
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    print(f"🔍 Scanning {path} for secrets...")
    issues = scan_directory(path)

    if issues:
        print(f"\n⚠️  Found {len(issues)} potential secrets:\n")
        for issue in issues:
            print(f"  {issue['type']}: {issue['file']}:{issue['line']}")
            print(f"    → {issue['match']}")
        print("\n❌ DO NOT commit until these are resolved!")
        sys.exit(1)
    else:
        print("✅ No obvious secrets found. Review manually before committing!")
        sys.exit(0)
```

---

## 📚 Resources

- **GitHub Secrets Scanning**: https://docs.github.com/en/code-security/secret-scanning
- **Git History Cleaner**: https://rtyley.github.io/bfg-repo-cleaner/
- **Environment Variables Best Practices**: https://12factor.net/config

---

## ⚡ Quick Command Reference

```bash
# Scan for secrets before commit
python3 security_scanner.py .

# Search for API keys
grep -r "sk-\|api_key\|API_KEY" . --exclude-dir={node_modules,.git,venv}

# Check what's being committed
git diff --cached

# Remove file from Git (keep local copy)
git rm --cached config.json

# Remove file from Git history
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/secret.json' \
  --prune-empty --tag-name-filter cat -- --all
```

---

## ✅ Safe to Commit:

- ✅ Source code (without secrets)
- ✅ Documentation (`.md` files)
- ✅ Example configurations (`.env.example`)
- ✅ Tests (without real credentials)
- ✅ Scripts (with placeholders)
- ✅ Public assets (icons, images)
- ✅ Dependencies lists (`requirements.txt`, `package.json`)

## ❌ NEVER Commit:

- ❌ `.env` files with real values
- ❌ `config.json` with API keys
- ❌ Database files (`.db`, `.sqlite`)
- ❌ Log files
- ❌ Private keys (`.pem`, `.key`)
- ❌ User data
- ❌ Backup files
- ❌ Screenshots with personal info

---

**Created**: October 2025
**Maintained by**: Daniel Alan Bates
**GitHub**: https://github.com/danielalanbates

**⚠️ Security is not optional. Check EVERY file before pushing!**
