import re

def replace(file_in, file_out):
    fout = open(file_out, 'w', encoding="utf-8")
    with open(file_in, 'r', encoding="utf-8") as fin:
        for line in fin:
            line = re.sub('([ ">«\(])язык((?:а|у|е|и|(?:ом)|(?:ов)|(?:ам)|(?:ами)|(?:ах))?[ ,"<\)»])', r'\1шашлык\2', line)
            line = re.sub('([ ">«\(])Язык((?:а|у|е|и|(?:ом)|(?:ов)|(?:ам)|(?:ами)|(?:ах))?[ ,"<\)»])', r'\1Шашлык\2', line)
            fout.write(line)
    fout.close()



print("variant:3")
filename = 'Лингвистика.html'
out_filename = 'Result.txt'
replace(filename, out_filename)
