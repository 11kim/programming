import random

def rand_choose(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        a = file.readlines()
        #word = random.randint(0, len(a) - 1)
        word = round(random.random() * (len(a) - 1))
        word = a[word]
        word = word.rstrip()
    return word

def cap(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

def make_phrase(words):
    return " ".join(words)

def co_verb(verb, gen):
    if gen == 'm':
        return verb
    end = ''
    if verb[-2:] == 'ся':
        end = 'сь'
        verb = verb[:-2]
    if gen == 'f':
        verb += 'а'
    else:
        verb += 'о'
    return verb + end

def co_adj_nom(adj, gen):
    if gen == 'm':
        return adj
    adj = adj[:-2]
    if gen == 'f':
        return adj + 'ая'
    else:
        return adj + 'ое'


def imper():
    verb = rand_choose("imper_verbs.txt") + random.choice(("", "те"))
    intro = rand_choose("imper_intro.txt")
    obj, gen = rand_choose("imper_obj.txt").split()
    def_pros = {'f': 'той', 'm': 'том', 'n':'том'}
    def_pro = random.choice(("", "э")) + def_pros[gen]
    prep = "o" + def_pro.startswith("э") * "б"
    return make_phrase((cap(verb), intro, prep, def_pro, obj)) + '!'

def quest():
    subj = rand_choose("quest_subj.txt").split()[0]
    verb = rand_choose("quest_verbs.txt")
    inf = rand_choose("quest_inf.txt")
    obj, gen = rand_choose("quest_obj.txt").split()
    def_pros = {'f': 'ту', 'm': 'того'}
    def_pro = random.choice(('', 'э')) + def_pros[gen]
    return make_phrase((cap(subj), verb, inf, def_pro, obj)) + '?'

def cond():
    subj, gen = rand_choose("quest_subj.txt").split()
    verb = co_verb(rand_choose("cond_verbs.txt"), gen)
    adv = rand_choose("cond_advs.txt")
    return make_phrase((cap(subj), verb, 'бы', adv)) + '.'

def neg():
    subj, gen = rand_choose("neg_subj.txt").split()
    adj = co_adj_nom(rand_choose("neg_adj.txt"), gen)
    verb = co_verb(rand_choose("neg_verbs.txt"), gen)
    obj = rand_choose("quest_obj.txt").split()[0]
    return make_phrase((cap(adj), subj, 'не', verb, obj)) + '.'

def ind():
    subj, gen = rand_choose("neg_subj.txt").split()
    adj = co_adj_nom(rand_choose("neg_adj.txt"), gen)
    verb = co_verb(rand_choose("neg_verbs.txt"), gen)
    obj = rand_choose("quest_obj.txt").split()[0]
    return make_phrase((cap(adj), subj, verb, obj)) + '.'

def main():
    res = [imper(), quest(), cond(), neg(), ind()]
    random.shuffle(res)
    for i in res:
        print(i)


main()