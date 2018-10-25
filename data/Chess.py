from sklearn.model_selection import train_test_split


def parse(line):
  features = line.split(',')
  file_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
  result_dict = {'draw':-1, 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
  'nine':9, 'ten':10, 'eleven':11, 'twelve':12,'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16}
  x = []
  for i in range(len(features) - 1):
    if i % 2 == 0:
      x.append(file_dict[features[i]])
    else:
      x.append(int(features[i]))
  y = result_dict[features[-1]]
  return x, y


def Chess(data_path):
  x_array, y_array = [], []
  with open(data_path, 'r') as infile:
    while True:
      line = infile.readline().strip()
      if not line:
        break
      x, y = parse(line)
      x_array.append(x)
      y_array.append(y)
  return train_test_split(x_array, y_array, test_size = 0.2)


if __name__ == '__main__':
  Chess('/Users/DavidGuan/Desktop/机器学习/homework1/data/chess/krkopt.data')

