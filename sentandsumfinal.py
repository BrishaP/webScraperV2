import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from transformers import pipeline

# Step 1: Fetch the webpage
url = "https://www.tomsguide.com/opinion/lord-of-the-rings-the-rings-of-power-review"  # Replace with actual URL
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    # Step 2: Parse the webpage content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Step 3: Extract all text from the soup
    all_text = soup.get_text()

    # Clean and preprocess the text
    clean_text = ' '.join(all_text.split())

    # Step 4: Load the summarization pipeline from Hugging Face
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")

    # Step 5: Split the text into smaller chunks
    max_chunk_length = 1024  # Maximum sequence length for the model
    chunks = [clean_text[i:i + max_chunk_length] for i in range(0, len(clean_text), max_chunk_length)]

    # Step 6: Summarize each chunk
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=20, do_sample=False, clean_up_tokenization_spaces=True)
        summaries.append(summary[0]['summary_text'])

    # Step 7: Combine and print the summarized text
    combined_summary = ' '.join(summaries)
    print("Summary:")
    print(combined_summary)

    # Step 8: Analyze the summary text using TextBlob for sentiment
    summary_blob = TextBlob(combined_summary)
    print("Summary sentiment analysis:")
    print(f"Sentiment: {summary_blob.sentiment}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")