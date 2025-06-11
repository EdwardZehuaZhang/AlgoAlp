#!/usr/bin/env python
"""
Convert Lightweight Charts HTML documentation to Markdown format.
This script processes the downloaded documentation and generates a clean, organized
markdown documentation structure.
"""

import os
import re
import html2text
from bs4 import BeautifulSoup, Comment
import shutil
import json
from pathlib import Path
import sys

# Config
SOURCE_DIR = "d:/Coding Files/GitHub/AlgoAlp/tradingview.github.io/lightweight-charts"
TARGET_DIR = "d:/Coding Files/GitHub/AlgoAlp/docs/lightweight-charts"
API_DIR = os.path.join(TARGET_DIR, "api")
TUTORIALS_DIR = os.path.join(TARGET_DIR, "tutorials")
EXAMPLES_DIR = os.path.join(TARGET_DIR, "examples")

# Create directories if they don't exist
os.makedirs(API_DIR, exist_ok=True)
os.makedirs(TUTORIALS_DIR, exist_ok=True)
os.makedirs(EXAMPLES_DIR, exist_ok=True)

# Initialize html2text
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False
h.escape_snob = False
h.ignore_emphasis = False
h.body_width = 0  # No wrapping

def extract_main_content(html_content):
    """Extract main content from Docusaurus-formatted HTML."""
    try:
        soup = BeautifulSoup(html_content, 'lxml')
        
        # Remove scripts, styles
        for script in soup(["script", "style"]):
            script.extract()
        
        # Try to find the main content container
        main_content = None
        
        # Look for common Docusaurus content selectors
        selectors = [
            "article", 
            "main", 
            ".markdown", 
            ".container .row",
            ".main-wrapper", 
            "#__docusaurus_skipToContent_fallback"
        ]
        
        for selector in selectors:
            main_content = soup.select(selector)
            if main_content:
                break
        
        # If we found a main content container
        if main_content:
            # Remove navigation elements
            for nav in main_content[0].select("nav"):
                nav.extract()
                
            # Remove header/footer elements
            for el in main_content[0].select("header, footer"):
                el.extract()
                
            # Clean up any other non-content elements
            for el in main_content[0].select(".pagination-nav, .tocCollapsible, .tableOfContents"):
                el.extract()
                
            return str(main_content[0])
        
        # If we couldn't find any main content, return the body
        body = soup.find('body')
        if body:
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
        
        # Fix relative links
        if source_path:
            base_dir = os.path.dirname(source_path)
            markdown = fix_relative_links(markdown, base_dir)
        
        return markdown
    except Exception as e:
        print(f"Error converting to markdown: {e}")
        return f"Error converting content: {str(e)}"

def fix_relative_links(markdown, base_dir):
    """Fix relative links in markdown to point to the correct files."""
    # Pattern for markdown links: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        
        # Skip external links and anchors
        if url.startswith(('http', 'mailto', '#', '/')):
            return f'[{text}]({url})'
        
        # Convert .html links to .md
        if url.endswith('.html'):
            url = url.replace('.html', '.md')
        
        # Add path relative to base_dir if needed
        # This would need more logic depending on the actual structure
        
        return f'[{text}]({url})'
    
    return re.sub(link_pattern, replace_link, markdown)

def save_markdown(markdown, output_file):
    """Save markdown content to a file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"Created {output_file}")

def process_html_file(file_path, output_dir, prefix=""):
    """Process an HTML file and convert it to Markdown."""
    rel_path = os.path.relpath(file_path, SOURCE_DIR)
    print(f"Processing {rel_path}...")
    
    # Skip certain files
    skip_patterns = ["404.html", "search.html"]
    if any(pattern in file_path for pattern in skip_patterns):
        print(f"Skipping {file_path}")
        return None
    
    # Determine the output file path
    file_name = os.path.basename(file_path).replace('.html', '.md')
    if '/' in rel_path:
        # Create subdirectories
        sub_dir = os.path.join(output_dir, os.path.dirname(rel_path))
        os.makedirs(sub_dir, exist_ok=True)
        output_file = os.path.join(sub_dir, file_name)
    else:
        output_file = os.path.join(output_dir, file_name)
    
    # Read HTML content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except UnicodeDecodeError:
        try:
            # Try with another encoding if UTF-8 fails
            with open(file_path, 'r', encoding='latin1') as f:
                html_content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None
    
    # Convert to Markdown
    try:
        markdown = html_to_markdown(html_content, file_path)
        
        # Add a title and source reference
        title = prefix + os.path.basename(file_path).replace('.html', '').replace('-', ' ').title()
        markdown = f"# {title}\n\n" + \
                f"*Source: {rel_path}*\n\n" + markdown
        
        # Save Markdown file
        save_markdown(markdown, output_file)
        return output_file
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def copy_images():
    """Copy images from the source to the target directory."""
    source_img_dir = os.path.join(SOURCE_DIR, "img")
    target_img_dir = os.path.join(TARGET_DIR, "img")
    
    if os.path.exists(source_img_dir):
        if os.path.exists(target_img_dir):
            shutil.rmtree(target_img_dir)
        shutil.copytree(source_img_dir, target_img_dir)
        print(f"Copied images to {target_img_dir}")
    
    # Also copy assets that might contain images
    source_assets_dir = os.path.join(SOURCE_DIR, "assets")
    target_assets_dir = os.path.join(TARGET_DIR, "assets")
    
    if os.path.exists(source_assets_dir):
        if os.path.exists(target_assets_dir):
            shutil.rmtree(target_assets_dir)
        shutil.copytree(source_assets_dir, target_assets_dir)
        print(f"Copied assets to {target_assets_dir}")

def create_index_file(processed_files):
    """Create an index markdown file for the documentation."""
    index_content = """# Lightweight Charts Documentation

