# Web Scraper Universal

A collection of professional web scraping utilities and tools for automated data extraction and processing.

## 📋 Overview

Web Scraper Universal is a modular Python toolkit providing various web scraping utilities, from simple HTML extraction to advanced automated reporting systems. Perfect for data collection, price monitoring, content aggregation, and automation workflows.

## ✨ Features

- **Simple HTML Scraping**: Basic web content extraction with error handling
- **Search Machine**: Interactive file system search utility
- **Report Generator**: Automated report generation for fitness, productivity, and finance
- **CSV Handling**: Import and process CSV data
- **Demo Scraper**: Working examples for quick-start learning
- **Test Integration**: GitHub Copilot LLM integration testing

## 📦 Installation

### Requirements

- Python 3.8+ (tested with Python 3.13.3)
- pip package manager

### Setup

```bash
# Clone or navigate to the project directory
cd Web_Scraper_Universal

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

```
requests>=2.32.5          # HTTP library for API calls
beautifulsoup4>=4.14.2    # HTML/XML parsing
lxml>=6.0.2               # Fast XML/HTML parser
selenium>=4.36.0          # Browser automation (optional)
pandas>=2.3.3             # Data manipulation
openpyxl>=3.1.5           # Excel file handling
matplotlib>=3.9.0         # Data visualization
numpy>=2.1.0              # Numerical computing
click>=8.1.7              # CLI framework
colorama>=0.4.6           # Terminal colors
python-dotenv>=1.0.1      # Environment variables
schedule>=1.2.2           # Task scheduling
rumps>=0.4.0              # macOS menu bar apps (macOS only)
```

## 🚀 Quick Start

### 1. HTML Scraper

Simple web content extraction:

```bash
python3 "HTML Scraper.py" https://example.com
```

Or use it programmatically:

```python
from HTML\ Scraper import HTMLScraper

scraper = HTMLScraper("https://example.com")
if scraper.fetch():
    content = scraper.get_content()
    scraper.save_to_file("output.html")
```

### 2. Search Machine

Interactive file search:

```bash
python3 search_machine.py
```

Or use programmatically:

```python
from search_machine import FileSearcher

searcher = FileSearcher()
result = searcher.search_file("document.pdf", "/Users/daniel/Documents")
if result:
    print(f"Found: {result}")
```

### 3. Report Generator

Generate comprehensive reports:

```bash
python3 report_generator.py
```

Or use programmatically:

```python
from report_generator import ReportGenerator

generator = ReportGenerator()

# Generate fitness report
fitness_report = generator.generate_fitness_progress_report()
generator.save_report(fitness_report, "fitness_report.json")

# Generate comprehensive report
comprehensive = generator.generate_comprehensive_report()
generator.save_report(comprehensive)
```

### 4. Web Scraper Demo

Test scraping functionality:

```bash
python3 web_scraper_demo.py
```

## 📁 Project Structure

```
Web_Scraper_Universal/
├── HTML Scraper.py              # Simple HTML content scraper
├── search_machine.py            # File system search utility
├── report_generator.py          # Automated report generation
├── web_scraper_demo.py          # Working demo scraper
├── scraper_quick_test.py        # Quick functionality test
├── csv_importer.py              # CSV data import utility
├── test_copilot_integration.py  # LLM integration tests
├── Python_documenting.py        # Documentation utility
├── Readfile.py & Readfile_test.py  # File reading utilities
├── requirements.txt             # Python dependencies
├── scraped_data/                # Output directory for scraped data
├── create_cute_icon.py          # Icon generation utilities
├── create_cute_robot_icns.py
├── create_icon.py
├── create_proper_icon.py
└── README.md                    # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file for configuration:

```env
# API Keys (if needed)
GITHUB_TOKEN=your_github_token_here

# Scraping Settings
USER_AGENT=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
REQUEST_TIMEOUT=30

# Report Settings
REPORTS_DIR=/path/to/reports
CHARTS_DIR=/path/to/charts
```

### Custom Report Directory

```python
from report_generator import ReportGenerator

# Use custom directory
generator = ReportGenerator(base_dir="/custom/path")
```

## 📊 Report Types

### Fitness Progress Report
- Workout frequency and consistency
- Body composition trends
- Goal progress tracking
- Exercise recommendations

### Productivity Report
- Goal completion rates
- Task management metrics
- Time estimation accuracy
- Productivity recommendations

### Financial Overview
- Income and expense tracking
- Savings rate calculation
- Investment metrics
- Financial health score

### Comprehensive Report
- Combined insights across all areas
- Key achievements summary
- Next period priorities
- Overall progress tracking

## 🧪 Testing

Run quick tests:

```bash
# Test basic scraping
python3 scraper_quick_test.py

# Test Copilot integration
python3 test_copilot_integration.py

# Test file reading
python3 Readfile_test.py
```

## 🐛 Troubleshooting

### Common Issues

**1. ModuleNotFoundError**
```bash
# Install missing dependencies
pip install -r requirements.txt
```

**2. Permission Errors (macOS)**
```bash
# Grant Terminal full disk access
System Settings > Privacy & Security > Full Disk Access
```

**3. Selenium WebDriver Issues**
```bash
# Install/update webdriver-manager
pip install --upgrade webdriver-manager
```

**4. Report Generation Fails**
```bash
# Check matplotlib backend
export MPLBACKEND=Agg
python3 report_generator.py
```

## 📝 Usage Examples

### Example 1: Scrape and Save HTML

```python
from HTML\ Scraper import HTMLScraper

urls = [
    "https://example.com/page1",
    "https://example.com/page2"
]

for i, url in enumerate(urls):
    scraper = HTMLScraper(url)
    if scraper.fetch():
        scraper.save_to_file(f"page_{i+1}.html")
```

### Example 2: Generate Weekly Reports

```python
from report_generator import ReportGenerator
import schedule
import time

def weekly_report():
    generator = ReportGenerator()
    report = generator.generate_comprehensive_report()
    generator.save_report(report, "weekly_report.json")
    print("Weekly report generated!")

# Schedule weekly reports
schedule.every().monday.at("09:00").do(weekly_report)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Example 3: Search Multiple Directories

```python
from search_machine import FileSearcher

searcher = FileSearcher()
directories = ["/Users/daniel/Documents", "/Users/daniel/Downloads"]

for directory in directories:
    result = searcher.search_file("invoice.pdf", directory)
    if result:
        print(f"Found in: {result}")
        break
```

## 🔒 Security Notes

- Never commit `.env` files containing API keys
- Use environment variables for sensitive configuration
- Sanitize user input when scraping user-provided URLs
- Respect robots.txt and website terms of service
- Implement rate limiting for production scraping

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📮 Support

For issues, questions, or suggestions:
- Create an issue in the repository
- Email: [your-email@example.com]

## 🔮 Future Enhancements

- [ ] Add database storage for scraped data
- [ ] Implement caching mechanism
- [ ] Add proxy rotation support
- [ ] Create web UI for report viewing
- [ ] Add email report delivery
- [ ] Implement API endpoints
- [ ] Add support for authenticated scraping
- [ ] Create Docker containerization

## 📚 Related Projects

- **Price Monitor Scraper** - Specialized price tracking tool
- **Copilot Master** - Integration with automation suite

---

**Version**: 1.0.0
**Last Updated**: October 2025
**Python**: 3.8+
**Platform**: macOS, Linux, Windows
