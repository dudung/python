<pre>
```mermaid
flowchart TD
  B --> I --> D1 --Y--> C1a
  D1 --N--> C2a
  C1b --> P1 ---> C3a
  C2b --> D2 --Y--> P2
  D2 --N--> P3
  P2 & P3 --> C3a
  C3b --> O --> E
  C1a(("1"))
  C1b(("1"))
  C2a(("2"))
  C2b(("2"))
  C3a(("3"))
  C3b(("3"))
  B(("Begin"))
  I[/"x"/]
  D1{"x < 0?"}
  D2{"x > 0?"}
  P1["msg = 'negative'"]
  P2["msg = 'positive'"]
  P3["msg = 'zero'"]
  O[/"x is msg"/]
  E(("End"))
```
</pre>


```mermaid
flowchart TD
  B --> I --> D1 --Y--> C1a
  D1 --N--> C2a
  C1b --> P1 ---> C3a
  C2b --> D2 --Y--> P2
  D2 --N--> P3
  P2 & P3 --> C3a
  C3b --> O --> E
  C1a(("1"))
  C1b(("1"))
  C2a(("2"))
  C2b(("2"))
  C3a(("3"))
  C3b(("3"))
  B(("Begin"))
  I[/"x"/]
  D1{"x < 0"}
  D2{"x > 0"}
  P1["msg = 'negative'"]
  P2["msg = 'positive'"]
  P3["msg = 'zero'"]
  O[/"x is msg"/]
  E(("End"))
```

+ [code](negzeropos.py)