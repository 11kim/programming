import re

fin = open("Ozhegov.txt", "r", encoding="utf-8")
a = fin.readlines()

print("Task1")
for i in a:
    word = i[:i.find("|")]
    if len(word) > 20:
        print(word)

print("\nTask 2")
count = 0
for i in a:
    j1 = i[i.find("|") + 1:].find("|") + (i.find("|") + 1)
    j2 = i.rfind("|")
    if (j2 > j1 + 1):
        print(i[j1 + 1:j2])


print("\nTask 3")

dic = dict()
for i in a:
    s = i.split("|")
    dic[s[0]] = (s[1], s[2], s[3][:s[3].find("\n")])

while True:
    print("Input word")
    word = input()
    if word == "":
        break
    if not word in dic:
        print("no word")
    else:
        print(word + "-" + dic[word][2] + "-" + dic[word][0])

fin.close()
