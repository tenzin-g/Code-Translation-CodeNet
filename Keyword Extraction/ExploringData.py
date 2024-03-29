#!pip install contractions
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import re, string, unicodedata                          # Import Regex, string and unicodedata.
import contractions                                     # Import contractions library.
from bs4 import BeautifulSoup                           # Import BeautifulSoup.

import numpy as np                                      # Import numpy.
import pandas as pd                                     # Import pandas.
import nltk                                             # Import Natural Language Tool-Kit.

nltk.download('stopwords')                              # Download Stopwords.
nltk.download('punkt')
nltk.download('wordnet')

from nltk.corpus import stopwords                       # Import stopwords.
from nltk.tokenize import word_tokenize, sent_tokenize  # Import Tokenizer.
from nltk.stem.wordnet import WordNetLemmatizer         # Import Lemmatizer.
import warnings
warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)
data=pd.read_csv('csvfiles/all_incidents.csv')
#save org data
data_org = data.copy()
 ##exploring the data 
data.shape

data.head()

data.dtypes

data.columns

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")                    
    return soup.get_text()

def replace_contractions(text):
    return contractions.fix(text)
 
lemmatizer = WordNetLemmatizer()
def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
       # print(word)
        new_word = word.lower()
      #  print(new_word)
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words
def lemmatize_list(words):
    new_words = []
    for word in words:
      new_words.append(lemmatizer.lemmatize(word, pos='v'))
    return new_words
    
def normalize(words):
   # words = remove_non_ascii(words)
    words = to_lowercase(words)
    #words = remove_punctuation(words)
    words = remove_stopwords(words)
   # words = lemmatize_list(words)
    return ' '.join(words)

print("done")   

import wordcloud
def show_wordcloud(text, title):
    stopwords = set(wordcloud.STOPWORDS)
    fig_wordcloud = wordcloud.WordCloud(stopwords=stopwords,background_color='white',
                    colormap='viridis', width=800, height=600).generate(text)
    plt.figure(figsize=(14,11), frameon=True)
    plt.imshow(fig_wordcloud)
    plt.axis('off')
    plt.title(title, fontsize=30)
    plt.show()

    root_cause_category_mapping = pd.read_csv('rootcause_csv_mapping_file.csv')

print(root_cause_category_mapping.shape)
data_pred =data_pred.merge(root_cause_category_mapping, on='rootcause')
data_pred.head()
