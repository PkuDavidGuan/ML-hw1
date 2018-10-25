from sklearn.model_selection import train_test_split


def parse(line):
  features = [int(f) for f in line.split(',')]
  return features[1:], features[0]


def Cnae(data_path):
  x_array, y_array = [], []
  with open(data_path, 'r') as infile:
    while True:
      line = infile.readline().strip()
      if not line:
        break
      x, y = parse(line)
      x_array.append(x)
      y_array.append(y)
  return train_test_split(x_array, y_array, train_size=900)
