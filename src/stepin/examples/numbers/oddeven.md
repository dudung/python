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
  I[/"x"/]
  D{"x % 2 == 1?"}
  P1["msg = 'odd'"]
  P2["msg = 'even'"]
  O[/"x is msg"/]
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
  I[/"x"/]
  D{"x % 2 == 1?"}
  P1["msg = 'odd'"]
  P2["msg = 'even'"]
  O[/"x is msg"/]
  E(("End"))
```


```python
# begin

# input
x = int(input("Give a number : "))

# decision
if x % 2 == 1:
  # process 1
  msg = "odd"
else:
  # process 2
  msg = "even"

# ouput
print(x, "is", msg)

# end


"""
$ python oddeven.py
Give a number : 2
2 is even
$ python oddeven.py
Give a number : 3
3 is odd
"""
```
