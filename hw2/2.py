print("variant:3")
print("Input word")
s = input()
s = s[::-1]
s = s.replace("з", "")
s = s.replace("я", "")
print(s)
