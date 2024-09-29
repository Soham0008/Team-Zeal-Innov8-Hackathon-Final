import pandas as pd

# Step 1: Read the CSV file
csv_file_path = r'Datasets\final_dataset_ranked_ordered (1).csv'
df = pd.read_csv(csv_file_path)

# Step 2: Rename the 'Unnamed: 0' column to 'candidate_id'
df.rename(columns={'Unnamed: 0': 'candidate_id'}, inplace=True)

# Step 3: Select specific columns
selected_columns = ['candidate_id', 'name', 'score_5']
df_selected = df[selected_columns]

# Step 4: Add a 'rank' column in increasing order
df_selected['rank'] = range(1, len(df_selected) + 1)

# Step 5: Convert the DataFrame to a JSON string
json_str = df_selected.to_json(orient='records')

# Step 6: Save the JSON string to a file
json_file_path = 'Datasets/final.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_str)