x0 = 1
x1 = [0, 0, 0, 0, 1, 1, 1, 1]
x2 = [0, 0, 1, 1, 0, 0, 1, 1]
x3 = [0, 1, 0, 1, 0, 1, 0, 1]
t1 = [0, 0, 0, 0, 1, 1, 1, 1]
t2 = [0, 0, 1, 1, 0, 0, 1, 1]
w1 = [0, 0, 0, 0]
w2 = [0, 0, 0, 0]

y1 = 0
y2 = 0
e1 = 0
e2 = 0
repete = True
cont = 0
while repete:
    repete = False
    cont += 1
    for i in range(len(x1)):
        y1 = (w1[0]*1) + (w1[1]*x1[i]) + (w1[2]*x2[i]) + (w1[3]*x3[i])
        y2 = (w2[0]*1) + (w2[1]*x1[i]) + (w2[2]*x2[i]) + (w2[3]*x3[i])

        if (y1 > 0):
            y1 = 1
        else:
            y1 = 0
        if (y2 > 0):
            y2 = 1
        else:
            y2 = 0

        e1 = t1[i] - y1
        e2 = t2[i] - y2

        if(e1 != 0):
            w1[0] = w1[0] + (e1 * 1)
            w1[1] = w1[1] + (e1 * x1[i])
            w1[2] = w1[2] + (e1 * x2[i])
            w1[3] = w1[3] + (e1 * x3[i])
            repete = True

        if(e2 != 0):
            w2[0] = w2[0] + (e2 * 1)
            w2[1] = w2[1] + (e2 * x1[i])
            w2[2] = w2[2] + (e2 * x2[i])
            w2[3] = w2[3] + (e2 * x3[i])
            repete = True

        print("x1: ", str(w1[0])+str(w2[0]), "x2: ", str(w1[1])+str(w2[1]), "x3: ", str(w1[2])+str(w2[2]), "x4: ", str(w1[3])+str(w2[3]))
