import re
import os
from processlist import *
from dead_word_counter import counter
"""

Will split the text file into paragraphs, replace dead words with appropriate html tags,
and write the contents into an html file which will be displayed in Google Chrome along
with an html file containing the number of counts of each word

"""

textfile = input("Enter File Name")
with open(textfile+".txt") as langessay:
    data = langessay.read()
deadwordlist = None
with open("DeadWordList.txt") as dwords:
    for line in dwords:
        deadwordlist = line.split(" ")
deadwordlist = process_list(deadwordlist)

paragraphs = data.split("\n")
parlist = list()
for paragraph in paragraphs:
    if(re.search('[a-zA-Z]', paragraph)):
        parlist.append(paragraph)
deadwordlist[0] = "about how"
for index in range(len(parlist)):
    for deadword in deadwordlist:
        parlist[index] = parlist[index].replace(" "+deadword+" ", " <span style='background-color:yellow'>%s</span> " % (" "+deadword+" "))  
        parlist[index] = parlist[index].replace(" "+deadword+".", " <span style='background-color:yellow'>%s</span> " % (" "+deadword+"."))  

with open("WordChecker.html","w") as file:
    countstring = counter(textfile)
    total = (sum(countstring[1].values()))
    countlist = countstring[0].split("\n")
    countlist.append("Total dead words: %d" % (total))
    for paragraph in parlist:
        file.write("<p style = 'line-height:2;text-indent:50px;'>%s</p>\n" % paragraph)
    for string in countlist:
        file.write("<p style = 'line-height:2;text-indent:50px;'>%s</p>\n" % string)
os.system("google-chrome WordChecker.html")