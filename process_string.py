def process_string(wordlist, finalstring):
    worddict = dict()
    stringlist = finalstring.split(" ")
    for word in wordlist:
        while word in stringlist:
            worddict[word] = worddict.get(word,0) + 1
            stringlist.remove(word)

    return worddict
