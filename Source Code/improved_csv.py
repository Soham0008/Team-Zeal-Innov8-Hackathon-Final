import os
import re
import json
import pandas as pd
import spacy
import fitz  # PyMuPDF

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def read_recommendations(folder_path):
    recommendations = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            recommender_id = os.path.splitext(file_name)[0]
            file_path = os.path.join(folder_path, file_name)
            recommendations[recommender_id] = read_pdf(file_path)
    return recommendations

def segregate_sections(text):
    section_headers = {
        'position': ['position', 'professional position'],
        'summary': ['summary', 'professional summary'],
        'highlights': ['highlights', 'key highlights'],
        'experience': ['experience', 'professional experience', 'work experience'],
        'education': ['education', 'academic background'],
        'skills': ['skills', 'technical skills'],
        'certificates': ['certificates', 'certifications']
    }

    sections = {key: '' for key in section_headers.keys()}
    current_section = None

    for line in text.split('\n'):
        line = line.strip().lower()
        for section, headers in section_headers.items():
            if any(re.match(rf'^{header}', line) for header in headers):
                current_section = section
                break
        if current_section:
            sections[current_section] += line + '\n'

    return sections

def organize_data(resume_dir, recommendation_dir, recommender_map):
    data = {}
    for candidate_id in recommender_map.keys():
        resume_path = os.path.join(resume_dir, f'Resume_of_ID_{candidate_id}.pdf')
        recommendation_folder = os.path.join(recommendation_dir, f'Recommendation_Letters_of_ID_{candidate_id}')
        
        resume_text = read_pdf(resume_path)
        recommendations = read_recommendations(recommendation_folder)
        
        sections = segregate_sections(resume_text)
        
        data[candidate_id] = {
            'sections': sections,
            'recommendations': recommendations,  # Dictionary of recommender ID and recommendation
            'recommenders': ','.join(recommender_map[candidate_id])
        }
    return data

def read_csv(file_path):
    df = pd.read_csv(file_path)
    if 'ID' not in df.columns or 'Recommenders ID' not in df.columns:
        raise KeyError("CSV file must contain 'ID' and 'Recommenders ID' columns")
    
    recommender_map = {}
    for _, row in df.iterrows():
        candidate_id = row['ID']
        recommender_id = row['Recommenders ID']
        if candidate_id not in recommender_map:
            recommender_map[candidate_id] = []
        recommender_map[candidate_id].append(recommender_id)
    return recommender_map

def flatten_data(data):
    flattened_data = []
    for candidate_id, details in data.items():
        sections = details['sections']
        recommendations = details['recommendations']
        flattened_data.append({
            'candidate_id': candidate_id,
            'position': sections.get('position', ''),
            'summary': sections.get('summary', ''),
            'highlights': sections.get('highlights', ''),
            'experience': sections.get('experience', ''),
            'education': sections.get('education', ''),
            'skills': sections.get('skills', ''),
            'certificates': sections.get('certificates', ''),
            'recommenders': details['recommenders'],
        })
    return flattened_data

def write_to_json_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def write_to_csv_file(data, output_file):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)

def main():
    resume_dir = 'resumes'
    recommendation_dir = 'recommendations'
    recommender_map = read_csv('Datasets/Final_Persons_And_Recommenders.csv')

    data = organize_data(resume_dir, recommendation_dir, recommender_map)
    flattened_data = flatten_data(data)

    json_output_file = 'improved_output.json'
    csv_output_file = 'improved_output.csv'
    write_to_json_file(flattened_data, json_output_file)
    write_to_csv_file(flattened_data, csv_output_file)
    print(f"Flattened data has been written to {json_output_file} and {csv_output_file}")

if __name__ == "__main__":
    main()