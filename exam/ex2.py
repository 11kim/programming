import os
import re
import csv

def l_check(word):
    return not re.fullmatch('[XLVI]+', word)


def find_abbs(abb, filename):
    with open('news/' + filename, 'r', encoding='windows-1251') as file:
        text = file.read()
        forms = re.findall('lex="([А-ЯЁA-Z /-][А-ЯЁA-Z /-]+)"', text)
    for word in forms:
        if word in abb:
            abb[word] += 1
        elif l_check(word):
            abb[word] = 1
    return abb


def print_table(abb):
    with open('abbreviations.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        for word in abb:
            writer.writerow([word, abb[word]])

def main():
    abb = {}
    file_list = os.listdir('news')
    for file in file_list:
        abb = find_abbs(abb, file)
    print_table(abb)


main()
