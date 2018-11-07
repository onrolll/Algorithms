def lcs(X,Y):
    m = len(X)
    n = len(Y)
    LS = [[0 for x in range(m+1)] for y in range(n+1)]
    #word = []
    #print(len(LS))
    #print(len(LS[0]))
    for i in range(m, -1, -1):
        #print('i->',i)
        for j in range(n, -1, -1):
            #print('j->',j)
            if i == m or j == n:
                #print("if i == m or j == n:")
                LS[j][i] = 0
            else:
                if X[i] == Y[j]:
                    #word.append(X[i])
                    LS[j][i] = 1 + LS[j+1][i+1]
                else:
                    choices = []
                    choices.append(LS[j+1][i]) # same as delete X[i]
                    choices.append(LS[j][i+1]) # same as insert Y[j] at X[i]
                    LS[j][i] = max(choices)

    #word = ''.join(word)
    #return word
    return LS[0][0]


if __name__ == '__main__':
    X = "HIERROGLYPHOLOGY"
    Y = "MICHAELANGELO"
    print(lcs(X,Y))
