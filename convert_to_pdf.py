#!/usr/bin/env python3
"""
Convert resume.md to PDF using markdown2 and weasyprint
"""

import markdown2
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os

def convert_md_to_pdf():
    """Convert resume.md to resume.pdf"""
    
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
        
        # Add CSS styling for better PDF formatting
        css_content = """
        @page {
            size: A4;
            margin: 1in;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.4;
            color: #333;
        }
        
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
            margin-bottom: 20px;
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
        """
        
        # Create HTML document
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>{css_content}</style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Convert to PDF
        print("Converting resume.md to PDF...")
        HTML(string=full_html).write_pdf('resume.pdf')
        
        print("✅ Successfully converted resume.md to resume.pdf")
        print("📄 Output file: resume.pdf")
        return True
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install required packages:")
        print("pip install markdown2 weasyprint")
        return False
        
    except Exception as e:
        print(f"❌ Error converting to PDF: {e}")
        return False

if __name__ == "__main__":
    convert_md_to_pdf()
