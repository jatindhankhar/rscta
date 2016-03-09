import nltk
import codecs
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+') # Tokenizer with regex to remove punctuation marks

input_file = codecs.open("file.txt") # Replace with the file
input_data = input_file.read()

tokens = tokenizer.tokenize(input_data)

fd = nltk.FreqDist(tokens)

fd.plot(30,cumulative=False) # Plots a non cumulative graph for 30 common words