This is a converted version of the official Lightweight Charts documentation from TradingView,
organized for easier reference.

## Contents

- [API Reference](api/README.md)
- [Tutorials](tutorials/README.md)
- [Examples](examples/README.md)

## About Lightweight Charts

Lightweight Charts™ is a library for creating interactive financial charts developed by TradingView.
This documentation provides all the information needed to get started and make the most of its features.

## Quick Links

"""
    # Add some direct links to important docs
    for file_path in processed_files:
        if file_path and "api" in file_path.lower():
            rel_path = os.path.relpath(file_path, TARGET_DIR)
            name = os.path.basename(file_path).replace(".md", "").replace("-", " ").title()
            index_content += f"- [{name}]({rel_path})\n"
    
    save_markdown(index_content, os.path.join(TARGET_DIR, "README.md"))

def create_section_readme(section_dir, title, intro_text=""):
    """Create a README for a section directory listing its contents."""
    files = []
    for root, _, filenames in os.walk(section_dir):
        for filename in filenames:
            if filename.endswith(".md") and filename != "README.md":
                rel_path = os.path.relpath(os.path.join(root, filename), section_dir)
                files.append(rel_path)
    
    # Sort files alphabetically
    files.sort()
    
    content = f"# {title}\n\n{intro_text}\n\n## Contents\n\n"
    
    for file in files:
        name = os.path.basename(file).replace(".md", "").replace("-", " ").title()
        content += f"- [{name}]({file})\n"
    
    save_markdown(content, os.path.join(section_dir, "README.md"))

def main():
    print("Starting HTML to Markdown conversion for Lightweight Charts documentation...")
    
    processed_files = []
    
    # Process main docs.html first to get structure
    main_docs = os.path.join(SOURCE_DIR, "docs.html")
    if os.path.exists(main_docs):
        processed_files.append(process_html_file(main_docs, TARGET_DIR, ""))
    
    # Process API documentation
    print("\nProcessing API documentation...")
    api_files = []
    docs_dir = os.path.join(SOURCE_DIR, "docs")
    
    # Current version docs
    for file in os.listdir(docs_dir):
        if file.endswith(".html") and not file.startswith("next") and not file.startswith("3.") and not file.startswith("4."):
            file_path = os.path.join(docs_dir, file)
            processed_file = process_html_file(file_path, API_DIR, "API: ")
            api_files.append(processed_file)
            processed_files.append(processed_file)
    
    # Process API subdirectories
    api_subdir = os.path.join(docs_dir, "api")
    if os.path.exists(api_subdir):
        for root, _, files in os.walk(api_subdir):
            for file in files:
                if file.endswith(".html"):
                    file_path = os.path.join(root, file)
                    processed_file = process_html_file(file_path, API_DIR, "API: ")
                    api_files.append(processed_file)
                    processed_files.append(processed_file)
    
    # Process tutorials
    print("\nProcessing tutorials...")
    tutorials_dir = os.path.join(SOURCE_DIR, "tutorials")
    if os.path.exists(tutorials_dir):
        for root, _, files in os.walk(tutorials_dir):
            for file in files:
                if file.endswith(".html"):
                    file_path = os.path.join(root, file)
                    # Skip demo files which will be processed separately
                    if "/demos/" not in root:
                        processed_file = process_html_file(file_path, TUTORIALS_DIR, "Tutorial: ")
                        processed_files.append(processed_file)
    
    # Process examples/demos
    print("\nProcessing examples and demos...")
    demos_dir = os.path.join(SOURCE_DIR, "tutorials", "demos")
    if os.path.exists(demos_dir):
        for root, _, files in os.walk(demos_dir):
            for file in files:
                if file.endswith(".html"):
                    file_path = os.path.join(root, file)
                    processed_file = process_html_file(file_path, EXAMPLES_DIR, "Example: ")
                    processed_files.append(processed_file)
    
    # Copy images and assets
    print("\nCopying images and assets...")
    copy_images()
    
    # Create index files
    print("\nCreating index files...")
    create_index_file(processed_files)
    create_section_readme(API_DIR, "API Reference", "The official API reference for the Lightweight Charts library.")
    create_section_readme(TUTORIALS_DIR, "Tutorials", "Tutorials on using Lightweight Charts in different contexts and frameworks.")
    create_section_readme(EXAMPLES_DIR, "Examples", "Example implementations of Lightweight Charts features.")
    
    print("\nConversion complete! The markdown documentation is available at:", TARGET_DIR)

if __name__ == "__main__":
    main()
