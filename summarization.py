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


def score_sentences(sentences: list, freq_table: dict) -> dict:
    sentence_value = dict()

    for sentence in sentences:
        word_count_in_sentence = len(word_tokenize(sentence))
        for word_value in freq_table:
            if word_value in sentence.lower():
                if sentence[:10] in sentence_value:
                    sentence_value[sentence[:10]] += freq_table[word_value]
                else:
                    sentence_value[sentence[:10]] = freq_table[word_value]

        # Divide by number of words in sentence to ensure longer sentences do not have advantage
        sentence_value[sentence[:10]] = sentence_value[sentence[:10]] // word_count_in_sentence

    return sentence_value


def find_average_score(sentence_value: dict) -> int:
    sum_values = 0
    for value in sentence_value.values():
        sum_values += value

    # Average value of a sentence from original text
    average = int(sum_values / len(sentence_value))

    return average


def generate_summary(text) -> str:
    # Create word frequency table
    freq_table = create_frequency_table(text)

    # Tokenize sentences
    sentences = sent_tokenize(text)
