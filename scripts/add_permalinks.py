#!/usr/bin/env python3
"""
Add permalinks to markdown files that don't have them.
The permalink is derived from the filename.
"""

import os
import re
from pathlib import Path

def add_permalink_to_post(filepath):
    """Add permalink to a post if it doesn't have one."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if permalink already exists
    if 'permalink:' in content:
        print(f"✓ {filepath.name} already has permalink")
        return False
    
    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        print(f"✗ {filepath.name} has no frontmatter")
        return False
    
    frontmatter = match.group(1)
    body = match.group(2)
    
    # Generate permalink from filename
    filename = filepath.stem
    # Remove date prefix if present (e.g., "2022-09-24-hello-world" -> "hello-world")
    filename = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
    
    # Skip special files
    if filename in ['blog', 'portfolio', 'confirm-subscription', 'payment-confirmation', 
                    'payment-failed', 'return-policy', 'terms-and-conditions', 'upload',
                    'stripe_success', 'stripe_failure', 'web-development']:
        print(f"⊘ {filepath.name} is a special page, skipping")
        return False
    
    permalink = f"/{filename}/"
    
    # Add permalink to frontmatter
    new_frontmatter = frontmatter + f'\npermalink: {permalink}'
    new_content = f"---\n{new_frontmatter}\n---\n{body}"
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Added permalink to {filepath.name}: {permalink}")
    return True

def main():
    posts_dir = Path('src/posts')
    count = 0
    
    for md_file in sorted(posts_dir.glob('*.md')):
        if add_permalink_to_post(md_file):
            count += 1
    
    print(f"\n✓ Added permalinks to {count} posts")

if __name__ == '__main__':
    main()

