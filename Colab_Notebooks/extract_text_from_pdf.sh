#!/bin/bash

# Function to extract text from PDF
extract_text_from_pdf() {
    local pdf_file="$1"
    local output_file="${pdf_file%.pdf}.txt"

    if [ ! -f "$pdf_file" ]; then
        echo "Error: PDF file '$pdf_file' not found."
        return 1
    fi

    # Extract text from PDF
    pdftotext "$pdf_file" "$output_file"

    if [ $? -ne 0 ]; then
        echo "Error: Failed to extract text from PDF."
        return 1
    fi

    echo "Text extracted successfully to $output_file"
}

# Main script
if [ $# -eq 0 ]; then
    echo "Usage: $0 <pdf_file>"
    exit 1
fi

pdf_file="$1"
extract_text_from_pdf "$pdf_file"