#print('Je kan dit niffo!')

def computegrade() :
    sc = input ('Enter score between 0.0 to 1.0: ')
    sc = float(sc)

    if sc >= 1.0:
        print('Bad score')
        quit()

    if sc >= 0.9:
        print('A')
    elif sc >= 0.8:
        print('B')
    elif sc >= 0.6:
        print('C')
    elif sc < 0.6:
        print('F')

computegrade()
computegrade()
computegrade()
