import random

a = ['active', 'ambient', 'angry']
b = ['bad', 'brawny', 'brilliant']
c = ['cunning', 'clever', 'casual']
d = ['dynamic', 'dumb']
e = ['empty', 'elegant']
f = ['foolish', 'frank']
g = ['goofy']
h = ['haughty', 'horsey']
i = ['intelligent', 'idealistic']
j = ['joker', 'jolly']
k = ['kind', 'knowledgebale']
l = ['lousy', 'lame']
m = ['mickey', 'maniac']
n = ['noisy', 'nocturnal']
o = ['optimistic', 'obedient']
p = ['practical', 'poshy']
q = ['queer', 'quaint', 'quick']
r = ['rockstar', 'rocky', 'rich']
s = ['speedy', 'super']
t = ['tiny', 'tidy']
u = ['untidy', 'uncommon', 'unique']
v = ['valiant', 'vengeful']
w = ['warmhearted', 'wealthy', 'weary']
x_list = ['xenophilic']
y = ['young', 'youthful', 'yeasty']
z = ['zazzy', 'zestful', 'zany']


def name_fun():
    name = input('Type your name:')
    name = name.lower()
    list_of_letters = list(name)
    charecteristics = {}
    for x in list_of_letters:
        if x == 'a':
            charecteristics[x] = random.choice(a)
        if x == 'b':
            charecteristics[x] = random.choice(b)
        if x == 'c':
            charecteristics[x] = random.choice(c)
        if x == 'd':
            charecteristics[x] = random.choice(d)
        if x == 'e':
            charecteristics[x] = random.choice(e)
        if x == 'f':
            charecteristics[x] = random.choice(f)
        if x == 'g':
            charecteristics[x] = random.choice(g)
        if x == 'h':
            charecteristics[x] = random.choice(h)
        if x == 'i':
            charecteristics[x] = random.choice(i)
        if x == 'j':
            charecteristics[x] = random.choice(j)
        if x == 'k':
            charecteristics[x] = random.choice(k)
        if x == 'l':
            charecteristics[x] = random.choice(l)
        if x == 'm':
            charecteristics[x] = random.choice(m)
        if x == 'n':
            charecteristics[x] = random.choice(n)
        if x == 'o':
            charecteristics[x] = random.choice(o)
        if x == 'p':
            charecteristics[x] = random.choice(p)
        if x == 'q':
            charecteristics[x] = random.choice(q)
        if x == 'r':
            charecteristics[x] = random.choice(r)
        if x == 's':
            charecteristics[x] = random.choice(s)
        if x == 't':
            charecteristics[x] = random.choice(t)
        if x == 'u':
            charecteristics[x] = random.choice(u)
        if x == 'v':
            charecteristics[x] = random.choice(v)
        if x == 'w':
            charecteristics[x] = random.choice(w)
        if x == 'x':
            charecteristics[x] = random.choice(x_list)
        if x == 'y':
            charecteristics[x] = random.choice(y)
        if x == 'z':
            charecteristics[x] = random.choice(z)
    for key, value in charecteristics.items():
        print('Your', key, 'stands for', value)
    # print('Remember this is just for fun. We are all kind and brilliant.')


name_fun()
