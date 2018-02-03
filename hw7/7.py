def learn_file_name():
    print("input name of file")
    file_name = input()
    try:
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        file_name = -1
    return file_name


def word_cut(word):
    if word.endswith('s'):
        word = word[:-1]
    return word


def find_hoodwords(file_name):
    hoodwords = {}
    with open(file_name, "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word_cut(word)
                if word.endswith('hood'):
                    if word in hoodwords:
                        hoodwords[word] += 1
                    else:
                        hoodwords[word] = 1
    return hoodwords


def word_parent(word):
    word = word[:-4]
    if len(word) > 0 and word[-1] == 'i':
        word = word[:-1] + 'y'
    return word

def print_words(words):
    print('words parents:')
    for word in words:
        print(word_parent(word))

def print_min_frec(words):
    print('the rarest words:')
    frec = min(words.values())
    for word in words:
        if words[word] == frec:
            print(word)



def main():
    print("variant:3")
    file_name = learn_file_name()
    if file_name == -1:
        print("!incorrect file name")
        return
    hoodwords = find_hoodwords(file_name)
    #print(hoodwords)
    print('count:', len(hoodwords), '\n')
    print_min_frec(hoodwords)
    print()
    print_words(hoodwords)


main()

