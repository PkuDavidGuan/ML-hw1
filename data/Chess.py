from sklearn.model_selection import train_test_split


def parse(line):
  features = line.split(',')
  file_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
  result_dict = {'draw':-1, 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
  'nine':9, 'ten':10, 'eleven':11, 'twelve':12,'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16}
  x = []
  # x.append((file_dict[features[0]] * 8 + int(features[1])) * 64 + file_dict[features[2]] * 8 + int(features[3]))
  # x.append(file_dict[features[4]] * 8 + int(features[5]))
  # y = result_dict[features[-1]]
  for i in range(len(features) - 1):
    if i % 2 == 0:
      x.append(file_dict[features[i]])
    else:
      x.append(int(features[i]))
  y = result_dict[features[-1]]
  return x, y


def Chess(data_path, with_val=True):
  x_array, y_array = [], []
  with open(data_path, 'r') as infile:
    while True:
      line = infile.readline().strip()
      if not line:
        break
      x, y = parse(line)
      x_array.append(x)
      y_array.append(y)
  if not with_val:
    return train_test_split(x_array, y_array, test_size = 0.2)
  else:
    x_train, x_test, y_train, y_test = train_test_split(x_array, y_array, train_size=0.6)
    x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, train_size=0.5)
    return x_train, x_val, x_test, y_train, y_val, y_test


if __name__ == '__main__':
  Chess('/Users/DavidGuan/Desktop/机器学习/homework1/data/chess/krkopt.data')

