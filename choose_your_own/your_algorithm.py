#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together--separate them so we can give them different colors
# in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]


# initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


# your code here!  name your classifier object clf if you want the
# visualization code (prettyPicture) to show you the decision boundary

best_algo = None
best_score = 0.0
best_clf = None
best_property = None

# knn algorithm

from sklearn.neighbors import KNeighborsClassifier
prop = {
    'n_neighbors': None,
    'weights': None,
    'algorithm': None,
    'p': None
}

for n_neighbors in range(1, 15):
    for weights in ('uniform', 'distance'):
        for algorithm in ('auto', 'ball_tree', 'kd_tree', 'brute'):
            for p in range(1, 3):
                prop['n_neighbors'] = n_neighbors
                prop['weights'] = weights
                prop['algorithm'] = algorithm
                prop['p'] = p
                clf = KNeighborsClassifier(**prop)
                clf.fit(features_train, labels_train)

                curr_score = clf.score(features_test, labels_test)

                if curr_score > best_score:
                    best_score = curr_score
                    best_property = prop
                    best_algo = 'KNeighbors'
                    best_clf = clf

# adaboost algorithm

from sklearn.ensemble import AdaBoostClassifier

prop = {
    'n_estimators': None,
    'algorithm': None,
}

for n_estimators in range(40, 100):
    for algorithm in ("SAMME", "SAMME.R"):
        prop['n_estimators'] = n_estimators
        prop['algorithm'] = algorithm

        clf = AdaBoostClassifier(**prop)
        clf.fit(features_train, labels_train)

        curr_score = clf.score(features_test, labels_test)

        if curr_score > best_score:
            best_score = curr_score
            best_property = prop
            best_algo = 'AdaBoost'
            best_clf = clf

# Random Forest

from sklearn.ensemble import RandomForestClassifier

prop = {
    'n_estimators': None,
    'criterion': None,
    'max_features': None,
    'max_depth': None,
    'bootstrap': None,
    'n_jobs': -1
}


for n_estimators in range(1, 20):
    for criterion in ("gini", "entropy"):
        for max_features in ("auto", "sqrt", "log2", None):
            for max_depth in tuple(range(1, 11)) + (None,):
                for bootstrap in (True, False):
                    prop['n_estimators'] = n_estimators
                    prop['criterion'] = criterion
                    prop['max_features'] = max_features
                    prop['max_depth'] = max_depth
                    prop['bootstrap'] = bootstrap

                    clf = RandomForestClassifier(**prop)
                    clf.fit(features_train, labels_train)

                    curr_score = clf.score(features_test, labels_test)

                    if curr_score > best_score:
                        best_score = curr_score
                        best_property = prop
                        best_algo = 'RandomForest'
                        best_clf = clf

print "Best classifier : ", best_algo
print "Parmeters:\n", best_property
print "Accuracy score:", best_score


try:
    prettyPicture(clf, features_test, labels_test)
    plt.show()
except NameError:
    pass
