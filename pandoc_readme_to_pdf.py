#!/usr/bin/env python3
"""
High-Quality README to PDF Converter using Pandoc

This script converts a README.md file containing both HTML and Markdown content
to a high-quality PDF document using Pandoc, which handles mixed content excellently.

Requirements:
    - pandoc (system installation)
    - Optional: texlive for better PDF output

Usage:
    python pandoc_readme_to_pdf.py
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_pandoc():
    """Check if pandoc is available."""
    return shutil.which('pandoc') is not None

def check_latex():
    """Check if LaTeX is available for better PDF output."""
    return shutil.which('pdflatex') is not None or shutil.which('xelatex') is not None

def create_pandoc_config():
    """Create a pandoc configuration for better PDF output."""

    metadata = """---
title: "smFISH Analysis Pipeline Documentation"
author: "Quantitative Analysis Project"
date: "\\today"
geometry: margin=1in
fontsize: 11pt
linestretch: 1.2
documentclass: article
header-includes:
  - \\usepackage{fancyhdr}
  - \\usepackage{graphicx}
  - \\usepackage{float}
  - \\usepackage{booktabs}
  - \\usepackage{longtable}
  - \\usepackage{array}
  - \\usepackage{multirow}
  - \\usepackage{wrapfig}
  - \\usepackage{colortbl}
  - \\usepackage{pdflscape}
  - \\usepackage{tabu}
  - \\usepackage{threeparttable}
  - \\usepackage{threeparttablex}
  - \\usepackage[normalem]{ulem}
  - \\usepackage{makecell}
  - \\usepackage{xcolor}
  - \\pagestyle{fancy}
  - \\fancyhf{}
  - \\fancyhead[L]{smFISH Analysis Pipeline}
  - \\fancyhead[R]{\\thepage}
  - \\renewcommand{\\headrulewidth}{0.4pt}
---

"""
    
    with open('metadata.yaml', 'w') as f:
        f.write(metadata)
    
    return 'metadata.yaml'

def preprocess_readme(input_file, output_file):
    """Preprocess README to fix image paths and formatting."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix image paths - ensure they're relative to current directory
    import re
    
    # Convert absolute paths starting with / to relative paths
    content = re.sub(r'src="/([^"]*)"', r'src="./\1"', content)
    
    # Ensure other relative paths are properly formatted
    content = re.sub(r'src="([^./][^"]*)"', r'src="./\1"', content)
    
    # Fix image references in markdown format
    content = re.sub(r'!\[([^\]]*)\]\(/([^)]*)\)', r'![\1](./\2)', content)
    content = re.sub(r'!\[([^\]]*)\]\(([^./][^)]*)\)', r'![\1](./\2)', content)
    
    # Improve table formatting for pandoc
    content = re.sub(r'<table>', r'<table style="width:100%">', content)
    
    # Add figure captions for better PDF formatting
    content = re.sub(
        r'<img[^>]*alt="([^"]*)"[^>]*>',
        lambda m: f'{m.group(0)}\n\n*{m.group(1)}*\n',
        content
    )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return output_file

def convert_with_pandoc(input_file, output_file, use_latex=True):
    """Convert README to PDF using pandoc."""
    
    try:
        # Preprocess the README
        processed_file = preprocess_readme(input_file, 'processed_readme.md')
        
        # Create metadata file
        metadata_file = create_pandoc_config()
        
        # Build pandoc command
        cmd = ['pandoc']
        
        # Add metadata
        cmd.extend([metadata_file, processed_file])
        
        # Output format and file
        cmd.extend(['-o', output_file])
        
        if use_latex and check_latex():
            # Use LaTeX engine for better output
            cmd.extend([
                '--pdf-engine=xelatex',
                '--variable', 'geometry:margin=1in',
                '--variable', 'fontsize=11pt',
                '--variable', 'linestretch=1.2'
            ])
        else:
            # Use HTML to PDF conversion
            cmd.extend([
                '--pdf-engine=wkhtmltopdf',
                '--variable', 'margin-top=1in',
                '--variable', 'margin-bottom=1in',
                '--variable', 'margin-left=1in',
                '--variable', 'margin-right=1in'
            ])
        
        # Additional options for better formatting
        cmd.extend([
            '--standalone',
            '--table-of-contents',
            '--toc-depth=3',
            '--number-sections',
            '--highlight-style=github',
            '--filter=pandoc-crossref' if shutil.which('pandoc-crossref') else '--no-highlight'
        ])
        
        # Remove the crossref filter if not available
        if '--filter=pandoc-crossref' in cmd and not shutil.which('pandoc-crossref'):
            cmd.remove('--filter=pandoc-crossref')
            cmd.remove('--no-highlight')
        
        print(f"Running pandoc command: {' '.join(cmd)}")
        
        # Run pandoc
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Clean up temporary files
            for temp_file in [processed_file, metadata_file]:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            return True
        else:
            print(f"Pandoc error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Error running pandoc: {e}")
        return False

def main():
    """Main function to convert README.md to PDF using pandoc."""
    
    # Check if pandoc is available
    if not check_pandoc():
        print("❌ Pandoc is not available. Please install pandoc first.")
        print("Visit: https://pandoc.org/installing.html")
        return False
    
    # Check LaTeX availability
    has_latex = check_latex()
    if has_latex:
        print("✅ LaTeX found - will use high-quality PDF engine")
    else:
        print("⚠️  LaTeX not found - will use alternative PDF engine")
        print("For best results, consider installing LaTeX (e.g., MacTeX on macOS)")
    
    # Define file paths
    readme_path = "README.md"
    output_path = "smFISH_Analysis_Pipeline_Documentation.pdf"
    
    # Check if README.md exists
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found in current directory")
        return False
    
    print(f"\nConverting README.md to PDF using Pandoc...")
    print(f"Input: {readme_path}")
    print(f"Output: {output_path}")
    
    # Try with LaTeX first, then fallback to HTML
    success = False
    
    if has_latex:
        print("\n1. Attempting conversion with LaTeX engine...")
        success = convert_with_pandoc(readme_path, output_path, use_latex=True)
    
    if not success:
        print("\n2. Attempting conversion with HTML engine...")
        success = convert_with_pandoc(readme_path, output_path, use_latex=False)
    
    if success:
        print(f"\n✅ Successfully created PDF: {output_path}")
        if os.path.exists(output_path):
            file_size = os.path.getsize(output_path) / 1024
            if file_size > 1024:
                print(f"File size: {file_size/1024:.1f} MB")
            else:
                print(f"File size: {file_size:.1f} KB")
        
        print("\n📄 PDF Features:")
        print("  • Table of contents")
        print("  • Numbered sections")
        print("  • Syntax highlighting")
        print("  • Preserved images and tables")
        print("  • Professional formatting")
        
        return True
    else:
        print("\n❌ Failed to create PDF with pandoc")
        print("You can try the simpler conversion with: python simple_readme_to_pdf.py")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
