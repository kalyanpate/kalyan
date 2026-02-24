import os
from pypdf import PdfMerger

def merge_pdfs(input_dir, output_filename):
    """
    Merges all PDF files in the specified input directory into a single PDF file.

    Args:
        input_dir (str): The directory containing the PDF files.
        output_filename (str): The name of the output merged PDF file.
    """
    merger = PdfMerger()
    pdf_files = []

    # Find all PDF files in the directory and sort them alphabetically for predictable order
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf') and filename != output_filename:
            pdf_files.append(os.path.join(input_dir, filename))
    
    pdf_files.sort(key=str.lower)

    print(f"Found files to merge: {pdf_files}")

    for pdf_file in pdf_files:
        # Open each PDF file in binary read mode and append to the merger
        with open(pdf_file, 'rb') as f:
            merger.append(f)
            print(f"Appended: {pdf_file}")

    # Write the merged PDF to an output file
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)
        print(f"Successfully created: {output_filename}")

    # Close the merger object to ensure all file handles are released
    merger.close()

if __name__ == "__main__":
    # Define the directory and output filename
    # You might need to change 'pdfs_to_merge' to your directory path
    input_directory = './pdfs_to_merge' 
    output_name = 'merged_document.pdf'

    # Create the directory if it doesn't exist (for testing purposes)
    if not os.path.exists(input_directory):
        os.makedirs(input_directory)
        print(f"Created directory '{input_directory}'. Please add PDF files to it and run the script again.")
    else:
        merge_pdfs(input_directory, output_name)

