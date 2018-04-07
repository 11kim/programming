import re


def symb_count(filename):
    with open(filename, "r", encoding = "utf-8") as file:
        text = file.read()
        i = text.find('<body>')
        j = text.find('</body>')
        count = 0
        if (i != -1) and (j != -1):
            count = j - i - 6
    return count


def print_count(s_count, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write('symbols count: ' + str(s_count) + '\n')


def find_all_grs(filename):
    grs = dict()
    with open(filename, "r", encoding = "utf-8") as file:
        for line in file:
            if ('w' in line) and ('gr' in line):
                gr = ''
                i = line.find('gr=') + 4
                while (i < len(line) and line[i] != '"'):
                    gr += line[i]
                    i += 1
                if gr in grs:
                    grs[gr] += 1
                else:
                    grs[gr] = 1
    return grs


def print_grs(grs, filename):
    grs_list = []
    for gr in grs:
        grs_list.append((grs[gr], gr))
    grs_list.sort()
    grs_list.reverse()
    grs_listik = []
    for i in grs_list:
        grs_listik.append(i[1])
    with open(filename, "a", encoding="utf-8") as file:
        for i in grs_listik:
            file.write(i + '\n')

def count_verbs(filename):
    count = 0
    with open(filename, "r", encoding = "utf-8") as file:
        for line in file:
            s1 = re.findall('gr=".*"', line)
            if s1:
                s1 = s1[0]
                s1 = s1[3:]
                if (s1[1] == 'V') and ('ед' in s1) and re.search('[/(,/| ]сов', line):
                    count += 1
                    print(line)
    return count

def print_v_count(count, filename):
    with open(filename, "w", encoding = "utf-8") as file:
        file.write(str(count))


def main():
    print('var: 2')
    filename = 'mystem.xml'
    res_filename = 'results.txt'
    s_count = symb_count(filename)
    print_count(s_count, res_filename)
    grs = dict()
    grs = find_all_grs(filename)
    print_grs(grs, res_filename)
    v_count = count_verbs(filename)
    res_filename = 'results2.txt'
    print_v_count(v_count, res_filename)

main()
