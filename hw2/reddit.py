import string
from zipfile import ZipFile
import json

def getkey(dict, value):
    for k, v in dict.items():
        if v == value:
            del dict[k]
            return k

zip_name = "RC_2005-12.zip"
file_name = "/JsonFolder/RC_2005-12"
dict = {}
top = {}
base = []
tab = str.maketrans('', '', string.punctuation)

for i in range(1, 6):
    zip_data = ZipFile(zip_name)
    zip_data.extractall('/JsonFolder')
    zip_data.close()

    with open(file_name, "r") as jsonfile:
        numb = 0
        for line in jsonfile:
            linepart = json.loads(line)
            comment = linepart['body'].translate(tab)
            base.append(comment.split())
            for wordnumb in range(0, len(base[numb])):
                if base[numb][wordnumb] not in dict.keys():
                    dict.update({base[numb][wordnumb]: 1})
                else:
                    dict[base[numb][wordnumb]] += 1
            numb += 1
    zip_name = "RC_2006-0" + str(i) + ".zip"
    file_name = "/JsonFolder/RC_2006-0" + str(i)

while len(top) <= 20:
    max_val = max(dict.values())
    word = getkey(dict, max_val)
    if len(word) > 3:
        top.update({word: max_val})
print(top)

with open("output.json", "w") as output:
    for k, v in top.items():
        output.write(str(k) + " -- " + str(v) + "\n")

