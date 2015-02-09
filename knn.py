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
lengthOutcome = 11831
trainingSize = (lengthOutcome/4)*3

def classify(Xi,yi,testData):
    print("finshed importing data")
    from sklearn import neighbors
    neigh = neighbors.KNeighborsRegressor(3)
    neigh.fit(Xi, yi)
    squaredErrorSum = 0.0;
    for test in testData:
        'get classification'
        classification = neigh.predict(test[1:len(test)-1])
        classification = float(classification[0])
        'compare to actual'
        'sum squared errors'
        actual = float(test[len(test)-1])
        squaredError = pow((classification - actual),2)
        squaredErrorSum = squaredErrorSum + squaredError

    meanSquaredError = squaredErrorSum/lengthOutcome;
    print(meanSquaredError)

def main():
    testData = []
    with open("outcome.csv") as csvfile:
        levelOne = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in levelOne:
            row = map(float, row)
            'Load Training Data'
            if count<=trainingSize:
                X.append(row[1:len(row)-1])
                y.append(row[len(row)-1])
                count = count+1
            elif(trainingSize<count and count<lengthOutcome):
                testData.append(row)
                count = count+1
        classify(X,y,testData)

main()






