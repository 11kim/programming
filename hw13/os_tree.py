import os

def maxi(d):
    maxs = 0
    for key in d:
        if d[key] > maxs:
            maxs = d[key]
            maxi = key
    return maxi

print('variant: 3')
res = {}
for root, dirs, files in os.walk('.'):
    print(files)
    for file in files:
        if '.' in file:
            type = file.split('.')[-1]
            if type in res:
                res[type] += 1
            else:
                res[type] = 1

print(maxi(res))