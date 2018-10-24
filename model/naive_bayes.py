import argparse
from sklearn.naive_bayes import GaussianNB

from ..data import create


def main(args):
  x_train, y_train, x_test, y_test = create(args.dataset, args.data_path)
  gnb = GaussianNB()
  gnb.fit(x_train, y_train)
  print('Accuracy of {}: {}'.format(args.dataset, gnb.score(x_test, y_test)))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--dataset', type=str)
  parser.add_argument('--data_path', type=str)

  main(parser.parse_args())
