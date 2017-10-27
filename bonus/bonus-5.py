print("Input word or a phrase in English")
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
ss = input().split()
ans = []
for s in ss:
    res = ""
    top = s[0] == s[0].upper()
    s = s.lower()
    buf = ""
    for i in range(len(s) - 1, -1, -1):
        if not s[i].isalpha():
            buf = s[i] + buf
        else:
            break
    s = s[:i + 1]

    for letter in s:
        res += letter
        if (letter not in vowels) and (letter.isalpha()):
            res += "aig"
    res += buf
    if top:
        res = res[0].upper() + res[1:]
    ans.append(res)
print("Aigy Paigy:", " ".join(ans))
