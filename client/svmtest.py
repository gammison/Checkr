import numpy as np
import os
import CreateVector
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
        print(clf.fit(X, y))
        #print(clf.predict(
         #   CreateVector.createVector(filepath))  # predict what arry in the training samples this data set is closest to in this case label 1
        #print(clf.support_vectors_)  # get support vectors, which are a subset of the training data
        #print(clf.support_)  # get indices of the support vectors
        #print(clf.n_support_)  # the number of support vectors for each class
        return clf.predict(CreateVector.createVector(filepath))
