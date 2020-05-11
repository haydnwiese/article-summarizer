from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize


# Create a dictionary of word frequencies for words that are not stop words
def create_frequency_table(text_string) -> dict:
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freq_table = dict()
    for word in words:
        word = ps.stem(word)
        if word in stop_words:
            continue
        elif word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table


def generate_summary(text) -> str:
    # Create word frequency table
    freq_table = create_frequency_table(text)

    # Tokenize sentences
    sentences = sent_tokenize(text)
