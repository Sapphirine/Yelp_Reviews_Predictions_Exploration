import csv
import string
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import nltk
from nltk import word_tokenize
from nltk.util import bigrams, trigrams
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter

# nltk.download("stopwords")
# nltk.download('punkt')
# nltk.download('wordnet')

POSITIVE_WORDS = set([line.strip() for line in open('../stopwords/positive-words.txt', 'r')])
NEGATIVE_WORDS = set([line.strip() for line in open('../stopwords/negative-words.txt', 'r')])
NLTK_STOPWORDS = set(stopwords.words('english'))
MORE_STOPWORDS = set([line.strip() for line in open('../stopwords/more_stopwords.txt', 'r')])


def remove_numbers_in_string(s):
    return s.translate(None, string.digits)


def lowercase_remove_punctuation(s):
    s = s.lower()
    s = s.translate(None, string.punctuation)
    return s


def remove_stopwords(s):
    token_list = nltk.word_tokenize(s)
    exclude_stopwords = lambda token: token not in NLTK_STOPWORDS
    return ' '.join(filter(exclude_stopwords, token_list))


def filter_out_more_stopwords(token_list):
    return filter(lambda tok: tok not in MORE_STOPWORDS, token_list)


def stem_token_list(token_list):
    STEMMER = PorterStemmer()
    return [STEMMER.stem(tok.decode('utf-8')) for tok in token_list]


def restring_tokens(token_list):
    return ' '.join(token_list)


def lowercase_remove_punctuation_and_numbers_and_tokenize_and_filter_more_stopwords_and_stem_and_restring(s):
    s = remove_numbers_in_string(s)
    s = lowercase_remove_punctuation(s)
    s = remove_stopwords(s)
    token_list = nltk.word_tokenize(s)
    token_list = filter_out_more_stopwords(token_list)
    # token_list = stem_token_list(token_list)
    wnl = WordNetLemmatizer()
    token_list = [wnl.lemmatize(i) for i in token_list]
    return token_list

# -----------------------------------------------------------------------------------------------------------------

src_name = ['../review-star/uk-review-5.txt',
            '../review-star/uk-review-4.txt',
            '../review-star/uk-review-3.txt',
            '../review-star/uk-review-2.txt',
            '../review-star/uk-review-1.txt',
            '../review-star/usa-review-5.txt',
            '../review-star/usa-review-4.txt',
            '../review-star/usa-review-3.txt',
            '../review-star/usa-review-2.txt',
            '../review-star/usa-review-1.txt',
            '../review-star/ger-review-5.txt',
            '../review-star/ger-review-4.txt',
            '../review-star/ger-review-3.txt',
            '../review-star/ger-review-2.txt',
            '../review-star/ger-review-1.txt',
            '../review-star/can-review-5.txt',
            '../review-star/can-review-4.txt',
            '../review-star/can-review-3.txt',
            '../review-star/can-review-2.txt',
            '../review-star/can-review-1.txt']

des_name = ['../review_new/uk-review-5.csv',
            '../review_new/uk-review-4.csv',
            '../review_new/uk-review-3.csv',
            '../review_new/uk-review-2.csv',
            '../review_new/uk-review-1.csv',
            '../review_new/usa-review-5.csv',
            '../review_new/usa-review-4.csv',
            '../review_new/usa-review-3.csv',
            '../review_new/usa-review-2.csv',
            '../review_new/usa-review-1.csv',
            '../review_new/ger-review-5.csv',
            '../review_new/ger-review-4.csv',
            '../review_new/ger-review-3.csv',
            '../review_new/ger-review-2.csv',
            '../review_new/ger-review-1.csv',
            '../review_new/can-review-5.csv',
            '../review_new/can-review-4.csv',
            '../review_new/can-review-3.csv',
            '../review_new/can-review-2.csv',
            '../review_new/can-review-1.csv']
for i in range(20):
    text = open(src_name[i]).read()
    str = lowercase_remove_punctuation_and_numbers_and_tokenize_and_filter_more_stopwords_and_stem_and_restring(text)
    bi = list(bigrams(str))
    bigram = []
    for line in bi:
        bigram.append(line[0] + ' ' + line[1])

    dic = nltk.FreqDist(w for w in bigram)

    f = open(des_name[i], 'wb+')
    x = csv.writer(f)
    x.writerow(['word', 'freq'])
    for key, value in dic.items():
        x.writerow([key, value])
    f.close()