import os

import requests
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Step 1: Load the vague word list from the MIT URL
url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(url)
vague_words = set(response.text.splitlines())  # Use a set for faster lookups

# Step 2: Function to clean and normalize the text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    return words

# Step 3: Generate vague word ratio as a feature
def vague_word_ratio(text, vague_words):
    words = clean_text(text)
    total_words = len(words)
    
    if total_words == 0:
        return 0  # Return 0 if there are no words
    
    # Count vague words
    vague_count = sum(1 for word in words if word in vague_words)
    return vague_count / total_words

# Step 4: Load text data from a file
def load_data(file_path):
    with open(file_path, 'r') as f:
        texts = f.readlines()
    return [text.strip() for text in texts]

# Step 5: Add vague word ratio and classify using a machine learning model
def classify_texts_from_file(file_path):
    # Load the texts from the file
    texts = load_data(file_path)
    
    # Labels (if you have them in a separate file or manually set them)
    # Here, we manually create labels for the sake of example (vague = 1, not vague = 0)
    # In practice, you'd load or generate real labels for each line in the file
    labels = [1 if vague_word_ratio(text, vague_words) > 0.1 else 0 for text in texts]
    
    # Step 6: Feature extraction using TF-IDF and vague word ratio
    tfidf_vectorizer = TfidfVectorizer()
    
    # Convert texts to TF-IDF features
    tfidf_features = tfidf_vectorizer.fit_transform(texts)
    
    # Add vague word ratio as an additional feature
    vague_ratios = [vague_word_ratio(text, vague_words) for text in texts]
    
    # Combine TF-IDF features with vague word ratio
    combined_features = np.hstack((tfidf_features.toarray(), np.array(vague_ratios).reshape(-1, 1)))
    
    # Step 7: Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(combined_features, labels, test_size=0.2, random_state=42)
    
    # Step 8: Train a RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Step 9: Predict and evaluate the model
    y_pred = model.predict(X_test)
    
    # Evaluate model performance
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

# Example: Load data from a file and classify
os.getcwd()
n = 1000
for i in range(n):
    data_folder = os.path.join(os.getcwd(),'Final_Recommendation_Letters/Recommendation_Letters_of_ID_'+str(i))
    file_lst = os.walk(data_folder)
    for root, folders, files in file_lst:
        for file in files:
            path = os.path.join(root.file)
            classify_texts_from_file(path)
                