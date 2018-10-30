import argparse
from tqdm import tqdm
from sklearn.naive_bayes import GaussianNB, MultinomialNB
import heapq
from ..data import create


def main(args):
  x_train, x_valid, x_test, y_train, y_valid, y_test = create(
        args.dataset, args.data_path)
  gnb = GaussianNB()
  gnb.fit(x_train, y_train)
  '''
  Codes annotated below are for analysis.
  '''
  print("Class Prior: {}".format(gnb.class_prior_))
  print("Class Prior: {}".format(gnb.class_count_))
  results = gnb.theta_
  print(results)
  # negative = results[0]
  # postive = results[1]
  # print(list(zip(negative,postive)))
  # negIds = set(heapq.nlargest(10,range(18),negative.take))
  # posiIds = set(heapq.nlargest(10,range(18),postive.take))
  # print(negIds)
  # print(posiIds)

  finalAcc = gnb.score(x_test, y_test)
  print("Accuracy on test set: {}".format(finalAcc))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--dataset', type=str)
  parser.add_argument('--data_path', type=str)

  main(parser.parse_args())
