n = 0
sum = 0
while True:
    print("Input number (or empty string to stop inputing)")
    x = input()
    if x == "":
        break
    x = float(x)
    sum += x
    n += 1
    if n == 1:
        min = x
        max = x
    else:
        if x < min:
            min = x
        if x > max:
            max = x

if n == 0:
    print("No numbers")
else:
    print("average", sum / n)
    print("min", min)
    print("max", max)
