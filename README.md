# Web Scraping Toolkit

Universal web scraper with price monitoring capabilities. Extract data from any website with intelligent selectors.

## Features

- **Universal Scraping**: Works with most websites
- **Intelligent Selectors**: Auto-detect data patterns
- **Price Monitoring**: Track price changes over time
- **Multi-format Export**: JSON, CSV, Excel support
- **Scheduled Scraping**: Automatic periodic scraping
- **Anti-detection**: Stealth mode to avoid bot detection

## Use Cases

- Price monitoring for e-commerce
- Product catalog extraction
- News article scraping
- Data aggregation
- Market research
- Competitive analysis

## Installation

### Prerequisites
- Python 3.8+
- Chrome/Chromium browser

### Setup
```bash
# Clone repository
git clone <repository-url>
cd 16-Web_Scraping

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings
```

### Dependencies
```
beautifulsoup4>=4.12.0
selenium>=4.15.0
requests>=2.31.0
pandas>=2.1.0
lxml>=4.9.0
schedule>=1.2.0
```

## Usage

### Basic Scraping

```python
from scraper import WebScraper

# Initialize scraper
scraper = WebScraper()

# Scrape a single page
data = scraper.scrape_url('https://example.com/product')

# Save to CSV
scraper.save_to_csv(data, 'output.csv')
```

### Price Monitoring

```python
from price_monitor import PriceMonitor

# Initialize monitor
monitor = PriceMonitor()

# Add product to track
monitor.add_product(
    url='https://example.com/product',
    name='Product Name',
    target_price=99.99
)

# Check prices
monitor.check_all_prices()

# Get price history
history = monitor.get_price_history('product-id')
```

### Scheduled Scraping

```python
from scheduler import ScrapingScheduler

# Create scheduler
scheduler = ScrapingScheduler()

# Schedule daily scraping
scheduler.schedule_daily(
    url='https://example.com',
    time='09:00',
    output='data.json'
)

# Start scheduler
scheduler.start()
```

## Project Structure

```
16-Web_Scraping/
├── scraper.py           # Main scraping engine
├── price_monitor.py     # Price tracking functionality
├── scheduler.py         # Scheduled scraping
├── selectors.py         # Selector utilities
├── exporters.py         # Data export functions
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
└── data/               # Scraped data storage
```

## Configuration

Edit `.env` file:

```env
# Browser settings
HEADLESS=true
BROWSER=chrome

# Anti-detection
USER_AGENT=Mozilla/5.0...
USE_STEALTH=true

# Rate limiting
REQUEST_DELAY=2
MAX_RETRIES=3

# Export settings
DEFAULT_FORMAT=json
```

## Features

### Smart Selectors
- Automatic CSS selector generation
- XPath support
- Regex pattern matching
- Dynamic content handling

### Anti-Detection
- Randomized user agents
- Request throttling
- Cookie management
- JavaScript rendering

### Data Export
- JSON
- CSV
- Excel (.xlsx)
- SQLite database
- Custom formats

## Legal Notice

⚠️ **Important**: Web scraping must comply with:
- Website Terms of Service
- robots.txt directives
- Copyright laws
- Data protection regulations (GDPR, CCPA)

**Only scrape websites where you have permission or legal right to do so.**

## Best Practices

1. **Respect robots.txt**: Check and honor website scraping policies
2. **Rate Limiting**: Don't overload servers with requests
3. **User Agent**: Identify your scraper appropriately
4. **Caching**: Store data locally to reduce requests
5. **Error Handling**: Handle failures gracefully

## Troubleshooting

### Scraper Blocked
- Increase `REQUEST_DELAY`
- Enable stealth mode
- Use rotating proxies
- Check robots.txt compliance

### Missing Data
- Verify selectors are correct
- Enable JavaScript rendering
- Check for dynamic content
- Inspect page source

### Performance Issues
- Reduce concurrent requests
- Implement caching
- Use headless browser
- Optimize selectors

## Examples

See `examples/` directory for:
- E-commerce price scraping
- News article extraction
- Product catalog scraping
- Real estate listings

## Support

For questions or issues:
- Email: daniel@batesai.org
- Website: https://batesai.org

## License

See [LICENSE](../LICENSE) file for details.

---

**Status**: Beta
**Last Updated**: January 2025
**Version**: 1.0.0

## License & Commercial Use

- **Personal projects:** Free to download, study, and modify for your own hobby, research, or learning needs.
- **Attribution required:** Include “Built with BatesAI software by Daniel Bates (https://batesai.org)” anywhere you showcase or distribute this work.
- **Organizations & monetization:** Any company, client, school, nonprofit, or government project must either buy a commercial license (daniel@batesai.org) or share 10% of gross revenue from every sale that includes this software.
- **Compliance:** Missing attribution, skipping payments, or sublicensing under new terms immediately sunsets your access until the issue is fixed.

Read the full “BatesAI Personal & Revenue Share License v1.0” in LICENSE.

