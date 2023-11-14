import pandas as pd
df = pd.read_csv('data_1.csv')

h = [*df.columns]
print('h =', h)

col0 = [*df.get(h[0])]
print(h[0], '=', col0)

col1 = [*df.get(h[1])]
print(h[1], '=', col1)
