print("Input word or a phrase in English")
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
ss = input().split()
res = []
for s in ss:
    top = s[0] == s[0].upper()
    s = s.lower()
    buf = ""
    for i in range(len(s) - 1, -1, -1):
        if not s[i].isalpha():
            buf = s[i] + buf
        else:
            break
    s = s[:i + 1]

    ind = s[0] in vowels
    j = 0
    while s[0] not in vowels:
        s = s[1:] + s[0].lower()
        j += 1
        if j >= len(s):
            break

    if ind:
        s += "way"
    else:
        s += "ay"
    if top:
        s = s[0].upper() + s[1:]
    s += buf
    res.append(s)
print("Pig-latin version:", " ".join(res))
