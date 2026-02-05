#!/usr/bin/env python3
"""
Add default author to posts that are missing the author field
"""

import re
from pathlib import Path

POSTS_DIR = Path("/Users/agnesriley/Github/wordpress-to-astro/src/posts")
DEFAULT_AUTHOR = "ZeroBlue"

def has_author(content):
    """Check if frontmatter has an author field"""
    # Look for author: in the frontmatter (between --- markers)
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        return re.search(r'^author:', frontmatter, re.MULTILINE) is not None
    return False

def add_author(content):
    """Add author field to frontmatter"""
    # Find the frontmatter
    frontmatter_match = re.search(r'^(---\n.*?)\n(---)', content, re.DOTALL | re.MULTILINE)
    if frontmatter_match:
        # Insert author before the closing ---
        before_closing = frontmatter_match.group(1)
        closing = frontmatter_match.group(2)
        
        # Add author field
        new_frontmatter = f'{before_closing}\nauthor: "{DEFAULT_AUTHOR}"\n{closing}'
        
        # Replace in content
        content = content.replace(frontmatter_match.group(0), new_frontmatter)
    
    return content

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not has_author(content):
            content = add_author(content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added author to: {filepath.name}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"✗ Error processing {filepath.name}: {e}")
        return False

if __name__ == "__main__":
    print("Adding missing author fields...")
    print("=" * 50)
    
    fixed_count = 0
    for md_file in POSTS_DIR.glob("*.md"):
        if process_file(md_file):
            fixed_count += 1
    
    print("=" * 50)
    print(f"✓ Added author to {fixed_count} files")

