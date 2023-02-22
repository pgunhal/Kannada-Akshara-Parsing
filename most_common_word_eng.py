# name = input("Enter file:")
# if len(name) < 1:
#     name = "test.txt"
import os
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rAyara_stOtra_padachEda.txt")
file = open(path)


#Finds the number of times each word appears in the file
nAma = dict()
for line in file:
    line = line.rstrip()
    line = line.lower()
    #print(transliterate(line, sanscript.ITRANS, sanscript.DEVANAGARI))
    #known errors in transliterate: does not work with 'R' and has trouble recognizing 'ah' sounds (ie. namah)
    print(line + transliterate(line, sanscript.ITRANS, sanscript.KANNADA))
    names = line.split()
    for word in names:
        nAma[word] = nAma.get(word, 0) + 1


#Finds the most common nAma and num times it occurs in the file
common_nAma = None
nAma_count = None
for name,count in list(nAma.items()):
    if nAma_count is None or count > nAma_count:
        common_nAma = name
        nAma_count = count

print('The most common syllable is:', common_nAma + " " + transliterate(common_nAma, sanscript.ITRANS, sanscript.KANNADA))
print('It appears', nAma_count, 'times')
