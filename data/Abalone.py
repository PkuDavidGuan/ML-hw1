from sklearn.model_selection import train_test_split


def parse(line):
  gender_dict = {'I':0, 'F':1, 'M':2}
  features = line.split(',')

  x = [gender_dict[features[0]]]
  y = int(features[-1])

  for i in range(1, len(features) - 1):
    x.append(float(features[i]))

  return x, y


def Abalone(data_path, with_val=True):
  x_train, y_train, x_test, y_test = [], [], [], []
  with open(data_path, 'r') as infile:
    count = 0
    while True:
      line = infile.readline().strip()
      if not line:
        break
      count += 1
      x, y = parse(line)
      if count <= 3133:
        x_train.append(x)
        y_train.append(y)
      else:
        x_test.append(x)
        y_test.append(y)
  if not with_val:
    return x_train, x_test, y_train, y_test
  else:
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, train_size=len(x_train)-len(x_test))
    return x_train, x_val, x_test, y_train, y_val, y_test
