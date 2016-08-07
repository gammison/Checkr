import numpy as np
import os
from sklearn import svm
import CreateVector

def compare(filepath):
    targetVector = CreateVector.createVectorNoFile(filepath)
    print(targetVector)
    onlyfiles = [f for f in os.listdir("profiles")]
    X = []
    y = []
    for temp in onlyfiles:
        tfile = open('profiles/'+temp, 'r')
        print(tfile)
        y.append(tfile.readline())
        print(y)
        tomake = tfile.readline().split(",")
        print(tomake)
        for k in tomake:
            w = k.split(" ")
            X.append(w)
    clf = svm.SVC()


compare('text')
