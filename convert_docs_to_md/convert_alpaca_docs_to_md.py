#!/usr/bin/env python
"""
Convert Alpaca API HTML documentation to Markdown format.
This script processes the downloaded Alpaca documentation and generates a clean, organized
markdown documentation structure that GitHub Copilot can easily access and use.
"""

import os
import re
import html2text
from bs4 import BeautifulSoup, Comment
import shutil
import json
from pathlib import Path
import sys
from urllib.parse import unquote

# Config
SOURCE_DIR = "d:/Coding Files/GitHub/AlgoAlp/docs.alpaca.markets"
TARGET_DIR = "d:/Coding Files/GitHub/AlgoAlp/docs/alpaca-api"
DOCS_DIR = os.path.join(TARGET_DIR, "docs")
API_DIR = os.path.join(TARGET_DIR, "api")
REFERENCE_DIR = os.path.join(TARGET_DIR, "reference")
CHANGELOG_DIR = os.path.join(TARGET_DIR, "changelog")

# Create directories if they don't exist
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(API_DIR, exist_ok=True)
os.makedirs(REFERENCE_DIR, exist_ok=True)
os.makedirs(CHANGELOG_DIR, exist_ok=True)

# Initialize html2text
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False
h.escape_snob = False
h.ignore_emphasis = False
h.body_width = 0  # No wrapping

def clean_filename(filename):
    """Clean filename for better readability and organization."""
    # Remove encoded characters like %2F
    filename = unquote(filename)
    
    # Replace special characters with hyphens
    filename = re.sub(r'[^\w\-.]', '-', filename)
    
    # Remove multiple consecutive hyphens
    filename = re.sub(r'-+', '-', filename)
    
    # Remove leading/trailing hyphens
    filename = filename.strip('-')
    
    # Ensure it ends with .md
    if not filename.endswith('.md'):
        if filename.endswith('.html'):
            filename = filename[:-5] + '.md'
        else:
            filename = filename + '.md'
    
    return filename

def extract_main_content(html_content):
    """Extract main content from ReadMe/Alpaca-formatted HTML."""
    try:
        soup = BeautifulSoup(html_content, 'lxml')
        
        # Remove scripts, styles, and comments
        for script in soup(["script", "style"]):
            script.extract()
        
        # Remove comments
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()
        
        # Try to find the main content container
        main_content = None
        
        # Look for common Alpaca/ReadMe content selectors
        selectors = [
            "article.rm-Article",
            ".rm-Article",
            "main.rm-Guides",
            ".content-body",
            ".rm-Markdown",
            "section.content-body",
            ".markdown-body",
            "[data-testid='RDMD']",
            "main",
            "article"
        ]
        
        for selector in selectors:
            main_content = soup.select(selector)
            if main_content:
                main_content = main_content[0]
                break
        
        # If we found a main content container
        if main_content:
            # Remove navigation elements
            for nav in main_content.select("nav, .rm-Sidebar, .hub-sidebar"):
                nav.extract()
                
            # Remove header/footer elements that aren't part of content
            for el in main_content.select("header#content-head, .rm-Header, .Header"):
                el.extract()
                
            # Clean up other non-content elements
            for el in main_content.select(".pagination-nav, .tocCollapsible, .tableOfContents, .suggestEdits"):
                el.extract()
                
            # Remove search elements
            for el in main_content.select(".hub-search-results, .rm-SearchModal, .rm-SearchToggle"):
                el.extract()
            
            # Clean up any buttons and interactive elements that aren't part of documentation
            for el in main_content.select("button[aria-label='Copy Code']"):
                el.extract()
                
            return str(main_content)
        
        # If we couldn't find any main content, try body
        body = soup.find('body')
        if body:
            # Remove known non-content elements from body
            for el in body.select("header, nav, .rm-Header, .rm-Sidebar, footer"):
                el.extract()
            return str(body)
        
        return str(soup)
        
    except Exception as e:
        print(f"Error extracting content: {e}")
        return html_content

def html_to_markdown(html_content, source_path=""):
    """Convert HTML content to Markdown."""
    try:
        cleaned_html = extract_main_content(html_content)
        markdown = h.handle(cleaned_html)
        
        # Clean up the markdown
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Remove excess newlines
        markdown = re.sub(r'^\s+', '', markdown, flags=re.MULTILINE)  # Remove leading whitespace
        
        # Fix relative links
        if source_path:
            base_dir = os.path.dirname(source_path)
            markdown = fix_relative_links(markdown, base_dir)
        
        # Clean up code blocks
        markdown = clean_code_blocks(markdown)
        
        return markdown
    except Exception as e:
        print(f"Error converting to markdown: {e}")
        return f"Error converting content: {str(e)}"

