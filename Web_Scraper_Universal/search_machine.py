#!/usr/bin/env python3
"""
Search Machine - File search utility with interactive interface
Searches for files in the file system with visual feedback
"""

import os
import time
import itertools
from typing import Optional


class FileSearcher:
    """Interactive file search utility"""

    def __init__(self, default_directory: Optional[str] = None):
        """
        Initialize file searcher

        Args:
            default_directory: Default directory to search (uses home if None)
        """
        self.home_directory = os.path.expanduser("~")
        self.default_directory = default_directory or self.home_directory

    def search_file(self, filename: str, directory: str) -> Optional[str]:
        """
        Search for a file in the specified directory

        Args:
            filename: Name of the file to search for
            directory: Directory to search in

        Returns:
            Path to the file if found, None otherwise
        """
        print(f"\nSearching for '{filename}' in {directory}...")

        found_path = None
        spinner = itertools.cycle(['-', '/', '|', '\\'])

        try:
            # Walk through directory tree
            for dirpath, dirnames, filenames in os.walk(directory):
                # Show spinner while searching
                print(f" Scanning: {next(spinner)}", end="\r")

                if filename in filenames:
                    found_path = os.path.join(dirpath, filename)
                    print(" " * 50, end="\r")  # Clear spinner line
                    break

        except PermissionError as e:
            print(f"\n⚠️  Permission denied accessing some directories")
        except Exception as e:
            print(f"\n❌ Error during search: {e}")

        return found_path

    def run_interactive(self):
        """Run interactive search session"""
        print("=== File Search Machine ===")
        print("Type 'exit' or 'quit' to stop searching\n")

        while True:
            # Get filename to search
            file_to_find = input("Enter the name of the file you're looking for: ").strip()

            if file_to_find.lower() in ['exit', 'quit', '']:
                print("Exiting the program.")
                break

            # Get search directory
            search_directory = input(
                f"Enter the directory to search in (or press Enter for {self.default_directory}): "
            ).strip()

            if search_directory == "":
                search_directory = self.default_directory

            # Validate directory
            if not os.path.exists(search_directory):
                print(f"❌ Directory not found: {search_directory}")
                print("-" * 40)
                continue

            if not os.path.isdir(search_directory):
                print(f"❌ Not a directory: {search_directory}")
                print("-" * 40)
                continue

            # Search for file
            found_path = self.search_file(file_to_find, search_directory)

            # Display results
            if found_path:
                print(f"✅ Success! File found at: {found_path}")
            else:
                print(f"❌ Sorry, the file '{file_to_find}' was not found.")

            print("-" * 40)


def main():
    """Main entry point"""
    searcher = FileSearcher()
    searcher.run_interactive()


if __name__ == "__main__":
    main()
