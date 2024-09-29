import pandas as pd

# Step 1: Read the CSV file
csv_file_path = 'Datasets/rankings_rec.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Select specific columns
selected_columns = ['candidate id', 'position', 'recommenders', 'secore_5']
df_selected = df[selected_columns]

# Step 3: Convert the DataFrame to a JSON string
json_str = df_selected.to_json(orient='records')

# Step 4: Save the JSON string to a file
json_file_path = 'rankings_rec.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_str)