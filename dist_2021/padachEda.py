# shrI: gurubhyO nama:

import os
import re
#finds if a char is a 'vowel' in
#indic languages (swara)
def is_swara (c):
    vowel = ['ಅ', 'ಆ', 'ಇ', 'ಈ', 'ಉ', 'ಊ', 'ಋ' 'ೠ', 'ಎ', 'ಏ', 'ಐ', 'ಒ', 'ಓ', 'ಔ',
             '್', 'ಾ', 'ಿ', 'ೀ', 'ು', 'ೂ', 'ೃ', 'ೄ', 'ೆ', 'ೇ', 'ೈ', 'ೊ', 'ೋ', 'ೌ', 'ಂ', ':', 'ಂ']
    #KNOWN ISSUE: 'ಂ' is not properly recognized, so it ends up being placed w/ next letter. 
    # Ex: 'ದಿ', 'ಂದಾ' instead of 'ದಿಂ', 'ದಾ'
    #This is only w/ other kAguNita, so ಮಂಗಳ  will be ‘ಮಂ’, ‘ಗ’, ‘ಳ’
    for i in vowel:
        if i == c:
            return True
    return False

def is_vyanjana(c):
    vyanjana = ['ಕ', 'ಖ', 'ಗ', 'ಘ', 'ಙ', 'ಚ', 'ಛ', 'ಜ', 'ಝ', 'ಞ', 'ಟ', 'ಠ', 'ಡ', 'ಢ', 'ಣ', 'ತ', 'ಥ', 
             'ದ', 'ಧ', 'ನ', 'ಪ', 'ಫ', 'ಬ', 'ಭ', 'ಮ', 'ಯ', 'ರ', 'ಲ', 'ವ', 'ಶ', 'ಷ', 'ಸ', 'ಹ', 'ಳ']
    for i in vyanjana:
        if i == c:
            return True
    return False

def parse_words(input):
    words, aksharas = [], []
    # words.append(input.split(" "))
    # print(re.split(u' ', input))
    for i in range(0, len(re.split(u' ', input))): #words
        words.append(re.split(u' ', input)[i])

    #words has every single word in the line, '\n' are included, but not spaces
    
    index = 0 #index of prev vowel
    for word in words:
        index = 0
        for i in range(len(word)): #parsing through the words
            if is_vyanjana(word[i]):
                if i+1 < len(word) and is_swara(word[i+1]): #if the next char is a swara AND it is a valid index
                    aksharas.append(word[index:i+2])
                    index = i+2
                    i = index
                else: #else just add the letter 
                    aksharas.append(word[index:i+1])
                    index=i+1
    return aksharas

fn = input('Pick a file: ')
if len(fn) < 1:
    fn = 'vayustuti.txt'
path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), fn)
file = open(path, 'r',  encoding='utf8')

path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parsed_text.txt')
f1 = open(path, 'w',  encoding='utf8',)
parsed_words=[]
for line in file:
    temp = parse_words(line)
    for val in temp:
        parsed_words.append(val)
        val = val+','
        f1.write(val)
    f1.write('\n')
file.close()
f1.close()


#Finds the number of times each word appears in the file
nAma = dict()
for word in parsed_words:
        nAma[word] = nAma.get(word, 0) + 1


#Finds the most common nAma and num times it occurs in the file
common_nAma = None
nAma_count = None
for name,count in list(nAma.items()):
    if nAma_count is None or count > nAma_count:
        common_nAma = name
        nAma_count = count
        
print('Most common akshara: ', common_nAma, '\nCount: ', nAma_count)
print('Please check \'parsed_text.txt\' for the padachEda. ')