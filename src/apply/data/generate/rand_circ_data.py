import os
import random as rn
import pandas as pd

# create headers for n variables with d digits numbering
d = 1
n = 10
headers = [f"x{i:0{d}d}" for i in range(n)]

# define ranges for random integer number
m = 100
c0 = [rn.randint(1, 2) for i in range(m)]
c1 = [rn.randint(145, 165) if i == 1 else rn.randint(160, 175) for i in c0]
c2 = [rn.randint(40, 60) if i == 1 else rn.randint(55, 90) for i in c0]
c3 = [rn.randint(1, 3) for i in range(m)]

c12 = [100, 110]
c4 = []
for i in range(m):
  s = c0[i]
  val = 2
  if (c1[i] - c2[i] < c12[s-1]):
    val = 1
  c4.append(val)

c5 = [rn.randint(0, 20) for i in range(m)]
c6 = [rn.randint(0, 20) for i in range(m)]
c7 = [1 if ((c5[i]-10)**2 + (c6[i]-10)**2) < 64 else 0 for i in range(m)]
c8 = [rn.randint(0, 5) if i == 1 else rn.randint(6, 10) for i in c7]
c9 = [1 if (c5[i] + c6[i] > 20) else 0 for i in range(m)]

print("Generated data")
e = 2
print(*headers, sep='\t')
for i in range(m):
  print(
    c0[i], c1[i], c2[i], c3[i], c4[i],
    c5[i], c6[i], c7[i], c8[i], c9[i],
    sep='\t'
  )
print()

# create dataframe from previous lists
df_out = pd.DataFrame(
  list(
    zip(
      c0, c1, c2, c3, c4,
      c5, c6, c7, c8, c9
    )
  ),
  columns=headers
)

print("Dataframe to be written")
print(df_out)

print()

# write dataframe to excel file,
df_out.to_excel(
  "xlsx/random_data.xlsx",
  sheet_name="random_x1_x9",
  index=False
  )

# read excel file as dataframe
df_in = pd.read_excel("xlsx/random_data.xlsx")

print("Read dataframe from file")
print(df_in)

print()

if os.path.exists("xlsx/random_data.xlsx"):
  os.remove("xlsx/random_data.xlsx")
  print("File is deleted")
else:
  print("File does not exist")


"""
$ rand_circ_data.py
Generated data
x0      x1      x2      x3      x4      x5      x6      x7      x8      x9
1       150     46      1       2       13      10      1       2       1
1       149     44      1       2       1       8       0       9       0
2       166     84      1       1       16      18      0       10      1
1       157     56      2       2       9       7       1       0       0
1       159     52      1       2       18      8       0       6       1
1       159     46      2       2       9       0       0       7       0
1       163     60      1       2       1       0       0       6       0
2       172     76      1       1       9       12      1       1       1
1       150     42      2       2       19      3       0       8       1

Dataframe to be written
    x0   x1  x2  x3  x4  x5  x6  x7  x8  x9
0    1  150  46   1   2  13  10   1   2   1
1    1  149  44   1   2   1   8   0   9   0
2    2  166  84   1   1  16  18   0  10   1
3    1  157  56   2   2   9   7   1   0   0
4    1  157  48   3   2   7  15   1   2   1
..  ..  ...  ..  ..  ..  ..  ..  ..  ..  ..
95   1  159  52   1   2  18   8   0   6   1
96   1  159  46   2   2   9   0   0   7   0
97   1  163  60   1   2   1   0   0   6   0
98   2  172  76   1   1   9  12   1   1   1
99   1  150  42   2   2  19   3   0   8   1

[100 rows x 10 columns]

Read dataframe from file
    x0   x1  x2  x3  x4  x5  x6  x7  x8  x9
0    1  150  46   1   2  13  10   1   2   1
1    1  149  44   1   2   1   8   0   9   0
2    2  166  84   1   1  16  18   0  10   1
3    1  157  56   2   2   9   7   1   0   0
4    1  157  48   3   2   7  15   1   2   1
..  ..  ...  ..  ..  ..  ..  ..  ..  ..  ..
95   1  159  52   1   2  18   8   0   6   1
96   1  159  46   2   2   9   0   0   7   0
97   1  163  60   1   2   1   0   0   6   0
98   2  172  76   1   1   9  12   1   1   1
99   1  150  42   2   2  19   3   0   8   1

[100 rows x 10 columns]

File is deleted
"""