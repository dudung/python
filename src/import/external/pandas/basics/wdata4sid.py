# data4sid
# data for student id

output = "data2.xlsx"

sid = [
    10218078, 10219009, 10219023, 10219056, 10219075, 10219076,
    10219109, 10220004, 10220007, 10220009, 10220011, 10220012,
    10220013, 10220014, 10220018, 10220021, 10220031, 10220033,
    10220035, 10220037, 10220038, 10220042, 10220048, 10220051,
    10220055, 10220056, 10220063, 10220067, 10220068, 10220073,
    10220076, 10220080, 10220082, 10294017, 10295019, 10296020,
]

import random

import pandas as pd
writer = pd.ExcelWriter(output, engine='xlsxwriter')

ROWS = 10
colheader = ['x1', 'x2', 'x3', 'x4']


for s in sid[-3:]:

  c1 = [random.randint(0, ROWS) for i in range(ROWS)]
  c2 = [i for i in c1]
  c3 = [i**2 for i in c2]
  c4 = [i**3 for i in c2]
  df = pd.DataFrame(list(zip(c1, c2, c3, c4)), columns=colheader)
  
  id = str(s)
  df.to_excel(writer, index=False, sheet_name=id)

writer.close()