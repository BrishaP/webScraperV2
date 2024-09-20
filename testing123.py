# import requests
# from bs4 import BeautifulSoup
# from textblob import TextBlob

# # Step 1: Fetch the webpage
# url = "https://collider.com/game-of-thrones-ending-bad-explained/"  # Replace with actual URL
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

# # 

# import requests
# from bs4 import BeautifulSoup
# from textblob import TextBlob
# from gensim.summarization import summarize

# # Step 1: Fetch the webpage
# url = "https://collider.com/game-of-thrones-ending-bad-explained/"  # Replace with actual URL
# response = requests.get(url)

# if response.status_code == 200:
#     html_content = response.text

#     # Step 2: Parse the webpage content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Step 3: Extract all text from the webpage
#     all_text = soup.get_text()

#     # Step 4: Analyze the entire text using TextBlob for sentiment
#     blob = TextBlob(all_text)
#     print("Full page sentiment analysis:")
#     print(f"Sentiment: {blob.sentiment}")

#     from sumy.parsers.plaintext import PlaintextParser
#     from sumy.nlp.tokenizers import Tokenizer
#     from sumy.summarizers.lsa import LsaSummarizer
    
#     # Step 5: Summarize the text using Sumy
#     try:
#         parser = PlaintextParser.from_string(all_text, Tokenizer("english"))
#         summarizer = LsaSummarizer()
#         summary = summarizer(parser.document, 5)  # Summarize to 5 sentences
#         print("Summary of the page content:")
#         for sentence in summary:
#             print(sentence)
#     except ValueError:
#         print("Text is too short to summarize.")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
