import smtplib
from email.message import EmailMessage
import string
from processlist import process_list
from process_string import process_string


def dict_to_string(dict1):

    string = ""
    for keys in dict1:
        string +=  "dead word: %s        count: %d\n" % (keys, dict1[keys])
    return string




def counter(filename):
    deadwordlist = None
    linkverblist = None
    with open("DeadWordList.txt") as dwordlist:
        for line in dwordlist:
            deadwordlist = line.split(" ")

    deadwordlist = process_list(deadwordlist)
    linelist = []
    with open(filename+".txt") as langessay:
        newpunct = list(string.punctuation)
        newpunct.remove("'")
        newpunct = "".join(newpunct)
        for line in langessay:
            line = line.rstrip()
            linelist.append(line.translate(str.maketrans(newpunct, len(newpunct)*",")).replace(",",""))
    finalstring = " ".join(linelist)
    deadcountlist = process_string(deadwordlist, finalstring)
    return [dict_to_string(deadcountlist), deadcountlist]
    


