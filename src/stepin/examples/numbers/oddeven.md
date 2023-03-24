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

+ [code](oddeven.py)