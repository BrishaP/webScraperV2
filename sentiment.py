# import requests
# from bs4 import BeautifulSoup
# from textblob import TextBlob

# # Step 1: Fetch the webpage
# url = "https://example.com/blog"  # Replace with actual URL
# response = requests.get(url)

# if response.status_code == 200:
#     html_content = response.text

#     # Step 2: Parse the webpage content
#     soup = BeautifulSoup(html_content, 'html.parser')
#     comments = soup.find_all('p')  # Assuming comments are inside <p> tags

#     # Step 3: Analyze sentiment of each comment
#     for comment in comments:
#         text = comment.get_text()
#         blob = TextBlob(text)
#         print(f"Comment: {text}")
#         print(f"Sentiment: {blob.sentiment}")
#         print("-----")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")



# import requests
# from bs4 import BeautifulSoup
# from textblob import TextBlob

# # Step 1: Fetch the webpage
# url = "https://movieweb.com/what-makes-the-godfather-a-masterpiece/"  # Replace with actual URL
# response = requests.get(url)

# if response.status_code == 200:
#     html_content = response.text

#     # Step 2: Parse the webpage content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Step 3: Extract all text from the soup
#     all_text = soup.get_text()

#     # Step 4: Analyze the entire text using TextBlob for sentiment
#     blob = TextBlob(all_text)
#     print("Full page sentiment analysis:")
#     print(f"Sentiment: {blob.sentiment}")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

# import requests
# from bs4 import BeautifulSoup
# from textblob import TextBlob

# # Step 1: Fetch the webpage
# url = "https://collider.com/game-of-thrones-ending-bad-explained/"  # Replace with actual URL
# response = requests.get(url)

# if response.status_code == 200:
#     html_content = response.text

# # consolelog a random heading just to demo that the web scraper works

#     # Step 2: Parse the webpage content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Attempt to find the main content
#     main_content = soup.find('article')  # Common tag for main content
#     if not main_content:
#         main_content = soup.find('div', {'class': 'main-content'})  # Example class name
#     if not main_content:
#         main_content = soup.find('div', {'id': 'content'})  # Example id

#     if main_content:
#         text = main_content.get_text()
#         blob = TextBlob(text)
#         print("Full page sentiment analysis:")
#         print(f"Sentiment: {blob.sentiment}")
#     else:
#         print("Main content not found.")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")



# Range: -1.0 to 1.0
# Meaning:
# Negative values (closer to -1.0): Indicate negative sentiment.
# Positive values (closer to 1.0): Indicate positive sentiment.
# Zero: Indicates neutral sentiment.
# Subjectivity
# Range: 0.0 to 1.0
# Meaning:
# Values closer to 0.0: Indicate more objective statements.
# Values closer to 1.0: Indicate more subjective statements.
    


import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Step 1: Fetch the webpage
url = "https://movieweb.com/what-makes-the-godfather-a-masterpiece/"  # Replace with actual URL
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    # Step 2: Parse the webpage content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Step 3: Extract text from the specific div class
    article_body = soup.select_one('#article-body > div.content-block-regular')
    if article_body:
        text = article_body.get_text()
        
        # Step 4: Analyze the extracted text using TextBlob for sentiment
        blob = TextBlob(text)
        print("Article body sentiment analysis:")
        print(f"Sentiment: {blob.sentiment}")
    else:
        print("Specified div not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")