x_stop = range(10)
y1 = list(x_stop)
print(y1)

x_start_stop = range(3, 10)
y2 = [*x_start_stop]
print(y2)

x_start_stop_step = range(2, 10, 2)
y3 = []
y3.extend(x_start_stop_step)
print(y3)


"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[3, 4, 5, 6, 7, 8, 9]
[2, 4, 6, 8]
"""
