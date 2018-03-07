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

def built_re(flexes):
    reg = '(?:'
    for flex in flexes:
        reg += '(?:' + flex + ')' + '|'
    reg = reg[:-1]
    reg += ')'
    return reg

def find_parts(line):
    flex_hard = {"ый", "ого", "ому", "ым", "ом", "ое", "ая", "ой", "ую"}
    flex_pal = {"ий", "его", "ему", "им", "ем", "ее", "яя", "ей", "юю"}
    hard = built_re(flex_hard)
    pal = built_re(flex_pal)
    perf = '(?:(?:программируем)|(?:программированн))' + hard
    act = '(?:(?:программирующ)|(?:программировавш))' + pal + '(?:ся)?'
    part = re.findall(perf, line)
    part += re.findall(act, line)
    return part

def adder(forms, words):
    for word in words:
        if word:
            forms.add(word)
    return forms

def cleaner(word):
    if len(word) == 0:
        return
    if not word[0].isalpha():
        word = word[1:]
    if not word[-1].isalpa():
        word = word[:-1]
    return word

def find_forms(file_name):
    forms = set()
    with open(file_name, "r", encoding = "utf-8") as file:
        for line in file:
            line = line.lower()
            verbs = re.findall(r'(?:программиру(?:(?:(?:ю|(?:ете))(?:сь)?)|(?:(?:(?:ешь)|(?:ет)|(?:ют)|(?:ем))(?:ся))))|(?:программирова((?:л[аои](?:ся)?)|(?:(?:(?:ть)|л)(?:ся)?)))', line)
            gerund = re.findall(r'программируя(?:сь)?', line)
            part = find_parts(line)
            forms = adder(forms, verbs)
            forms = adder(forms, gerund)
            forms = adder(forms, part)
    return forms


def main():
    print("variant:3")
    print("Введите название файла")
    file_name = learn_file_name()
    if file_name == -1:
        print("!incorrect file name")
        return
    forms = find_forms(file_name)
    print(forms)
    for form in forms:
        print(form)

main()