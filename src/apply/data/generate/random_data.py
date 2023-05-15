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

print("Generated data")
e = 2
print(*headers, sep='\t')
for i in range(m):
  print(
    c0[i], c1[i], c2[i], c3[i], c4[i],
    sep='\t'
  )
print()

# create dataframe from previous lists
df_out = pd.DataFrame(
  list(
    zip(
      c0, c1, c2, c3, c4
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
x0      x1      x2      x3      x4
2       175     67      2       1
1       149     52      1       1
1       165     58      3       2
2       161     66      2       1
1       163     41      3       2
1       146     51      1       1
1       159     42      2       2
1       162     48      3       2
2       163     61      2       1
2       175     78      3       1

Dataframe to be written
   x0   x1  x2  x3  x4
0   2  175  67   2   1
1   1  149  52   1   1
2   1  165  58   3   2
3   2  161  66   2   1
4   1  163  41   3   2
5   1  146  51   1   1
6   1  159  42   2   2
7   1  162  48   3   2
8   2  163  61   2   1
9   2  175  78   3   1

Read dataframe from file
   x0   x1  x2  x3  x4
0   2  175  67   2   1
1   1  149  52   1   1
2   1  165  58   3   2
3   2  161  66   2   1
4   1  163  41   3   2
5   1  146  51   1   1
6   1  159  42   2   2
7   1  162  48   3   2
8   2  163  61   2   1
9   2  175  78   3   1

File is deleted
"""