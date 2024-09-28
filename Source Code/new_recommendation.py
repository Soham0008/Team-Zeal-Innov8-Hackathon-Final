import os
import csv
import pdfplumber
import json
import re

def read_csv(file_path):
    recommender_map = {}
    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            candidate_id = row[0]
            recommenders = row[1].split(',')
            recommender_map[candidate_id] = recommenders
    return recommender_map

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def read_recommendations(folder_path):
    recommendations = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            recommender_id = file_name.split('_')[-1].split('.')[0]
            with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8', errors='ignore') as file:
                recommendations[recommender_id] = file.read()
    return recommendations

def segregate_sections(text):
    sections = {}
    current_section = None
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Identify section headers
        if re.match(r'(Position|Title|Role|Summary|Highlights|Education|Experience|Skills|Certificates):?', line, re.IGNORECASE):
            current_section = line.split(':')[0].strip().lower()
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)
    
    # Join section lines
    for section in sections:
        sections[section] = ' '.join(sections[section])
    
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

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        data = json.load(file)
    return data

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
            'recommendations': json.dumps(recommendations)  # Store recommendations as JSON string
        })
    return flattened_data

def write_csv(data, file_path):
    if not data:
        return
    
    keys = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8', errors='ignore') as file:
        dict_writer = csv.DictWriter(file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

if __name__ == "__main__":
    resume_dir = 'resumes'
    recommendation_dir = 'recommendations'
    csv_file_path = 'Final_Persons_And_Recommenders.csv'
    
    # Read CSV file
    recommender_map = read_csv(csv_file_path)
    
    # Organize data
    organized_data = organize_data(resume_dir, recommendation_dir, recommender_map)
    
    # Save organized data to JSON file
    json_file_path = 'organized_data.json'
    with open(json_file_path, 'w', encoding='utf-8', errors='ignore') as json_file:
        json.dump(organized_data, json_file, indent=4)
    
    # Read JSON data
    json_data = read_json(json_file_path)
    
    # Flatten JSON data
    flattened_data = flatten_data(json_data)
    
    # Write to CSV
    csv_output_path = 'new_organized_data.csv'
    write_csv(flattened_data, csv_output_path)