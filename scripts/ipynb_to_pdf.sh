#!/bin/bash

# Function to convert a single notebook to PDF using LaTeX
convert_to_pdf_latex() {
    local notebook="$1"
    
    echo "Converting $notebook to PDF..."
    
    # Use jupyter-nbconvert with LaTeX to convert the notebook to PDF
    jupyter nbconvert --to pdf "$notebook"
    
    if [ $? -eq 0 ]; then
        echo "Successfully converted $notebook to PDF"
    else
        echo "Failed to convert $notebook"
    fi
}

# Process all .ipynb files in the current directory
for file in *.ipynb; do
    convert_to_pdf_latex "$file"
done

echo "PDF conversion complete."