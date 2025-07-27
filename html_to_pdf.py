#!/usr/bin/env python3
"""
HTML README to PDF Converter

This script converts the HTML-formatted README.md file to a PDF document.
Since the README is now pure HTML, this should work much more reliably.

Requirements:
    pip install pdfkit (and wkhtmltopdf system dependency)
    OR
    pip install weasyprint (if system dependencies are available)
    OR
    Use built-in browser printing functionality

Usage:
    python html_to_pdf.py
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path

def check_wkhtmltopdf():
    """Check if wkhtmltopdf is available."""
    try:
        result = subprocess.run(['wkhtmltopdf', '--version'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def convert_with_wkhtmltopdf(input_file, output_file):
    """Convert HTML to PDF using wkhtmltopdf directly."""
    try:
        cmd = [
            'wkhtmltopdf',
            '--page-size', 'A4',
            '--margin-top', '1in',
            '--margin-bottom', '1in',
            '--margin-left', '1in',
            '--margin-right', '1in',
            '--encoding', 'UTF-8',
            '--enable-local-file-access',
            input_file,
            output_file
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return True
        else:
            print(f"wkhtmltopdf error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Error running wkhtmltopdf: {e}")
        return False

def convert_with_browser_print():
    """Provide instructions for browser-based conversion."""
    print("\n=== Browser-Based PDF Conversion ===")
    print("Since system dependencies aren't available, you can use your browser:")
    print()
    print("1. Open the README.md file in a web browser:")
    print("   - Right-click on README.md in your file manager")
    print("   - Select 'Open with' → 'Web Browser'")
    print("   - OR drag and drop README.md into a browser window")
    print()
    print("2. Print to PDF:")
    print("   - Press Ctrl+P (Cmd+P on Mac)")
    print("   - Select 'Save as PDF' as the destination")
    print("   - Adjust settings as needed")
    print("   - Click 'Save'")
    print()
    print("This will give you a high-quality PDF with all formatting preserved.")
    return True

def create_styled_html(input_file, output_file):
    """Create a standalone HTML file with embedded CSS for better PDF conversion."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add CSS styling for better PDF output
    css_styles = """
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
        }
        
        h1, h2, h3, h4, h5, h6 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
            color: #1f2328;
        }
        
        h1 {
            font-size: 2em;
            border-bottom: 1px solid #d1d9e0;
            padding-bottom: 10px;
        }
        
        h2 {
            font-size: 1.5em;
            border-bottom: 1px solid #d1d9e0;
            padding-bottom: 8px;
        }
        
        h3 {
            font-size: 1.25em;
        }
        
        p {
            margin-bottom: 16px;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
            border: 1px solid #d1d9e0;
            border-radius: 6px;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        
        table, th, td {
            border: 1px solid #d1d9e0;
        }
        
        th, td {
            padding: 12px;
            text-align: left;
        }
        
        th {
            background-color: #f6f8fa;
            font-weight: 600;
        }
        
        code {
            background-color: #f6f8fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            font-size: 85%;
        }
        
        pre {
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 16px 0;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
        }
        
        ul, ol {
            margin: 16px 0;
            padding-left: 30px;
        }
        
        li {
            margin: 4px 0;
        }
        
        strong {
            font-weight: 600;
        }
        
        em {
            font-style: italic;
        }
        
        a {
            color: #0969da;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        @media print {
            body {
                margin: 0;
                padding: 15px;
            }
            
            h1, h2, h3, h4, h5, h6 {
                page-break-after: avoid;
            }
            
            img {
                page-break-inside: avoid;
            }
            
            table {
                page-break-inside: avoid;
            }
            
            pre {
                page-break-inside: avoid;
            }
        }
    </style>
    """
    
    # Insert CSS into the head section
    if '<head>' in content:
        content = content.replace('<head>', f'<head>\n{css_styles}')
    else:
        # If no head section, add it after the html tag
        content = content.replace('<html>', f'<html>\n<head>\n{css_styles}\n</head>')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return output_file

def main():
    """Main function to convert HTML README to PDF."""
    
    # Define file paths
    readme_path = "README.md"
    output_path = "smFISH_Analysis_Pipeline_Documentation.pdf"
    
    # Check if README.md exists
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found in current directory")
        return False
    
    print("Converting HTML README.md to PDF...")
    print(f"Input: {readme_path}")
    print(f"Output: {output_path}")
    
    # Create a styled HTML version
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as temp_file:
        styled_html = create_styled_html(readme_path, temp_file.name)
    
    try:
        # Try wkhtmltopdf first
        if check_wkhtmltopdf():
            print("\n1. Using wkhtmltopdf...")
            success = convert_with_wkhtmltopdf(styled_html, output_path)
            
            if success:
                print(f"✅ Successfully created PDF: {output_path}")
                if os.path.exists(output_path):
                    file_size = os.path.getsize(output_path) / 1024
                    if file_size > 1024:
                        print(f"File size: {file_size/1024:.1f} MB")
                    else:
                        print(f"File size: {file_size:.1f} KB")
                return True
        
        # If wkhtmltopdf failed or isn't available, provide browser instructions
        print("wkhtmltopdf not available or failed.")
        convert_with_browser_print()
        
        # Also save the styled HTML for manual conversion
        styled_output = "README_styled.html"
        create_styled_html(readme_path, styled_output)
        print(f"\n📄 Created styled HTML file: {styled_output}")
        print("You can open this file in a browser and print to PDF for best results.")
        
        return True
        
    finally:
        # Clean up temporary file
        if os.path.exists(styled_html):
            os.unlink(styled_html)

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
