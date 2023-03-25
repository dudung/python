<pre>
```mermaid
flowchart LR
  B --> I --> P --> O --> E
  B(("Begin"))
  I[/"read x, y"/]
  P["z = x - y"]
  O[/"display z"/]
  E(("End"))
```
</pre>


```mermaid
flowchart LR
  B --> I --> P --> O --> E
  B(("Begin"))
  I[/"read x, y"/]
  P["z = x - y"]
  O[/"display z"/]
  E(("End"))
```


```python
# begin

# input
x = float(input("x = "))
y = float(input("y = "))

# process
z = x - y

# ouput
print("z = x - y =", z)

# end


"""
$ python substract.py
x = 5
y = 7.2
z = x - y = -2.2
"""
```