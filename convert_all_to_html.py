#!/usr/bin/env python3
"""
Convert all markdown files to HTML for easy PDF conversion
"""

import markdown2
import os
import glob

def convert_md_to_html(md_file, output_name=None):
    """Convert a single markdown file to HTML"""
    
    if not os.path.exists(md_file):
        print(f"Warning: {md_file} not found")
        return False
    
    try:
        # Read the markdown file
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Remove the markdown code block wrapper if present
        if md_content.startswith('```markdown'):
            md_content = md_content[11:]  # Remove ```markdown
        if md_content.endswith('```'):
            md_content = md_content[:-3]  # Remove ```
        
        # Convert markdown to HTML
        html_content = markdown2.markdown(md_content, extras=['fenced-code-blocks'])
        
        # Determine output filename
        if output_name:
            html_file = f"{output_name}.html"
        else:
            html_file = md_file.replace('.md', '.html')
        
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
        
        h3 {
            color: #34495e;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        ul, ol {
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
        
        blockquote {
            border-left: 4px solid #3498db;
            margin: 20px 0;
            padding-left: 20px;
            color: #555;
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
        title = os.path.basename(md_file).replace('.md', '').replace('_', ' ').title()
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>{title}</title>
            {css_content}
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Write HTML file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"SUCCESS: Converted {md_file} to {html_file}")
        return True
        
    except Exception as e:
        print(f"ERROR: Error converting {md_file}: {e}")
        return False

def convert_all_md_files():
    """Convert all markdown files in the current directory"""
    
    # List of expected markdown files (all in output directory)
    md_files = [
        'output/resume.md',
        'output/cover_letter.md', 
        'output/skills_gap_analysis.md',
        'output/interview_prep_guide.md',
        'output/linkedin_messages.md',
        'output/proposed_job_analysis.md',
        'output/company_intelligence.md',
        'output/candidate_profile_analysis.md',
        'output/skills_matching_report.md',
        'output/resume_content.md'
    ]
    
    print("Converting all markdown files to HTML...")
    print("=" * 50)
    
    converted_count = 0
    for md_file in md_files:
        if os.path.exists(md_file):
            if convert_md_to_html(md_file):
                converted_count += 1
        else:
            print(f"SKIP: {md_file} not found")
    
    print("=" * 50)
    print(f"Conversion complete! {converted_count} files converted.")
    
    if converted_count > 0:
        print("\nTo convert to PDF:")
        print("1. Open each .html file in your web browser")
        print("2. Press Ctrl+P (or Cmd+P on Mac)")
        print("3. Select 'Save as PDF' as destination")
        print("4. Click 'Save'")
        print("\nOr open all files at once:")
        for md_file in md_files:
            html_file = md_file.replace('.md', '.html')
            if os.path.exists(html_file):
                print(f"   start {html_file}")

if __name__ == "__main__":
    convert_all_md_files()