def clean_code_blocks(markdown):
    """Clean up code blocks and improve formatting."""
    # Fix code blocks that may have been mangled
    markdown = re.sub(r'```(\w+)?\s*\n\s*```', '', markdown)  # Remove empty code blocks
    
    # Ensure proper spacing around code blocks
    markdown = re.sub(r'```(\w+)?\n([^`]+)\n```', r'```\1\n\2\n```', markdown)
    
    return markdown

def fix_relative_links(markdown, base_dir):
    """Fix relative links in markdown to point to the correct files."""
    # Pattern for markdown links: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        
        # Skip external links, anchors, and absolute URLs
        if url.startswith(('http', 'mailto', '#', '/', 'data:')):
            return f'[{text}]({url})'
        
        # Convert .html links to .md
        if url.endswith('.html'):
            url = url.replace('.html', '.md')
        
        # Clean up the URL
        url = clean_filename(url)
        
        return f'[{text}]({url})'
    
    return re.sub(link_pattern, replace_link, markdown)

def save_markdown(markdown, output_file):
    """Save markdown content to a file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"Created {output_file}")
        return True
    except Exception as e:
        print(f"Error saving {output_file}: {e}")
        return False

def determine_output_directory(file_path):
    """Determine which output directory to use based on file path."""
    rel_path = os.path.relpath(file_path, SOURCE_DIR)
    
    if rel_path.startswith('docs'):
        return DOCS_DIR
    elif rel_path.startswith('reference'):
        return REFERENCE_DIR
    elif rel_path.startswith('changelog'):
        return CHANGELOG_DIR
    else:
        return API_DIR

def process_html_file(file_path):
    """Process an HTML file and convert it to Markdown."""
    rel_path = os.path.relpath(file_path, SOURCE_DIR)
    print(f"Processing {rel_path}...")
    
    # Skip certain files
    skip_patterns = [
        "404.html", 
        "search.html", 
        "login@redirect_uri=",
        "edit/",
        "cdn-cgi/",
        "robots.txt"
    ]
    
    if any(pattern in file_path for pattern in skip_patterns):
        print(f"Skipping {file_path}")
        return None
    
    # Determine the output directory
    output_dir = determine_output_directory(file_path)
    
    # Clean the filename
    base_name = os.path.basename(file_path)
    clean_name = clean_filename(base_name)
    
    # Create output file path
    output_file = os.path.join(output_dir, clean_name)
    
    try:
        # Read the HTML file
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Convert to markdown
        markdown = html_to_markdown(html_content, file_path)
        
        # Add frontmatter
        title = extract_title_from_html(html_content) or clean_name.replace('.md', '').replace('-', ' ').title()
        markdown_with_frontmatter = f"""---
title: {title}
source: {rel_path}
---

{markdown}"""
        
        # Save the markdown file
        if save_markdown(markdown_with_frontmatter, output_file):
            return output_file
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def extract_title_from_html(html_content):
    """Extract title from HTML content."""
    try:
        soup = BeautifulSoup(html_content, 'lxml')
        
        # Try different title selectors
        title_selectors = [
            'title',
            'h1',
            '.rm-Article h1',
            'header h1',
            '[data-testid="RDMD"] h1'
        ]
        
        for selector in title_selectors:
            title_elem = soup.select_one(selector)
            if title_elem:
                title = title_elem.get_text().strip()
                # Clean up the title
                title = re.sub(r'\s+', ' ', title)
                if title and title != 'Alpaca API Docs':
                    return title
        
        return None
    except:
        return None

def copy_assets():
    """Copy any assets like images to the output directory."""
    # Look for common asset directories
    asset_dirs = ['images', 'assets', 'img', 'static']
    
    for asset_dir in asset_dirs:
        source_asset_dir = os.path.join(SOURCE_DIR, asset_dir)
        if os.path.exists(source_asset_dir):
            target_asset_dir = os.path.join(TARGET_DIR, asset_dir)
            try:
                shutil.copytree(source_asset_dir, target_asset_dir, dirs_exist_ok=True)
                print(f"Copied assets from {source_asset_dir} to {target_asset_dir}")
            except Exception as e:
                print(f"Error copying assets: {e}")

def create_index_files(processed_files):
    """Create index files for each section."""
    
    # Group files by directory
    files_by_dir = {}
    for file_path in processed_files:
        if file_path:
            dir_name = os.path.dirname(file_path)
            if dir_name not in files_by_dir:
                files_by_dir[dir_name] = []
            files_by_dir[dir_name].append(file_path)
    
    # Create index for each directory
    for dir_path, files in files_by_dir.items():
        create_directory_readme(dir_path, files)
    
    # Create main README
    create_main_readme(processed_files)

def create_directory_readme(dir_path, files):
    """Create a README.md file for a directory."""
    dir_name = os.path.basename(dir_path)
    
    if dir_name == 'docs':
        title = "Alpaca API Documentation"
        intro = "This section contains guides and tutorials for using the Alpaca API."
    elif dir_name == 'reference':
        title = "Alpaca API Reference"
        intro = "This section contains detailed API endpoint documentation."
    elif dir_name == 'changelog':
        title = "Alpaca API Changelog"
        intro = "This section contains release notes and changes to the Alpaca API."
    else:
        title = f"Alpaca API {dir_name.title()}"
        intro = f"This section contains {dir_name} related documentation."
    
    readme_content = f"""# {title}

