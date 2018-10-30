import os
import numpy as np
from sklearn.model_selection import train_test_split


def parse(line):
    items = line.strip().split(',')
    label_dict = {'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2}
    x = items[:-1]
    x = [float(i) for i in x]
    y = items[-1]
    return x, y


def Iris(data_path):
    x_train, y_train, x_valid, y_valid, x_test, y_test = [], [], [], [], [], []
    raw_x = []
    raw_y = []
    rawFile = open(os.path.join(data_path, 'iris.data.txt'), 'r')
    for l in rawFile:
        tmpx, tmpy = parse(l)
        raw_x.append(tmpx)
        raw_y.append(tmpy)
    rawFile.close()
    x_train, x_rest, y_train, y_rest = train_test_split(
        raw_x, raw_y, train_size=0.7, random_state=2018)
    x_valid, y_valid, x_test, y_test = [], [], [], []
    for idx in range(len(x_rest)):
        if idx % 2 == 0:
            x_valid.append(x_rest[idx])
            y_valid.append(y_rest[idx])
        else:
            x_test.append(x_rest[idx])
            y_test.append(y_rest[idx])
    print(x_test[0])
    print("Train instances: {}\n".format(len(y_train)))
    print("Valid instances: {}\n".format(len(y_valid)))
    print("Test instances: {}\n".format(len(y_test)))
    return x_train, x_valid, x_test, y_train, y_valid, y_test