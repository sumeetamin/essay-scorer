from flask import Flask, request, jsonify, render_template
import re
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load('essay_scoring_model.joblib')

# Data cleaning function
def clean_text(text):
    """
    Preprocesses the essay text by removing special characters,
    correcting common spelling mistakes, and normalizing the text.
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text, flags=re.I)  # Replace multiple spaces with a single space
    text = re.sub(r'\d', '', text)  # Remove digits
    return text

@app.route('/')
def index():
    # Serve the HTML page
    return render_template('index.html')

@app.route('/score', methods=['POST'])
def score_essay():
    data = request.json  # Get data from AJAX request
    essay = data['essay']
    cleaned_essay = clean_text(essay)
    
    # Use the model to predict the score
    score = model.predict([cleaned_essay])[0]
    
    # Return the score in JSON format
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(debug=True)
