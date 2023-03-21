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
