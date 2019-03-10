'''
Find top-20 most used words
'''
import string
from zipfile import ZipFile
import json
import os

def get_key(value):
    '''
    Find key in dictionary
    '''
    for key, cur_value in DICT.items():
        if cur_value == value:
            del DICT[key]
            return key

ZIP_NAME = "RC_2005-12.zip"
FILE_NAME = "/JsonFolder/RC_2005-12"
DICT = {}
TOP = {}
BASE = []
TAB = str.maketrans('', '', string.punctuation)

if not os.path.exists('/JsonFolder'):
    os.makedirs('/JsonFolder')

for i in range(1, 6):
    ZIP_DATA = ZipFile(ZIP_NAME)
    ZIP_DATA.extractall('/JsonFolder')
    ZIP_DATA.close()

    with open(FILE_NAME, "r") as jsonfile:
        numb = 0
        for line in jsonfile:
            linepart = json.loads(line)
            comment = linepart['body'].translate(TAB)
            BASE.append(comment.split())
            for wordnumb in range(0, len(BASE[numb])):
                if BASE[numb][wordnumb] not in DICT.keys():
                    DICT.update({BASE[numb][wordnumb]: 1})
                else:
                    DICT[BASE[numb][wordnumb]] += 1
            numb += 1
    ZIP_NAME = "RC_2006-0" + str(i) + ".zip"
    FILE_NAME = "/JsonFolder/RC_2006-0" + str(i)

while len(TOP) <= 20:
    MAX_VAL = max(DICT.values())
    WORD = get_key(MAX_VAL)
    if len(WORD) > 3:
        TOP.update({WORD: MAX_VAL})
print(TOP)

with open("output.json", "w") as output:
    json.dump(TOP, output)
