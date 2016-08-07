import numpy as np
import os
from sklearn import svm
class svmtest():
    def compare(filepath):
        onlyfiles = [f for f in os.listdir("profiles")]
        X = []  # X = [[0, 0], [1, 1], [2, 2]] #training samples of n samples, n features
        y = []  # [0, 1,2 ] # class labels of n samples
        for temp in onlyfiles:
            tfile = open('profiles/'+temp, 'r')
            y.append(tfile.readline())
            print(y)
            tomake = tfile.readline().split(",")
            print(tomake)
            for k in tomake:
                w = k.split(" ")
                X.append(w)
        clf = svm.SVC()


