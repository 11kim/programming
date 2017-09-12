a = input()
if not a.isdigit():
    print("not int")
else:
    print("The previous number is " + str(int(a) - 1))
    print("The next one is " + str(int(a) + 1))
