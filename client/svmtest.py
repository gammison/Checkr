import numpy as np
import os
from sklearn import svm

onlyfiles=[f for f in os.listdir("\\profiles")]
for temp in onlyfiles:
    tfile = open(temp,'r')
    tfile.readline()
    tfile.readline()
    X.app
X=[]#X = [[0, 0], [1, 1], [2, 2]] #training samples of n samples, n features
y = #[0, 1,2 ] # class labels of n samples
clf = svm.SVC()
print(clf.fit(X, y))
print(clf.predict([[0,1]])) #predict what arry in the training samples this data set is closest to in this case label 1
print(clf.support_vectors_) # get support vectors, which are a subset of the training data
print(clf.support_) # get indices of the support vectors
print(clf.n_support_)# the number of support vectors for each class
