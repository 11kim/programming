import re

def learn_file_name():
    print("input name of file")
    file_name = input()
    try:
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        file_name = -1
    return file_name


def learn_year(filename):
    with open(filename, 'r', encoding = "utf-8") as file:
        flag = False
        year = -1
        for line in file:
            if flag:
                year = re.findall('title="([0-9]+) год"', line)
                if not year:
                    year = re.findall('title="([0-9]+)"', line)
                if year:
                    year = year[-1]
                break
            if '>Год основания<' in line:
                flag = True
    return year


def learn_name(filename):
    with open(filename, 'r', encoding = "utf-8") as file:
        for line in file:
            if line.startswith('<title>'):
                name = re.findall('<title>([А-ЯЁа-яё \-\.]+) +— Википедия</title>', line)
                if name:
                    name = name[0]
                else:
                    name = -1
                break
    return name

def create_file(year, name):
    #print(name, year)
    fout = open('informatio.txt', 'w', encoding = "utf-8")
    if year == -1:
        year = 'неизвестен'
    if name == -1:
        fout.write(str(year))
        return
    fout.write(name + ': ' + str(year))
    fout.close()



def main():
    print("variant:3")
    filename = learn_file_name()
    if filename == -1:
        print("!incorrect file name")
        return
    year = learn_year(filename)
    name = learn_name(filename)
    create_file(year, name)

main()