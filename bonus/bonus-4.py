print("Введите слово или фразу на русском языке")
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
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
        if letter in vowels:
            res += 'с' + letter
    if top:
        res = res[0].upper() + res[1:]
    res += buf
    ans.append(res)
print("Кирпичный язык:", " ".join(ans))
