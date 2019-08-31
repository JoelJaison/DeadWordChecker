from nltk import *
import re
with open('TestEssay.txt', mode =  'r', encoding = 'utf-8-sig') as file:
    essay = file.read()
    text = word_tokenize(essay.lstrip())

patterns = [\
("(is|was|were|are)", "lverb"), \
('\\b.+ing\\b', "GER")\
]
regexp_tagger = RegexpTagger(patterns)
speechparts = (regexp_tagger.tag(text))


print(speechparts)

deadwords = ['was', 'are', 'is']
for word in deadwords:
    count = len(re.findall('\\b%s\\b' % (word), essay))
    i = 0
    while i < count:

        matchlist = list()
        for matches in re.finditer('\\b%s\\b' % (word), essay):
            matchlist.append(matches)
            break
        if speechparts[(speechparts.index((word, 'lverb')))+1][1] == 'GER':
             essay = essay[:matchlist[0].start()] + 'replaced' + essay[matchlist[0].end():]
             speechparts.remove((word, 'lverb'))
        i += 1
print(essay)
