import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Step 1: Fetch the webpage
url = "https://www.tomsguide.com/opinion/lord-of-the-rings-the-rings-of-power-review"  # Replace with actual URL
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    # Step 2: Parse the webpage content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Step 3: Extract all text from the soup
    all_text = soup.get_text()

    # Step 4: Analyze the entire text using TextBlob for sentiment
    blob = TextBlob(all_text)
    print("Full page sentiment analysis:")
    print(f"Sentiment: {blob.sentiment}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


# Test urls:
# https://movieweb.com/what-makes-the-godfather-a-masterpiece/
# https://www.polygon.com/lotr-rings-of-power/452990/trop-episode-6-review-sauron-celebrimbor-numenor
# https://www.tomsguide.com/opinion/lord-of-the-rings-the-rings-of-power-review