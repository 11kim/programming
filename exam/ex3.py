import os
import re

def find_coll(filename):
    with open('news/' + filename, 'r', encoding='windows-1251') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].rstrip()
            if line.startswith('<w><ana lex=') and line.endswith('</w>') and lines[i + 1].startswith('<w><ana lex='):
                next = lines[i + 1]
                word1 = re.findall('</ana>(.+)</w>', line)[0]
                word2 = re.findall('</ana>(.+)</w>', next)[0]
                gr1 = re.findall('gr="(.+)"', line)[0]
                gr2 = re.findall('gr="(.+)"', next)[0]
                if gr1[0] == 'S' and gr2[0] == 'S' and 'gen' in gr2:
                    make_file(word1 + ' ' + word2, '')
                    print(word1, word2)


def make_file(bi, ph):
    with open('bigramms.txt', 'a', encoding='utf-8') as file:
        file.write(bi + '\t' + ph)

def main():
    file_list = os.listdir('news')
    for file in file_list:
        bigs = find_coll(file)

main()