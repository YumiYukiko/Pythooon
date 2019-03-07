
def ADD(word1,word2):
    if word1 not in synonyms.keys():
        synonyms[word1] = set()
    if word2 not in synonyms.keys():
        synonyms[word2] = set()
    synonyms[word1].add(word2)
    synonyms[word2].add(word1)

def COUNT(word):
    if word not in synonyms.keys():
        return 0
    else:
        return len(synonyms[word])

def CHECK(word1,word2):
    if word1 not in synonyms.keys() or word2 not in synonyms.keys():
        return "NO"
    if word1 in synonyms[word2]:
        return "YES"
    else:
         return "NO"

synonyms = {}
commands = []
n = int(input())

for i in range(0,n):
    command = str(input()).lower().split()
    commands.append(command)

for command in commands:
    if command[0] == "add":
        ADD(command[1],command[2])
    elif command[0] == "count":
        print(str(COUNT(command[1])))
    else:
        print(CHECK(command[1],command[2]))
