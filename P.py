f = open('words.txt')
fr = f.read()
lst = []

for i in fr:
    if i =='\n':
        lst.append(',')

    else:
        lst.append(i)

voc=(''.join(lst))
vocabulary=(voc.split(','))

Vocabulary=['head','heal','teal','tell','tall','tail']


def switch_f(str1, str2):
    if len(str1) != len(str2):
        return False

    count = 0

    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count =+ 1

    if count == 1:
        return True

    return False

switch_lst = []


def morph(Vocabulary, start, end, count):
    global switch_lst
    if count == 0:
        count =+ 1
        switch_lst = [start]

    if start == end:
        print (switch_lst)
        return switch_lst

    for i in Vocabulary:
        if switch_f(i, start) and i not in switch_lst:
            switch_lst.append(i)
            morph(Vocabulary, i, end, count)
        switch_lst[:-1]

    return None

Vocabulary = set(['head','heal','teal','tell','tall','tail'])
print (morph(Vocabulary, 'head', 'tail',0))
