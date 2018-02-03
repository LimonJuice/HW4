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


Vocabulary=['head','heal','teal','sdasd','tefa','tea']


def switch_f(str1, str2):
    count = 0
    if len(str1) == len(str2):
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                count =+ 1


    elif len(str1) >= len(str2):
        for j in range(0, len(str1) - 1):
            if str1[j] != str2[j]:
                break

        delet= str2[:j]+str1[j]+str2[j:]
        if delet==str1 or str1[1:]==str2 or str1[:-1]==str2:
            count =+1

    elif len(str1) <= len(str2):
        for y in range(0, len(str2) - 1):
            if str2[y] != str1[y] :
                break
        #here I printed an index of the deleted character
        # print(str1[a])
        delet= str1[:y]+str2[y]+str1[y:]
        if delet==str2 or str2[1:]==str1 or str2[:-1]==str1:
            count =+1


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


    for word in Vocabulary:
        if switch_f(word, start) and word not in switch_lst:
            switch_lst.append(word)

            '''Here we need a recursion to update the current found word from the dictionary
            to be compared with the rest of other word in the dictionary. So we did it
            recursively!'''

            morph(Vocabulary, word, end, count)
            #thinking recursively

            switch_lst[:-1]

    return None

Vocabulary = set(['head','heal','teal','sdasd','tefa','tea'])
print (morph(Vocabulary, 'head', 'tea',0))
