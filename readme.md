# Web Scraper with Sentiment Analysis

This project is a web application that allows users to input a URL, scrape the content of the webpage, summarize it, and perform sentiment analysis on the summarized text.

## Features

- Web scraping of user-provided URLs
- Text summarization using Hugging Face's transformers library
- Sentiment analysis using TextBlob
- Simple web interface for easy interaction

## Technologies Used

- Python
- Flask
- BeautifulSoup4
- TextBlob
- Hugging Face Transformers
- HTML/JavaScript

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/web-scraper-sentiment-analysis.git
   cd web-scraper-sentiment-analysis
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`

3. Enter a URL in the input field and click "Scrape" to analyze the webpage.

## Usage

1. Enter a valid URL into the input field on the home page.
2. Click the "Scrape" button to initiate the analysis.
3. Wait for the results to be displayed, including a summary of the page content and sentiment analysis.

## API Endpoint

The application provides a `/scrape` endpoint that accepts POST requests with a JSON body containing a `url` field. For example:

POST http://127.0.0.1:5000/scrape
Content-Type: application/json
{
"url": "https://www.example.com"
}


The response will include a summary of the page content and sentiment analysis results.

## Testing

To run the unit tests:

python -m unittest test_app.py

