#!/usr/bin/env python3
"""
Security scanner for detecting secrets before GitHub upload
Run this on any project before committing to GitHub!

Usage:
    python3 security_scanner.py /path/to/project
    python3 security_scanner.py .  # Current directory
"""
import os
import re
import sys
from pathlib import Path
from typing import List, Dict

# Patterns to detect sensitive information
PATTERNS = {
    'OpenAI API Key': r'sk-[a-zA-Z0-9]{48}',
    'Anthropic API Key': r'sk-ant-[a-zA-Z0-9-]{95,}',
    'Generic API Key': r'api[_-]?key["\s:=]+["\']?[a-zA-Z0-9]{20,}["\']?',
    'Password': r'password["\s:=]+["\']?[^"\s\n]{8,}["\']?',
    'Email Address': r'[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|outlook|hotmail|icloud)\.com',
    'AWS Access Key': r'AKIA[0-9A-Z]{16}',
    'GitHub Token': r'ghp_[a-zA-Z0-9]{36}',
    'GitHub OAuth': r'gho_[a-zA-Z0-9]{36}',
    'Slack Token': r'xox[baprs]-[a-zA-Z0-9-]+',
    'JWT Token': r'eyJ[a-zA-Z0-9-_]+\.eyJ[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+',
    'Private Key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'Discord Webhook': r'https://discord\.com/api/webhooks/[0-9]+/[a-zA-Z0-9_-]+',
    'Stripe Key': r'sk_(?:live|test)_[a-zA-Z0-9]{24,}',
    'Twilio Auth': r'SK[a-z0-9]{32}',
    'Database URL': r'(?:mysql|postgres|mongodb)://[^"\s]+',
    'SMTP Password': r'smtp[_-]?(?:pass|password)["\s:=]+["\']?[^"\s\n]{8,}["\']?',
}

# Directories to exclude from scanning
EXCLUDE_DIRS = {
    '.git', 'node_modules', 'venv', '.venv', '__pycache__',
    'dist', 'build', 'egg-info', '.eggs', 'htmlcov',
    '.pytest_cache', '.mypy_cache', '.tox', 'logs'
}

# Files to exclude from scanning
EXCLUDE_FILES = {
    '.gitignore',
    'security_scanner.py',
    'GITHUB_SECURITY_CHECKLIST.md',
    '.DS_Store',
    'package-lock.json',
    'yarn.lock',
    'Pipfile.lock'
}

# File extensions to exclude
EXCLUDE_EXTENSIONS = {
    '.pyc', '.pyo', '.so', '.dylib', '.dll', '.exe',
    '.jpg', '.jpeg', '.png', '.gif', '.ico', '.svg',
    '.mp4', '.mov', '.avi', '.mp3', '.wav',
    '.pdf', '.zip', '.tar', '.gz', '.dmg',
    '.db', '.sqlite', '.sqlite3'
}


