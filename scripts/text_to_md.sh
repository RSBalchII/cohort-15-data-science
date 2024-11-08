#!/bin/bash

# Function to convert HTML to Markdown using nbconvert
convert_html_to_md() {
    local input_file="$1"
    local base_name=$(basename "$input_file" .html)
    
    if jupyter nbconvert --to markdown "$input_file" --output "${base_name}.md" --no-input --no-output; then
        echo "Converted: $input_file -> ${base_name}.md"
    else
        echo "Failed to convert: $input_file"
    fi
}

# Check if nbconvert is installed
if ! command -v jupyter &> /dev/null; then
    echo "Jupyter (nbconvert) is not installed or not in PATH. Please install it and try again."
    echo "You can install it using: pip install nbconvert"
    exit 1
fi

# Get output directory from user or use current directory
read -p "Enter output directory (press Enter to use current directory): " output_dir
if [ -z "$output_dir" ]; then
    output_dir="."
fi

# Create output directory if it doesn't exist
mkdir -p "$output_dir"

# Loop through all HTML files in the current directory and subdirectories
count=0
total=$(find . -name "*.html" | wc -l)

find . -name "*.html" | while read file; do
    if [ -f "$file" ]; then
        # Check if file contains HTML content
        if grep -q "<html>" "$file"; then
            convert_html_to_md "$file"
            ((count++))
            echo "Progress: $count/$total"
        else
            echo "Skipping non-HTML file: $file"
        fi
    fi
done

echo "All conversions complete."