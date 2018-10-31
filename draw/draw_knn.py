import matplotlib
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,23,25]
y1 = [0.53, 0.59, 0.70, 0.68, 0.66, 0.65, 0.64, 0.64, 0.63, 0.63, 0.64, 0.63, 0.63]
y2 = [.57, .61, .64, .65, .64, .65, .63, .64, .65, .64, .65, .65, .64]
y3 = [0.8277777777777777, 0.8333333333333334, 0.85, 0.8388888888888889, .8333333333333334, 0.8444444444444444, 0.8388888888888889,
      0.85, 0.8222222222222222, .8055555555555556, 0.8166666666666667, 0.7944444444444444, 0.8166666666666667]
x_label = 'k_neighbors'
y_label = 'Accuracy'
file_name = 'knn_chess.png'
lineWidth = 3.0
plt.plot(x, y1, '-', label='chess', linewidth=lineWidth)
plt.plot(x, y2, '*', label='abalone', linewidth=lineWidth)
plt.plot(x, y3, '-.', label='cnae', linewidth=lineWidth)
plt.legend()
plt.xlabel(x_label, fontsize = "x-large")
plt.ylabel(y_label, fontsize = "x-large")
plt.savefig(file_name)

epochNum = [10, 20, 40, 80, 100, 120]