#!/usr/bin/env python3
"""
HTML Scraper - Simple HTML content extraction tool
Fetches and parses HTML content from web pages
"""

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from typing import Optional
import sys


class HTMLScraper:
    """Simple HTML scraper with error handling"""

    def __init__(self, url: str, timeout: int = 10):
        """
        Initialize HTML scraper

        Args:
            url: URL to scrape
            timeout: Request timeout in seconds (default: 10)
        """
        self.url = url
        self.timeout = timeout
        self.html_content: Optional[str] = None

    def fetch(self) -> bool:
        """
        Fetch HTML content from the URL

        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"Fetching: {self.url}")
            with urlopen(self.url, timeout=self.timeout) as page:
                html_bytes = page.read()
                self.html_content = html_bytes.decode("utf-8")
                print(f"✅ Successfully fetched {len(self.html_content)} characters")
                return True

        except HTTPError as e:
            print(f"❌ HTTP Error {e.code}: {e.reason}")
            return False

        except URLError as e:
            print(f"❌ URL Error: {e.reason}")
            return False

        except UnicodeDecodeError:
            print("❌ Failed to decode HTML content (invalid UTF-8)")
            return False

        except TimeoutError:
            print(f"❌ Request timeout after {self.timeout} seconds")
            return False

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False

    def get_content(self) -> Optional[str]:
        """
        Get the fetched HTML content

        Returns:
            HTML content as string, or None if not fetched
        """
        return self.html_content

    def print_content(self, max_lines: int = 50):
        """
        Print HTML content to console

        Args:
            max_lines: Maximum number of lines to print (default: 50)
        """
        if not self.html_content:
            print("⚠️  No content to display. Run fetch() first.")
            return

        lines = self.html_content.split('\n')
        total_lines = len(lines)

        for i, line in enumerate(lines[:max_lines], 1):
            print(f"{i:4d}: {line}")

        if total_lines > max_lines:
            print(f"\n... ({total_lines - max_lines} more lines)")

    def save_to_file(self, filename: str) -> bool:
        """
        Save HTML content to a file

        Args:
            filename: Path to output file

        Returns:
            True if successful, False otherwise
        """
        if not self.html_content:
            print("⚠️  No content to save. Run fetch() first.")
            return False

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.html_content)
            print(f"✅ Saved HTML to: {filename}")
            return True

        except Exception as e:
            print(f"❌ Failed to save file: {e}")
            return False


def main():
    """Main entry point for standalone usage"""
    # Default URL (example)
    default_url = "http://olympus.realpython.org/profiles/aphrodite"

    # Get URL from command line or use default
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = default_url
        print(f"Using default URL: {url}")
        print("Usage: python3 'HTML Scraper.py' <url>\n")

    # Create scraper and fetch content
    scraper = HTMLScraper(url)

    if scraper.fetch():
        # Print first 50 lines
        print("\n=== HTML Content (first 50 lines) ===")
        scraper.print_content(max_lines=50)

        # Optionally save to file
        save_prompt = input("\nSave to file? (y/n): ").strip().lower()
        if save_prompt == 'y':
            filename = input("Enter filename (default: output.html): ").strip()
            if not filename:
                filename = "output.html"
            scraper.save_to_file(filename)
    else:
        print("\n❌ Failed to fetch HTML content")
        sys.exit(1)


if __name__ == "__main__":
    main()
