import re
import os
from dead_word_counter import deadwordlist, linkverblist
from processlist import process_list
"""

Will split the text file into paragraphs, replace dead words with appropriate html tags,
and write the contents into an html file which will be displayed in Google Chrome along
with an html file containing the number of counts of each word

"""

textfile = input("Enter File Name")
with open(textfile+".txt") as langessay:
    data = langessay.read()
startwordlist = None
with open("StartWords.txt") as starts:
    for line in starts:
        startwordlist = line.split(" ")
startwordlist = process_list(startwordlist)
"""
deadwordlist = None
linkverblist = None
with open("DeadWordList.txt") as dwordlist:
    for line in dwordlist:
        deadwordlist = line.split(" ")

with open("LinkingVerbs.txt") as lverblist:
    for line in lverblist:
        linkverblist = line.split(" ")
linkverblist = process_list(linkverblist)

deadwordlist = process_list(deadwordlist)
"""
paragraphs = data.split("\n")
parlist = list()
for paragraph in paragraphs:
    if(re.search('[a-zA-Z]', paragraph)):
        parlist.append(paragraph)
for index in range(len(parlist)):
    for deadword in deadwordlist:
        parlist[index] = parlist[index].replace(deadword, "<span style='background-color:yellow'>%s</span>" % deadword)  
    for linkverb in linkverblist:
        parlist[index] = parlist[index].replace(linkverb, "<span style='background-color:yellow'>%s</span>" % linkverb)
    for startword in startwordlist:
        parlist[index] = parlist[index].replace(startword, "<span style = 'background-color:yellow'>%s</span>" % startword)
with open("WordChecker.html","w") as file:
    for paragraph in parlist:
        file.write("<p>%s</p>\n" % paragraph)
os.system("google-chrome WordChecker.html")