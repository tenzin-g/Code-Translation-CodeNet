#in command line:
    #pip install nltk
    #python -m nltk.downloader popular
#now ready to run!

import nltk
#switch out with whatever txt file you have
file_content = open("pythonKeywordTest.txt").read()
tokens = nltk.word_tokenize(file_content)
print (tokens)
