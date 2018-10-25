import argparse
from tqdm import tqdm
from sklearn.naive_bayes import GaussianNB, MultinomialNB

from ..data import create


def main(args):
  count = 0
  for i in tqdm(range(10)):
    x_train, x_test, y_train, y_test = create(args.dataset, args.data_path)
    # gnb = GaussianNB()
    gnb = MultinomialNB()
    gnb.fit(x_train, y_train)
    count += gnb.score(x_test, y_test)
  print('Accuracy of {}: {}'.format(args.dataset, count / 10))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--dataset', type=str)
  parser.add_argument('--data_path', type=str)

  main(parser.parse_args())
