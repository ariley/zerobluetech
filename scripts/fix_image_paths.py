#!/usr/bin/env python3
"""
Fix image paths in markdown files - convert relative paths to absolute paths
"""

import re
from pathlib import Path

POSTS_DIR = Path("/Users/agnesriley/Github/wordpress-to-astro/src/posts")

def fix_image_paths(content):
    """Fix relative image paths to absolute paths"""
    # Fix markdown image syntax: ![alt](../wp-content/...) -> ![alt](/wp-content/...)
    content = re.sub(r'!\[(.*?)\]\(\.\./wp-content/', r'![\1](/wp-content/', content)

    # Fix markdown link syntax: [text](../wp-content/...) -> [text](/wp-content/...)
    content = re.sub(r'\[(.*?)\]\(\.\./wp-content/', r'[\1](/wp-content/', content)

    # Fix any remaining ../wp-content references
    content = content.replace('../wp-content/', '/wp-content/')

    # Fix https://zerobluetech.com/wp-content/ to /wp-content/
    content = content.replace('https://zerobluetech.com/wp-content/', '/wp-content/')

    # Fix references to other subdomains (wp.zerobluetech.com, blog.zerobluetech.com, etc.)
    content = re.sub(r'\.\./\.\./[a-z]+\.zerobluetech\.com/wp-content/', '/wp-content/', content)
    content = re.sub(r'https?://[a-z]+\.zerobluetech\.com/wp-content/', '/wp-content/', content)

    return content

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = fix_image_paths(content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Fixed: {filepath.name}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"✗ Error processing {filepath.name}: {e}")
        return False

if __name__ == "__main__":
    print("Fixing image paths in markdown files...")
    print("=" * 50)
    
    fixed_count = 0
    for md_file in POSTS_DIR.glob("*.md"):
        if process_file(md_file):
            fixed_count += 1
    
    print("=" * 50)
    print(f"✓ Fixed {fixed_count} files")

