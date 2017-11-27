print("variant:3")
res = []
print("input word")
buf = input()
while buf != "":
    res.append(buf)
    print("input word")
    buf = input()
with open("output.txt", "w", encoding="utf-8") as file:
    for i in range(len(res)):
        file.write(res[i][i + 1:] + "\n")
