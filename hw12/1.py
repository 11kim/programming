import os

def is_kir(s):
    flag = True
    for symb in s:
        if not (symb.isspace() or symb == 'ё' or symb == 'Ё' or ('а' <= symb and symb <= 'я') or ('А' <= symb and symb <= 'Я')):
            flag = False
            break
    return flag


print("Variant: 3")
file_list = os.listdir()
print(file_list)
dir_kir = 0
for file in file_list:
    if os.path.isdir(file) and is_kir(file):
        dir_kir += 1
    print(file)
print("count:", dir_kir)