def scan_file(filepath: str) -> List[Dict]:
    """Scan a file for potential secrets"""
    issues = []

    # Skip binary files and certain extensions
    if any(filepath.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
        return issues

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

            # Skip if file is too large (>1MB)
            if len(content) > 1_000_000:
                return issues

            for name, pattern in PATTERNS.items():
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    # Get line number
                    line_num = content[:match.start()].count('\n') + 1

                    # Get the line content
                    lines = content.split('\n')
                    line_content = lines[line_num - 1] if line_num <= len(lines) else ''

                    # Skip if it's a comment explaining the pattern
                    if line_content.strip().startswith(('#', '//', '/*', '*', '<!--')):
                        if 'example' in line_content.lower() or 'placeholder' in line_content.lower():
                            continue

                    # Skip .env.example files
                    if '.example' in filepath or 'example.' in filepath:
                        continue

                    issues.append({
                        'type': name,
                        'file': filepath,
                        'line': line_num,
                        'match': match.group()[:50] + '...' if len(match.group()) > 50 else match.group(),
                        'context': line_content.strip()[:100]
                    })
    except Exception as e:
        # Silently skip files that can't be read
        pass

    return issues


def scan_directory(path: str) -> List[Dict]:
    """Scan all files in directory recursively"""
    all_issues = []
    scanned_files = 0

    for root, dirs, files in os.walk(path):
        # Exclude certain directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for filename in files:
            if filename in EXCLUDE_FILES:
                continue

            filepath = os.path.join(root, filename)
            scanned_files += 1
            issues = scan_file(filepath)
            all_issues.extend(issues)

    return all_issues, scanned_files


def print_report(issues: List[Dict], scanned_files: int):
    """Print a formatted report of found issues"""
    if not issues:
        print("\n" + "="*70)
        print("✅ SUCCESS: No obvious secrets found!")
        print("="*70)
        print(f"\nScanned {scanned_files} files.")
        print("\n⚠️  Manual review is still recommended:")
        print("  - Check config files manually")
        print("  - Review all .env files")
        print("  - Verify no personal data included")
        print("  - Use: git diff --cached")
        return True

    print("\n" + "="*70)
    print(f"⚠️  SECURITY WARNING: Found {len(issues)} potential secrets!")
    print("="*70)

    # Group by type
    by_type = {}
    for issue in issues:
        issue_type = issue['type']
        if issue_type not in by_type:
            by_type[issue_type] = []
        by_type[issue_type].append(issue)

    # Print grouped results
    for issue_type, type_issues in by_type.items():
        print(f"\n📛 {issue_type} ({len(type_issues)} found):")
        for issue in type_issues:
            print(f"   📁 {issue['file']}:{issue['line']}")
            print(f"      → {issue['match']}")
            if issue['context']:
                print(f"      Context: {issue['context']}")

    print("\n" + "="*70)
    print("❌ DO NOT COMMIT UNTIL THESE ARE RESOLVED!")
    print("="*70)
    print("\nRecommended actions:")
    print("  1. Move secrets to .env files")
    print("  2. Add .env to .gitignore")
    print("  3. Create .env.example with placeholders")
    print("  4. Use os.getenv() or environment variables")
    print("  5. Re-run this scanner after fixing")

    return False


def check_gitignore(path: str):
    """Check if .gitignore exists and has essential entries"""
    gitignore_path = os.path.join(path, '.gitignore')

    if not os.path.exists(gitignore_path):
        print("\n⚠️  WARNING: No .gitignore file found!")
        print("   Create one with at minimum:")
        print("     .env")
        print("     config.json")
        print("     *.log")
        print("     __pycache__/")
        print("     node_modules/")
        return False

    with open(gitignore_path, 'r') as f:
        content = f.read()

    required = ['.env', 'config.json', '*.log']
    missing = [req for req in required if req not in content]

    if missing:
        print(f"\n⚠️  .gitignore missing: {', '.join(missing)}")
        return False

    return True


def check_env_example(path: str):
    """Check if .env.example exists"""
    if os.path.exists(os.path.join(path, '.env')):
        if not os.path.exists(os.path.join(path, '.env.example')):
            print("\n⚠️  Found .env but no .env.example!")
            print("   Create .env.example with placeholders")
            return False
    return True


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '.'

    path = os.path.abspath(path)

    if not os.path.exists(path):
        print(f"❌ Error: Path '{path}' does not exist")
        sys.exit(1)

    print("="*70)
    print("🔍 SECURITY SCANNER FOR GITHUB")
    print("="*70)
    print(f"\nScanning: {path}")
    print("Looking for: API keys, passwords, emails, tokens, etc.\n")

    # Run checks
    gitignore_ok = check_gitignore(path)
    env_ok = check_env_example(path)

    # Scan files
    print("Scanning files...")
    issues, scanned_files = scan_directory(path)

    # Print report
    success = print_report(issues, scanned_files)

    # Exit with appropriate code
    if success and gitignore_ok and env_ok:
        print("\n✅ Ready for GitHub (but always review manually!)")
        sys.exit(0)
    else:
        print("\n❌ Fix issues before committing to GitHub!")
        sys.exit(1)


if __name__ == '__main__':
    main()
