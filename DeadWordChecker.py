import tkinter as tk
import nltk
import re


words = "about-how off-of a-lot always and-so-on and-etc. anything bad because ‘cause could-of ‘cuz due-to etc forever get getting good be got gotten had-of here-are here-is I-believe I-think in-conclusion in-my-opinion just kind-of like lottsa major majorly might-of never nice nothing ok pretty really should-of shows shows-that so something somewhat sorta sort-of so-yeah stuff talks-about are talks-about-how talks-about-why there-are there-is thing ‘til ‘till to-me try-and very would-of you yours appear appears appeared becomes became feel feels felt grow grows grew keep keeps kept look looks looked prove proves proved remain remains remained resemble resembles resembled seem seems seemed smell smells smelled sound sounds everything sounded stay stays stayed taste tastes tasted turn turns turned am is was were been being become And But Finally First However Second I-am-going-to-be-writing-about In-conclusion Then Though Well"
wordlist = [word.replace('-', " ") if '-' in word else word for word in words.split()]

#set default geometry 
window = tk.Tk()
window.title('DeadWordChecker')
window.geometry('1900x800')
window.columnconfigure(0, weight=1, minsize=100)
window.rowconfigure([i for i in range(3)], weight=1, minsize=100)

frame1 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=6, padx=10, pady=10)
frame1.grid(row=0, column=0, sticky='nesw')

frame2 = tk.Frame(master=window, borderwidth=6, padx=10, pady=10)
frame2.grid(row=1, column=0, sticky='nesw')

header = tk.Label(master=frame1, text='Dead Word Checker') #change font
header.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

inp = tk.Text(master=frame2, padx=10, pady=10)
inp.insert('1.0', 'Enter text here!')
inp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
inp.tag_configure("highlight", background="yellow")

wordcount = tk.Text(master=frame2, padx=10, pady=10)
wordcount.insert('1.0', "Word counts will be displayed here!")
wordcount["state"] = "disabled"
wordcount.pack(side=tk.LEFT, fill=tk.Y)

frame3 = tk.Frame(master=window, borderwidth=6, padx=10, pady=10)
frame3.grid(row=2, column=0)

def erase():
    wordcount["state"] = "normal"
    inp.delete('1.0', tk.END)
    wordcount.delete('1.0', tk.END)
    wordcount["state"] = "disabled"

def extract_chunk(newpos, param):
    newstr = re.sub("\\(\\'%s\\', \\'VB.\\'\\)" % param, "('%s', '%s')" % (param, param), newpos)
    tups = re.findall(r"\(\'.+?\', \'.+?\'\)", newstr)
    newtags = [eval(tup) for tup in tups]
    chunkGram = "Chunk:{<%s><RB>*<VBG>}" % param
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(newtags)
    chunks = []
    for child in chunked:
        if isinstance(child, nltk.tree.Tree):
            chunks.append(" ".join([x for x, y in child.leaves()]))
    return chunks





def checkwords():
    data = inp.get('1.0', tk.END).split('\n')
    counts = {}
    for index in range(len(data)):
        
        if data[index]:
            tokenize = nltk.word_tokenize(data[index])
            newpos = str(nltk.pos_tag(tokenize)) 
            for word in wordlist:
                count = 0
                if word in ['is', 'are', 'were', 'was', 'am']:
                    i = 0
                    chunks = extract_chunk(newpos, word)
                    for match in re.finditer("\\b%s\\b" % word, data[index]):
                        loc = match.span()
                        if not chunks:
                            inp.tag_add("highlight", "%d.%d" % (index+1, loc[0]), "%d.%d" % (index+1, loc[1]))
                            count+=1
                        elif data[index][loc[0]:loc[0]+len(chunks[i])] != chunks[i]:
                            inp.tag_add("highlight", "%d.%d" % (index+1, loc[0]), "%d.%d" % (index+1, loc[1]))
                            count+=1
                        else:
                            if i < len(chunks)-1:
                                 i+=1
                            
                else:
                    for match in re.finditer("\\b%s\\b" % word, data[index]):
                        loc = match.span()
                        inp.tag_add("highlight", "%d.%d" % (index+1, loc[0]), "%d.%d" % (index+1, loc[1]))
                        count+=1

                counts[word] = counts.get(word, 0) + count
    wordcount["state"] = "normal"
    wordcount.delete('1.0', tk.END)
    total = 0
    for key, value in counts.items():
        if value:
            wordcount.insert(tk.END, "\nWord: %s, Count: %d" % (key, value))
            total+=value
    wordcount.insert(tk.END, "\nTotal Words: %d" % (total))
    wordcount["state"] = "disabled"



clear = tk.Button(master=frame3, text="Clear", command=erase, padx=10, pady=10)
clear.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)

check = tk.Button(master=frame3, text="Check Text", padx=10, pady=10, command=checkwords)
check.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)

window.mainloop()



