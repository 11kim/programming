print("variant:3")
print("Input word")
s = input()
for i in range(len(s)):
    print(s)
    s = s[1:] + s[0]
