import pandas as pd
from fuzzywuzzy import fuzz, process

# Read the CSV file with specified encoding
df = pd.read_csv('Datasets/cleaned.csv', encoding='utf-8')

# Function to clean and split skills
def clean_and_split_skills(skills):
    if pd.isna(skills):
        return []
    return [skill.strip().lower().replace('\u200b', '') for skill in skills.split(',')]

# Apply the function to the 'skills' column
df['skills'] = df['skills'].apply(clean_and_split_skills)

# Flatten the list of skills and get unique skills
all_skills = [skill for sublist in df['skills'] for skill in sublist]
unique_skills = list(set(all_skills))

# Function to group similar skills
def group_similar_skills(skills, threshold=80):
    grouped_skills = {}
    for skill in skills:
        match = process.extractOne(skill, grouped_skills.keys(), scorer=fuzz.token_sort_ratio)
        if match and match[1] >= threshold:
            grouped_skills[match[0]].append(skill)
        else:
            grouped_skills[skill] = [skill]
    return grouped_skills

# Group similar skills
grouped_skills = group_similar_skills(unique_skills)

# Debugging: Print grouped skills
print("Grouped Skills:")
for group, skills in grouped_skills.items():
    print(f"{group}: {skills}")

# Create a mapping from original skill to grouped skill
skill_mapping = {}
for group, skills in grouped_skills.items():
    for skill in skills:
        skill_mapping[skill] = group

# Apply the mapping to the 'skills' column
df['skills'] = df['skills'].apply(lambda skills: [skill_mapping[skill] for skill in skills])

# Save the processed DataFrame to a new CSV file with specified encoding and error handling
df.to_csv('Datasets/processed_cleaned.csv', index=False, encoding='utf-8', errors='ignore')