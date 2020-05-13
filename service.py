from bs4 import BeautifulSoup
import urllib.request as request
import re
from summarization import run_summarization


def create_summarization(article_url: str) -> (str, str):
    scraped_data = request.urlopen(article_url)
    article = scraped_data.read()

    parsed_article = BeautifulSoup(article, 'lxml')
    paragraphs = parsed_article.find_all('p')

    heading = parsed_article.find('h1').getText()

    article_text = ""
    for para in paragraphs:
        article_text += para.getText()

    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    return run_summarization(article_text), heading
