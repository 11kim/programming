import random

def length(word):
    count = 0
    for i in word:
        if i.isalpha():
            count += 1
    return count


def file_reader_dict(filename):
    words_hints = {}
    with open(filename, 'r', encoding="utf-8") as file:
        file = file.readlines()
    for word_line in file:
        word_line = word_line.rstrip()
        if not word_line:
            break
        word_line = word_line.split(';')
        hints = []
        for i in range(1, len(word_line), 2):
            if not word_line[i]:
                break
            hints.append((word_line[i], word_line[i + 1], length(word_line[i])))
        words_hints[word_line[0]] = hints
    return words_hints


def file_reader_forms(filename):
    keys = {}
    with open(filename, 'r', encoding="utf-8") as file:
        file = file.readlines()
    for word_line in file:
        word_line = word_line.rstrip()
        forms = word_line.split()
        keys[forms[0]] = set(forms)
    return keys


def print_hint(hint):
    p_hint = hint[0]
    if hint[1] == '0':
        p_hint += ' ...'
    else:
        p_hint = '... ' + p_hint
    print('Подсказка:', p_hint)


def go_game(word, hint, key_forms):
    print('У вас есть', hint[2], 'попыток')
    print('Введите свой ответ')
    answer = input()
    for i in range(hint[2] - 1):
        if answer in key_forms[word]:
            print('Да, это оно')
            return
        print('Вы неправы. Попробуйте ещё')
        answer = input()
    print('Вы проиграли! Правильный ответ:', word)


def main():
    print("variant:3")
    words_hints = file_reader_dict('words_hints.csv')
    keys = list(words_hints.keys())
    key_forms = file_reader_forms('forms.csv')
    word = random.choice(keys)
    hint = random.choice(words_hints[word])
    print_hint(hint)
    go_game(word, hint, key_forms)


main()


