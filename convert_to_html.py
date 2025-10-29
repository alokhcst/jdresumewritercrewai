#!/usr/bin/env python3
"""
Simple markdown to HTML converter
Then you can use your browser to print to PDF
"""

import markdown2
import os

def convert_md_to_html():
    """Convert resume.md to resume.html for easy PDF conversion"""
    
    # Check if resume.md exists
    if not os.path.exists('resume.md'):
        print("Error: resume.md not found in current directory")
        return False
    
    try:
        # Read the markdown file
        with open('resume.md', 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Remove the markdown code block wrapper if present
        if md_content.startswith('```markdown'):
            md_content = md_content[11:]  # Remove ```markdown
        if md_content.endswith('```'):
            md_content = md_content[:-3]  # Remove ```
        
        # Convert markdown to HTML
        html_content = markdown2.markdown(md_content, extras=['fenced-code-blocks'])
        
        # Add CSS styling for better formatting
        css_content = """
        <style>
        @page {
            size: A4;
            margin: 1in;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.4;
            color: #333;
            max-width: 8.5in;
            margin: 0 auto;
            padding: 20px;
        }
        
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        h2 {
            color: #34495e;
            margin-top: 25px;
            margin-bottom: 15px;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 3px;
        }
        
        ul {
            margin: 10px 0;
            padding-left: 20px;
        }
        
        li {
            margin: 5px 0;
        }
        
        strong {
            color: #2c3e50;
        }
        
        hr {
            border: none;
            border-top: 1px solid #bdc3c7;
            margin: 20px 0;
        }
        
        /* Print styles */
        @media print {
            body {
                margin: 0;
                padding: 0;
            }
        }
        </style>
        """
        
        # Create HTML document
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Alok Gupta - Resume</title>
            {css_content}
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Write HTML file
        with open('resume.html', 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print("SUCCESS: Converted resume.md to resume.html")
        print("Output file: resume.html")
        print("\nTo convert to PDF:")
        print("1. Open resume.html in your web browser")
        print("2. Press Ctrl+P (or Cmd+P on Mac)")
        print("3. Select 'Save as PDF' as destination")
        print("4. Click 'Save'")
        print(f"\nOr open the file directly: file://{os.path.abspath('resume.html')}")
        
        return True
        
    except Exception as e:
        print(f"ERROR: Error converting to HTML: {e}")
        return False

if __name__ == "__main__":
    convert_md_to_html()