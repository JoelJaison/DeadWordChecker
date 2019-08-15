import smtplib
from email.message import EmailMessage
import string
from processlist import process_list
from process_string import process_string


def dict_to_string(dictlist):
    dict1 = dictlist[0]
    dict2 = dictlist[1]
    string = ""
    for keys in dict1:
        string +=  "dead word: %s        count: %d\n" % (keys, dict1[keys])
    for keys in dict2:
        string += "linking verb: %s         count: %d\n" % (keys, dict2[keys])
    return string






deadwordlist = None
linkverblist = None
with open("DeadWordList.txt") as dwordlist:
    for line in dwordlist:
        deadwordlist = line.split(" ")

with open("LinkingVerbs.txt") as lverblist:
    for line in lverblist:
        linkverblist = line.split(" ")
deadwordlist = process_list(deadwordlist)
linkverblist = process_list(linkverblist)
linelist = []
with open("TestEssay.txt") as langessay:
    newpunct = list(string.punctuation)
    newpunct.remove("'")
    newpunct = "".join(newpunct)

    for line in langessay:
        line = line.rstrip()
        linelist.append(line.translate(str.maketrans(newpunct, len(newpunct)*",")).replace(",",""))
finalstring = " ".join(linelist).lower()

deadcountlist = process_string(deadwordlist, finalstring)
linkcountlist = process_string(linkverblist, finalstring)
countstring = dict_to_string([deadcountlist, linkcountlist])
print(countstring)

#with open("Counts.txt", "w+") as countfile:
 #   countfile.write(countstring)
  #  msg = EmailMessage()
   # msg.set_content(countfile.read())
#msg['Subject'] = "Lang Essay Word Count"
#msg['From'] = "joeljaison13@gmail.com"
#msg['To'] = "joeljaison13@gmail.com"
#s = smtplib.SMTP('localhost')
#s.send_message(msg)
#s.quit()
    

