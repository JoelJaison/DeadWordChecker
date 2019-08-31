import re
def process_string(wordlist, finalstring):
    worddict = dict()
    for word in wordlist:
            templist = re.findall("\\b%s\\b" % word, finalstring)
            if len(templist)>0:
                    worddict[word] = len(templist)
   

    return worddict
