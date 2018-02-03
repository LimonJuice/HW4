Nucleotides = 'TCGGATCATGGTTACCCTGA'

print('\nINSTRUCTIONS!' 
      '\n At every turn a Player may delete either one or two Nucleotides from the sequence.'
      '\n The Player who is left with a uni-nucleotide sequence of an arbitrary length '
      '\n (i.e., the sequence containing only one of 4 possible Nucleotides),'
      '\n loses the game.','\n')


print('Sequence of Nucleotides Inserted: ',Nucleotides)

#Requirements function defines the limit to play the game


def Requirements(seq):
    dic = {}
    adenine = 0
    thymine = 0
    guanine = 0
    cytosine = 0

    for i in seq:
        if i == 'A':          #converter of seq elements into 'requirements' points
            adenine += 1

        elif i == 'T':
            thymine += 1

        elif i == 'G':
            guanine += 1

        elif i == 'C':
            cytosine += 1


    dic['A'] = adenine
    dic['T'] = thymine
    dic['G'] = guanine
    dic['C'] = cytosine


    print(dic)
    h = 0
    for i in dic.values():
        if i == 1:
            h += 1
            continue

        else:
            h = 0

    if h == 4:
        print('Game Over')

    else:
        print('Ready to play!','Good Luck Have Fun')


Requirements(Nucleotides)


def Check(seq):
    l = len(seq)
    print('# of N:',l)

    if l % 4 == 3 and l > 4:
        print('Tip: Player can win by picking One Nucleotide')

    elif l % 4 == 1 and l > 4:
        print('Tip: Player can win by picking Two Nucleotides')

    elif l % 4 == 0 and l != 8 and l > 4:
        print('Tip: Player can pick either One or Two Nucleotides.')

    elif l < 4:
        print('# of Nucleotides not sufficient!')
        print ('Insert Nucleotides to Continue!')

    else:
        if l == 4 :
            print ('You Lose!')


Check(Nucleotides)



# schedule to follow in game phases


def Strategies(seq_size):
    for N_seq in range(seq_size, 4, -1):
        f_move = 1
        s_move = 2
        print('If the size of the sequence is:', N_seq)

        if N_seq % 4 == 1 and N_seq - 2 != 4 and N_seq != 7 and N_seq != 5:

            print('The Player on the turn deletes Two Nucleotides -> takes', s_move,'\n')
            # a Player can delete either two on one time or one on the other time

            if  N_seq % 2 == 0:
                N_seq -= 4

            else:
                N_seq -= 3

            continue

        elif N_seq - 2 == 4 and N_seq != 7:
            print('The Player on the turn deletes Two Nucleotides to win > takes', s_move)
            print('Now the size of the sequence is', N_seq - 2)
            print('So the other Player, on the next round, loses the game.','\n')

        elif N_seq - 1 == 4 and N_seq != 7:
            print('The Player on the turn deletes Two Nucleotides to win > takes', s_move)
            print('Now the size of the sequence is', N_seq - 1)
            print('So the other Player, on the next round, loses the game.','\n')

        elif N_seq % 4 == 3 and N_seq != 7:

            print('The Player on the turn deletes one Nucleotide > takes', f_move,'\n')
            # a Player can delete either two on one time or one on the other time
            if N_seq % 2 == 0:
                N_seq -= 3
            else:
                N_seq -= 4
            continue

        elif N_seq % 4 == 0:
            print('The Player on the turn is free to delete One or Two Nucleotides > takes', f_move, 'or', s_move)
            c = N_seq - 1
            c2 = N_seq - 2
            # the other Player can delete either two on one time or one on the other time

            if N_seq % 2 == 0:
                N_seq -= 4

        else:
            print('Careful Player 2, you have the chance to win by thinking in the right term')



Strategies(len(Nucleotides))