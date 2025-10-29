#!/bin/bash
# Convert resume.md to PDF using pandoc
# Alternative method if Python conversion doesn't work

echo "Converting resume.md to PDF using pandoc..."

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "❌ Pandoc not found. Please install pandoc first:"
    echo "   Windows: choco install pandoc"
    echo "   macOS: brew install pandoc"
    echo "   Linux: sudo apt-get install pandoc"
    exit 1
fi

# Check if resume.md exists
if [ ! -f "resume.md" ]; then
    echo "❌ resume.md not found in current directory"
    exit 1
fi

# Convert using pandoc
pandoc resume.md -o resume.pdf --pdf-engine=xelatex -V geometry:margin=1in

if [ $? -eq 0 ]; then
    echo "✅ Successfully converted resume.md to resume.pdf"
    echo "📄 Output file: resume.pdf"
else
    echo "❌ Error converting to PDF"
    exit 1
fi