{intro}

## Contents

"""
    
    # Sort files and create links
    sorted_files = sorted(files)
    for file_path in sorted_files:
        if file_path and os.path.exists(file_path):
            filename = os.path.basename(file_path)
            if filename != 'README.md':
                # Create a readable name from filename
                display_name = filename.replace('.md', '').replace('-', ' ').title()
                readme_content += f"- [{display_name}]({filename})\n"
    
    readme_path = os.path.join(dir_path, 'README.md')
    save_markdown(readme_content, readme_path)

def create_main_readme(processed_files):
    """Create the main README.md file."""
    readme_content = """# Alpaca API Documentation

This is a converted version of the official Alpaca API documentation,
organized for easier reference and use with AI coding assistants.

## Contents

- [Documentation](docs/README.md) - Guides and tutorials
- [API Reference](reference/README.md) - Detailed endpoint documentation  
- [Changelog](changelog/README.md) - Release notes and changes

## About Alpaca API

Alpaca API is a commission-free trading platform that provides APIs for:

- **Trading API**: Execute trades for stocks, crypto, and options
- **Market Data API**: Access real-time and historical market data
- **Broker API**: Build trading applications and manage customer accounts
- **Connect API**: OAuth2 integration for third-party applications

## Quick Links

### Trading API
- [Getting Started with Trading API](docs/getting-started-with-trading-api.md)
- [Working with Orders](docs/working-with-orders.md)
- [Working with Positions](docs/working-with-positions.md)
- [Paper Trading](docs/paper-trading.md)

### Market Data API
- [Getting Started with Market Data](docs/getting-started-with-alpaca-market-data.md)
- [Historical Data](docs/historical-api.md)
- [Real-time Data](docs/streaming-market-data.md)

### Broker API
- [Getting Started with Broker API](docs/getting-started-with-broker-api.md)
- [Account Opening](docs/account-opening.md)
- [Funding Accounts](docs/funding-accounts.md)

## Authentication

All Alpaca APIs use API keys for authentication. You can get your API keys from:
- Trading API: [Alpaca Dashboard](https://app.alpaca.markets/)
- Broker API: [Broker Dashboard](https://broker-app.alpaca.markets/)

## SDKs and Tools

Alpaca provides SDKs for multiple programming languages:
- Python
- JavaScript/Node.js
- Go
- C#
- Java

For more information, see [SDKs and Tools](docs/sdks-and-tools.md).
"""
    
    readme_path = os.path.join(TARGET_DIR, 'README.md')
    save_markdown(readme_content, readme_path)

def main():
    """Main function to convert all HTML files."""
    print(f"Converting Alpaca API documentation from {SOURCE_DIR} to {TARGET_DIR}")
    
    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory {SOURCE_DIR} does not exist!")
        return
    
    processed_files = []
    total_files = 0
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith('.html'):
                total_files += 1
                file_path = os.path.join(root, file)
                result = process_html_file(file_path)
                if result:
                    processed_files.append(result)
    
    print(f"\nProcessed {len(processed_files)} out of {total_files} HTML files")
    
    # Copy assets
    copy_assets()
    
    # Create index files
    create_index_files(processed_files)
    
    print(f"\nConversion complete! Documentation saved to {TARGET_DIR}")
    print("\nGenerated files:")
    print(f"- Main README: {TARGET_DIR}/README.md")
    print(f"- Documentation: {DOCS_DIR}/")
    print(f"- API Reference: {REFERENCE_DIR}/")
    print(f"- Changelog: {CHANGELOG_DIR}/")

if __name__ == "__main__":
    main()
