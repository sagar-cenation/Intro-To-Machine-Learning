#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.svm import SVC

# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

# Optimize C Parameter
"""
for i in range(1, 5):
    c = 10**i
    print "C=" + str(c)
    clf = SVC(kernel="rbf", C=c)

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time() - t0, 3), "s"

    t1 = time()
    pred = clf.predict(features_test)
    print "predicting time:", round(time() - t1, 3), "s"

    print clf.score(features_test, labels_test)
"""

# Optimized rbf kernel
clf = SVC(kernel="rbf", C=10000)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time() - t1, 3), "s"

print clf.score(features_test, labels_test)

# Extracting Predictions from an SVM
for i in [10, 26, 50]:
    print pred[i]

# How Many Chris(1) Emails Predicted?
# print sum(pred) or
chris_mails = 0
for y in pred:
    if y == 1:
        chris_mails += 1
print chris_mails


#########################################################
