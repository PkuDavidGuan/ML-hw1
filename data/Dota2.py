import os


def parse(line):
    items = line.strip().split(',')
    x = [int(i) for i in items[1:]]
    y = int(items[0])
    return x, y


def Dota2(data_path):
    x_train, y_train, x_valid, y_valid, x_test, y_test = [], [], [], [], [], []
    trainFile = open(os.path.join(data_path, 'dota2Train.csv'), 'r')
    for l in trainFile:
        x, y = parse(l)
        x_train.append(x)
        y_train.append(y)
    trainFile.close()
    testFile = open(os.path.join(data_path, 'dota2Test.csv'), 'r')
    idx = 0
    for l in testFile:
        x, y = parse(l)
        idx += 1
        if idx % 2 == 0:
            x_valid.append(x)
            y_valid.append(y)
        else:
            x_test.append(x)
            y_test.append(y)
    testFile.close()
    print("Train instances: {}\n".format(len(y_train)))
    print("Valid instances: {}\n".format(len(y_valid)))
    print("Test instances: {}\n".format(len(y_test)))
    return x_train, x_valid, x_test, y_train, y_valid, y_test
