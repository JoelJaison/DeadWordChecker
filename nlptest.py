from nltk import *
with open('TestEssay.txt') as essay:
    text = word_tokenize(essay.read())

speechparts = pos_tag(text)
print(speechparts)