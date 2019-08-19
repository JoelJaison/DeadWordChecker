import re
import os
from processlist import process_list
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
for index in range(len(parlist)):
    for deadword in deadwordlist:
        parlist[index] = parlist[index].replace(" "+deadword+" ", "<span style='background-color:yellow'>%s</span>" % (" "+deadword+" "))  

with open("WordChecker.html","w") as file:
    for paragraph in parlist:
        file.write("<p>%s</p>\n" % paragraph)
os.system("google-chrome WordChecker.html")