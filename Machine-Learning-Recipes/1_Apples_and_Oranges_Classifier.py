# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 22:31:28 2016

@author: Kaya
"""
from sklearn import tree
features = [[140,1], [130,1], [150,0], [170,0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[150,0]])