import matplotlib.pyplot as plt

x1 = [1, 9]
y1 = [9, 1]

x2 = [1, 8]
y2 = [7, 3]

x3 = [1, 5]
y3 = [8, 7]

legends = ['red', 'green', 'blue']

plt.plot(x1, y1, 'r', x2, y2, 'g', x3, y3, 'b')
plt.legend(legends)
plt.show()
