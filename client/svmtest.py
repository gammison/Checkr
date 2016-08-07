import numpy as np
import os
from sklearn import svm
import CreateVector









def compare(filepath):
    targetVector = CreateVector.createVectorNoFile(filepath)

    onlyfiles = [f for f in os.listdir("profiles")]
    print(onlyfiles)
    X = []
    y = []
    for temp in onlyfiles:
        tfile = open('profiles/'+temp, 'r')

        y.append(tfile.readline())

        sets = tfile.readline().split('\n')


        for k in sets:
            k = k.split(',')
            print(k)
            w = []
            for n in k:
                if n.isnumeric():
                    w.append(int(n))

            X.append(w)

    clf = svm.SVC()
    print(targetVector)
    print(X, len(X))
    print(y, len(y))

compare('AlbertCamusThePlague.txt')
