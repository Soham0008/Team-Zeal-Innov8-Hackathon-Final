import os
import pandas as pd
import fitz  # PyMuPDF

def read_first_line_of_pdf(file_path):
    doc = fitz.open(file_path)
    first_line = ""
    if len(doc) > 0:
        first_page = doc[0]
        text = first_page.get_text().split('\n')
        if len(text) > 0:
            first_line = text[0]
    return first_line

def extract_positions(resume_dir):
    positions = []
    for file_name in os.listdir(resume_dir):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(resume_dir, file_name)
            first_line = read_first_line_of_pdf(file_path)
            positions.append(first_line)
    return positions

def write_positions_to_csv(positions, output_file):
    df = pd.DataFrame(positions, columns=['position'])
    df.to_csv(output_file, index=False)

def main():
    resume_dir = 'resumes'  # Replace with the path to your resume directory
    output_file = 'positions.csv'
    
    positions = extract_positions(resume_dir)
    write_positions_to_csv(positions, output_file)
    
    print(f"Positions have been written to {output_file}")

if __name__ == "__main__":
    main()