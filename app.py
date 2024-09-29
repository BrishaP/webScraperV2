from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from transformers import pipeline

# initialises Flask application
app = Flask(__name__)

# Hugging Face summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")

# Defines home route '/' 
@app.route('/')
def home():
    return render_template('index.html')

# Handles post request (takes frontend input URL and return summarised content and sentiment analysis)
@app.route('/scrape', methods=['POST'])
def scrape():
# Extracts data from incoming POST request (URL)
    data = request.get_json()  # Get the URL from the user request
    url = data.get('url')

    # Step 1: Fetch the webpage
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to retrieve the page."}), 400

    html_content = response.text

    # Step 2: Parse the webpage content
    # Scrapes and cleans webpage content
    soup = BeautifulSoup(html_content, 'html.parser')
    all_text = soup.get_text()

    # Clean and preprocess the text
    clean_text = ' '.join(all_text.split())

    # Step 3: Summarize the text
    # Huggimg face summarising content in chunks
    max_chunk_length = 1024  # Hugging Face model max length
    chunks = [clean_text[i:i + max_chunk_length] for i in range(0, len(clean_text), max_chunk_length)]
    summaries = [summarizer(chunk, max_length=150, min_length=20, do_sample=False)[0]['summary_text'] for chunk in chunks]
    combined_summary = ' '.join(summaries)

    # Step 4: Analyze the summary text using TextBlob for sentiment
    summary_blob = TextBlob(combined_summary)
    sentiment = summary_blob.sentiment

    return jsonify({
        "summary": combined_summary,
        "sentiment": {
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity
        }
    })

# Starts Flask application in debug mode ( auto-reload when changes are made )
if __name__ == '__main__':
    app.run(debug=True)
