from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import os

path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mangalAcharaNa_saMdhi.txt")
file = open(path, encoding='utf8')

data = '''a aa i I u U o au am k kh g gh ch Ch j jh t
th d dh N T Th D Dh p ph b bh y r l v s sh Sh
h L kSha'''


for line in file:
    line = line.rstrip()
    #line = line.lower()
    names = list(line)
    # print(len(names))
    # if len(names) > 0:
    print(names)
    # print(transliterate(line, sanscript.ITRANS, sanscript.DEVANAGARI))
    # print(transliterate(line, sanscript.ITRANS, sanscript.KANNADA))