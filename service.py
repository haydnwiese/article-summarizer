from bs4 import BeautifulSoup
import urllib.request as request
import re
from summarization import run_summarization

scraped_data = request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scraped_data.read()

parsed_article = BeautifulSoup(article, 'lxml')
paragraphs = parsed_article.find_all('p')

article_text = ""
for para in paragraphs:
    article_text += para.getText()

# Removing Square Brackets and Extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

print(run_summarization(article_text))
