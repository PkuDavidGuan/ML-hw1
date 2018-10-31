import argparse
from sklearn.neighbors import KNeighborsClassifier

from ..data import create


def main(args):
    x_train, x_valid, x_test, y_train, y_valid, y_test = create(
        args.dataset, args.data_path)
    paras = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,23,25]
    bestAcc = 0.0
    bestPara = 0
    for para in paras:
        clf = KNeighborsClassifier(n_neighbors=para, p=1)
        clf.fit(x_train, y_train)
        tmpAcc = clf.score(x_valid, y_valid)
        print("neigh = {}, Acc = {}".format(para, tmpAcc))
        if tmpAcc > bestAcc:
            bestAcc = tmpAcc
            bestPara = para
    print("choose {} as n_neighbors".format(bestPara))
    clf = KNeighborsClassifier(n_neighbors=bestPara, p=1)
    clf.fit(x_train, y_train)
    finalAcc = clf.score(x_test, y_test)
    print("Accuracy on test set: {}".format(finalAcc))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str)
    parser.add_argument('--data_path', type=str)
    main(parser.parse_args())
