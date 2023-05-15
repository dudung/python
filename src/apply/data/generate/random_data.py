import os
import random as rn
import pandas as pd



# create headers for n variables with d digits numbering
d = 1
n = 10
headers = [f"x{i:0{d}d}" for i in range(n)]

# define ranges for random integer number
m = 10
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

c5 = [rn.randint(145, 165) if i == 2 else rn.randint(160, 175) for i in c0]
c6 = [rn.randint(40, 60) if i == 2 else rn.randint(55, 90) for i in c0]
c7 = [rn.randint(1, 3) for i in range(m)]

c8 = [1 if (c4[i] == 1) and (c0[i] == 1) else 0 for i in range(m)]
c9 = [1 if (c4[i] == 1) and (c0[i] == 2) else 0 for i in range(m)]

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
$ python random_data.py
Generated data
x0      x1      x2      x3      x4      x5      x6      x7      x8      x9
2       175     67      2       1       150     53      1       0       1
1       149     52      1       1       171     73      2       1       0
1       165     58      3       2       171     69      2       0       0
2       161     66      2       1       158     52      1       0       1
1       163     41      3       2       162     89      1       0       0
1       146     51      1       1       162     66      3       1       0
1       159     42      2       2       161     60      3       0       0
1       162     48      3       2       168     81      1       0       0
2       163     61      2       1       150     43      1       0       1
2       175     78      3       1       151     60      2       0       1

Dataframe to be written
   x0   x1  x2  x3  x4   x5  x6  x7  x8  x9
0   2  175  67   2   1  150  53   1   0   1
1   1  149  52   1   1  171  73   2   1   0
2   1  165  58   3   2  171  69   2   0   0
3   2  161  66   2   1  158  52   1   0   1
4   1  163  41   3   2  162  89   1   0   0
5   1  146  51   1   1  162  66   3   1   0
6   1  159  42   2   2  161  60   3   0   0
7   1  162  48   3   2  168  81   1   0   0
8   2  163  61   2   1  150  43   1   0   1
9   2  175  78   3   1  151  60   2   0   1

Read dataframe from file
   x0   x1  x2  x3  x4   x5  x6  x7  x8  x9
0   2  175  67   2   1  150  53   1   0   1
1   1  149  52   1   1  171  73   2   1   0
2   1  165  58   3   2  171  69   2   0   0
3   2  161  66   2   1  158  52   1   0   1
4   1  163  41   3   2  162  89   1   0   0
5   1  146  51   1   1  162  66   3   1   0
6   1  159  42   2   2  161  60   3   0   0
7   1  162  48   3   2  168  81   1   0   0
8   2  163  61   2   1  150  43   1   0   1
9   2  175  78   3   1  151  60   2   0   1

File is deleted
"""