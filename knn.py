__author__ = 'ChristopherChan'
# for each row in data.csv
    # for each row in numberofgalaxies.csv
        #count the number of occurrences of haloID
    # add number of occurences into the row field [last column]

import csv
import sklearn
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
X = []
y = []
with open("outcome.csv") as csvfile:
    levelOne = csv.reader(csvfile, delimiter=',')
    for row in levelOne:
        count = 0
        endIndex = len(row)-1
        row = map(float, row)
        X.append(row[1:endIndex])
        y.append(row[endIndex])


print("finshed importing data")
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=30)
neigh.fit(X, y)
print(neigh.predict([33809.0,3382.295,0.23306856,301.99652,5.52761,-6.9788985,-4.086555]))

