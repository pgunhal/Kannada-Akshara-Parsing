# shrI: gurubhyO nama:
#author: pranav gunhal
#rev: 02 (2/20/23) fixed most known bugs, published 
#rev: 01 (5/10/21) main algorithm works, some bugs


#main class. if run, will prompt for a file to read and parse
#file should be in kannada, and free of unwanted symbols (i.e. '||', '1.', etc.)
#will output the most common akshara to the console, and will output the parsed file to '/input_file_path/parsed_text.txt

import os
import re
#finds if a char is a 'vowel' in
#indic languages (swara)
def is_swara (c):
    vowel = ['ಅ', 'ಆ', 'ಇ', 'ಈ', 'ಉ', 'ಊ', 'ಋ' 'ೠ', 'ಎ', 'ಏ', 'ಐ', 'ಒ', 'ಓ', 'ಔ',
             '್', 'ಾ', 'ಿ', 'ೀ', 'ು', 'ೂ', 'ೃ', 'ೄ', 'ೆ', 'ೇ', 'ೈ', 'ೊ', 'ೋ', 'ೌ', 'ಂ', ':', 'ಂ']
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
                    if i+2 < len(word) and word[i+2] == 'ಂ': #addresses bug with kAguNita before aM
                        #i.e. ಪಾಂತು is now ಪಾಂ, ತು instead of ಪಾ, ಂತು
                        aksharas.append(word[index:i+3])
                        index = i+3
                        continue
                    aksharas.append(word[index:i+2])
                    index = i+2
                    i = index
                else: #else just add the letter 
                    aksharas.append(word[index:i+1])
                    index=i+1
            elif is_swara(word[i]) and i+1 < len(word) and is_vyanjana(word[i+1]) and len(word[index:i+1]) == 1:
                    #addresses bug of words/lines starting with swara
                    #i.e. ಅಸ್ಯ is now ಅ,ಸ್,ಯ instead of ಅಸ್,ಯ
                    aksharas.append(word[index:i+1])
                    index = i+1
    return aksharas

fn = input('Pick a file: ')
if len(fn) < 1:
    fn = 'text/vayustuti_kan.txt'
path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), fn)
file = open(path, 'r',  encoding='utf8')

path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parsed_text.txt')
f1 = open(path, 'w',  encoding='utf8',)
parsed_words=[]
for line in file:
    temp = parse_words(line)
    for val in temp:
        parsed_words.append(val)
        val = val.replace('ಽ', 'ಅ,') #fix for bug w/ avagraha (ರಾಮೋಽಸ್ತಿ becomes ರಾ,ಮೋ,ಅ,ಸ್ತಿ instead of ರಾ,ಮೋ,ಽಸ್ತಿ)
        #TODO: this does not remove the samdhi formed to use avagraha, so padacheda is slightly innacurate here
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