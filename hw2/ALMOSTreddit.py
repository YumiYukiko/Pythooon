from zipfile import *
import json

def getkey(dict, value):
    for k, v in dict.items():
        if v == value:
            del dict[k]
            return k

zip_name = "C:/Users/Юми/Desktop/Учёба/PYTHON COURSES/reddit/RC_2005-12.zip"
file_name = "C:/Users/Юми/Desktop/Учёба/PYTHON COURSES/reddit/JsonFolder/RC_2005-12"
letters = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
dict = {}
top = {}
base = []

for i in range(1,6):
    zip_data = ZipFile(zip_name)
    zip_data.extractall('C:/Users/Юми/Desktop/Учёба/PYTHON COURSES/reddit/JsonFolder')
    zip_data.close()

    with open(file_name, "r") as jsonfile:
        numb = 0
        for line in jsonfile:
            linepart = json.loads(line) 
            base.append(linepart['body'])
            base[numb] = ''.join(s for s in linepart['body'] if s in letters)
            base[numb] = base[numb].split()
            for wordnumb in range(0,len(base[numb])):
                if base[numb][wordnumb] not in dict.keys():
                    dict.update({base[numb][wordnumb]: 1})
                else:
                    dict[base[numb][wordnumb]] += 1
            numb+=1
    #print('\n\n',dict)
    zip_name = "C:/Users/Юми/Desktop/Учёба/PYTHON COURSES/reddit/RC_2006-0" + str(i) + ".zip"
    file_name = "C:/Users/Юми/Desktop/Учёба/PYTHON COURSES/reddit/JsonFolder/RC_2006-0" + str(i)
        

while len(top) <= 20:
    max_val = max(dict.values())
    word = getkey(dict,max_val)
    if len(word) > 3:
        top.update({word:max_val})
print(top)

with open("C:/Users/Юми/Desktop/Учёба/PYTHON COURSES/reddit/output.json", "w") as output:
    for k,v in top.items():
        output.write(str(k) + " -- " + str(v) + "\n")
