#!/usr/bin/env python3
"""
Extract WordPress blog posts from HTML files and convert to Markdown for Astro
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
import html2text

# Configuration
WORDPRESS_DIR = Path("/Users/agnesriley/Github/zerobluetech.com")
OUTPUT_DIR = Path("/Users/agnesriley/Github/wordpress-to-astro/src/posts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Initialize html2text converter
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False
h.ignore_emphasis = False
h.body_width = 0  # Don't wrap lines

def extract_metadata(soup):
    """Extract metadata from HTML head"""
    metadata = {}
    
    # Title
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text()
        # Remove " - ZeroBlue" suffix
        title = re.sub(r'\s*[-–]\s*ZeroBlue\s*$', '', title)
        metadata['title'] = title.strip()
    
    # Published date
    pub_meta = soup.find('meta', property='article:published_time')
    if pub_meta and pub_meta.get('content'):
        metadata['pubDate'] = pub_meta['content']
    
    # Modified date
    mod_meta = soup.find('meta', property='article:modified_time')
    if mod_meta and mod_meta.get('content'):
        metadata['modDate'] = mod_meta['content']
    
    # Description
    desc_meta = soup.find('meta', property='og:description') or soup.find('meta', attrs={'name': 'description'})
    if desc_meta and desc_meta.get('content'):
        metadata['description'] = desc_meta['content']
    
    # Hero image
    img_meta = soup.find('meta', property='og:image')
    if img_meta and img_meta.get('content'):
        img_url = img_meta['content']
        # Convert to relative path
        img_url = img_url.replace('https://zerobluetech.com/', '/')
        metadata['heroImage'] = img_url
    
    # Author
    author_meta = soup.find('span', class_='author')
    if author_meta:
        author_link = author_meta.find('a')
        if author_link:
            metadata['author'] = author_link.get_text().strip()
    
    # Categories
    cat_span = soup.find('span', class_='blog-categories')
    if cat_span:
        cats = [a.get_text().strip() for a in cat_span.find_all('a')]
        if cats:
            metadata['categories'] = cats
    
    return metadata

def extract_content(soup):
    """Extract main content from article"""
    # Find the entry-content div
    content_div = soup.find('div', class_='entry-content')
    
    if not content_div:
        return None
    
    # Convert HTML to Markdown
    html_content = str(content_div)
    markdown_content = h.handle(html_content)
    
    # Clean up the markdown
    markdown_content = markdown_content.strip()
    
    return markdown_content

def process_post(post_dir):
    """Process a single blog post directory"""
    index_file = post_dir / 'index.html'
    
    if not index_file.exists():
        return None
    
    print(f"Processing: {post_dir.name}")
    
    try:
        with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract metadata
        metadata = extract_metadata(soup)
        
        # Extract content
        content = extract_content(soup)
        
        if not content or not metadata.get('title'):
            print(f"  ⚠️  Skipping {post_dir.name} - missing content or title")
            return None
        
        # Create markdown file
        slug = post_dir.name
        output_file = OUTPUT_DIR / f"{slug}.md"
        
        # Build frontmatter
        frontmatter = "---\n"
        frontmatter += f"title: \"{metadata.get('title', '')}\"\n"
        if 'description' in metadata:
            frontmatter += f"description: \"{metadata['description']}\"\n"
        if 'pubDate' in metadata:
            frontmatter += f"pubDate: \"{metadata['pubDate']}\"\n"
        if 'modDate' in metadata:
            frontmatter += f"updatedDate: \"{metadata['modDate']}\"\n"
        if 'heroImage' in metadata:
            frontmatter += f"heroImage: \"{metadata['heroImage']}\"\n"
        if 'author' in metadata:
            frontmatter += f"author: \"{metadata['author']}\"\n"
        if 'categories' in metadata:
            frontmatter += f"tags: {json.dumps(metadata['categories'])}\n"
        frontmatter += "---\n\n"
        
        # Write the file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write(content)
        
        print(f"  ✓ Created {output_file.name}")
        return output_file
        
    except Exception as e:
        print(f"  ✗ Error processing {post_dir.name}: {e}")
        return None

if __name__ == "__main__":
    print("WordPress to Astro Post Extractor")
    print("=" * 50)
    print(f"Source: {WORDPRESS_DIR}")
    print(f"Output: {OUTPUT_DIR}")
    print()
    
    # Find all potential blog post directories
    post_count = 0
    for item in WORDPRESS_DIR.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            # Skip system directories
            if item.name in ['wp-content', 'wp-includes', 'wp-json', 'cdn-cgi', 
                            'author', 'category', 'tag', 'feed', 'comments', 
                            'customer-area', 'portfolio-item', 'jobs', 'software']:
                continue
            
            # Skip year directories
            if item.name.isdigit():
                continue
            
            result = process_post(item)
            if result:
                post_count += 1
    
    print()
    print("=" * 50)
    print(f"✓ Extracted {post_count} blog posts")

