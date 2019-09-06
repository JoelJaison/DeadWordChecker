import re
import os
from nltk import *
"""

Will split the text file into paragraphs, replace dead words with appropriate html tags,
and write the contents into an html file which will be displayed in Google Chrome along
with an html file containing the number of counts of each word

"""
def process_list(list):
    for i in range(len(list)):
        if "-" in list[i]:
            list[i] = list[i].replace("-", " ")
    return list

textfile = input("Enter File Name")
countdict = dict()
with open(textfile+".txt", mode = 'r', encoding = 'utf-8-sig') as langessay:
    data = langessay.read()

deadwordlist = None

with open("DeadWordList.txt", mode = 'r', encoding = 'utf-8-sig') as dwords:
    for line in dwords:
        deadwordlist = line.split(" ")

deadwordlist = process_list(deadwordlist)

paragraphs = data.split("\n")
parlist = list()

for paragraph in paragraphs:
    if(re.search('[a-zA-Z]', paragraph)):
        parlist.append(paragraph)


#Replaces all instances of dead words with highlighted html tag
#Also uses NLP to check if participle is in front of linking verb
for index in range(len(parlist)):
    text = word_tokenize(parlist[index])
    patterns = [\
    ("\\b(is|was|were|are)\\b", "lverb"), \
    ('\\b.+ing\\b', "GER")\
    ]
    regexp_tagger = RegexpTagger(patterns)
    speechparts = (regexp_tagger.tag(text))

    for deadword in deadwordlist:
        if deadword in ['is', 'are', 'were', 'was']:
            count = len(re.findall('\\b%s\\b' % (deadword), parlist[index]))
            i = 0
            
            while i < count:
                matchlist = list()
                for matches in re.finditer('\\b%s\\b' % (deadword), parlist[index]):
                    matchlist.append(matches)
                    
                if speechparts[(speechparts.index((deadword, 'lverb')))+1][1] != 'GER':
                    parlist[index] = parlist[index][:matchlist[i].start()] + ("<span style='\
                    background-color:yellow'>%s</span>" % (deadword)) + parlist[index][matchlist[i].end():]
                    countdict[deadword] = countdict.get(deadword, 0) + 1
                speechparts.remove((deadword, 'lverb'))
                i += 1
        
        
        
        else:
            parlist[index] = re.sub("\\b%s\\b" % deadword, "<span style='background-color:yellow'>%s</span>" % (deadword), parlist[index])
            countdict[deadword] = countdict.get(deadword, 0) + len(re.findall('\\b%s\\b' % deadword, parlist[index]))  
            
with open("WordChecker.html","w") as file:
    total = (sum(countdict.values()))
    for paragraph in parlist:
        file.write("<p style = 'line-height:2;text-indent:50px;'>%s</p>\n" % paragraph)
    for key in countdict:
        if not countdict[key] == 0:
            file.write("<p style = 'line-height:2;text-indent:50px;'>dead word: %s; count: %d</p>\n" % (key, countdict[key]))
    file.write("<p style = 'line-height:2;text-indent:50px;'>total dead words: %d</p>\n" % total)
os.system("google-chrome WordChecker.html")
