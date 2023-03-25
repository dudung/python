<pre>
```mermaid
flowchart TD
  B --> I --> D
  D --Y--> C1a
  D --N--> C2a
  C1b --> P1 --> O
  C2b --> P2 --> O
  O --> E
  C1a(("1"))
  C1b(("1"))
  C2a(("2"))
  C2b(("2"))
  B(("Begin"))
  I[/"x, y"/]
  D{"x < y?"}
  P1["sign = '<'"]
  P2["sign = '>='"]
  O[/"x sign y"/]
  E(("End"))
```
</pre>


```mermaid
flowchart TD
  B --> I --> D
  D --Y--> C1a
  D --N--> C2a
  C1b --> P1 --> O
  C2b --> P2 --> O
  O --> E
  C1a(("1"))
  C1b(("1"))
  C2a(("2"))
  C2b(("2"))
  B(("Begin"))
  I[/"x, y"/]
  D{"x < y?"}
  P1["sign = '<'"]
  P2["sign = '>='"]
  O[/"x sign y"/]
  E(("End"))
```


```python
# begin

# input
x = float(input("x = "))
y = float(input("y = "))

# decision
if x < y:
  # process 1
  sign= "<"
else:
  # process 2
  sign = ">="

# ouput
print(x, sign, y)

# end


"""
$ python compare.py
x = 3
y = 6
3.0 < 6.0
$ python compare.py
x = 6
y = 2
6.0 >= 2.0
"""
```
