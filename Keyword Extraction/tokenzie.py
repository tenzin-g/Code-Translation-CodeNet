#in command line:
    #pip install nltk
    #python -m nltk.downloader popular
#now ready to run!

import nltk
import csv
#switch out with whatever txt file you have
file_content = open("pythonKeywordTest.txt").read()
tokens = nltk.word_tokenize(file_content)
print (tokens)

# data to be written row-wise in csv file
data = tokens

# opening the csv file in 'w+' mode
file = open('test.csv', 'w+', newline ='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(data)
