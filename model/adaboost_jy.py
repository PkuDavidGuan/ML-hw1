import argparse
from tqdm import tqdm
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
import heapq
from ..data import create


def main(args):
  x_train, x_valid, x_test, y_train, y_valid, y_test = create(args.dataset, args.data_path)
  paras = [2,20,40,60,80,100,120,140,160,180,200]
  bestAcc = 0.0
  bestPara = 0
  for para in paras:
      clf = AdaBoostClassifier( n_estimators=para, learning_rate=0.1)
      clf.fit(x_train, y_train)
      tmpAcc = clf.score(x_valid, y_valid)
      print("n_estimators = {}, Acc = {}".format(para, tmpAcc))
      if tmpAcc > bestAcc:
          bestAcc = tmpAcc
          bestPara = para
  print("choose {} as n_neighbors".format(bestPara))
  clf = AdaBoostClassifier( n_estimators=bestPara, learning_rate=0.1)
  clf.fit(x_train, y_train)
  feaImportance = clf.feature_importances_
  feaIds = heapq.nlargest(2,range(4),feaImportance.take)
  print(feaIds)
  finalAcc = clf.score(x_test, y_test)
  print("Accuracy on test set: {}".format(finalAcc))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
  parser.add_argument('--dataset', type=str)
  parser.add_argument('--data_path', type=str)

  main(parser.parse_args())