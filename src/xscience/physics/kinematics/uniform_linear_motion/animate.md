# animate
![](animate.svg)

$$
x = x_0 + v t
$$

```svg
<svg
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  width="260" height="100"
  viewbox="0 0 260 100"
  style="border: 0px solid #fff;">
    <defs>
    <marker id="arrowhead" markerWidth="5" markerHeight="4" 
    refX="0" refY="2" orient="auto">
      <polygon fill="#888" points="0 0, 5 2, 0 4" />
    </marker>
  </defs>
  <line x1="48" y1="50" x2="68" y2="50" stroke="#888" 
    stroke-width="2" marker-end="url(#arrowhead)">
    <animate attributeName="x1" dur="4s"
      repeatCount="indefinite"
      values="46 ; 46 ; 206 ; 206"
      keyTimes="0 ; 0.25 ; 0.75 ; 1"
    />
    <animate attributeName="x2" dur="4s"
      repeatCount="indefinite"
      values="66 ; 66 ; 226 ; 226"
      keyTimes="0 ; 0.25 ; 0.75 ; 1"
    />
  </line>
  <text x="14" y="85" fill="#888" font-size="1em">
    <tspan font-family="Times">
      <tspan font-style="italic">x</tspan>
      <tspan baseline-shift="sub" font-size="0.8em">0</tspan>
    </tspan>
  </text>
  <rect x="2" y="30" width="40" height="40"
    stroke="#00a" stroke-width="2"
    fill="#55e" fill-opacity=".5">
    <animate attributeName="x" dur="4s"
      repeatCount="indefinite"
      values="2 ; 2 ; 158 ; 158"
      keyTimes="0 ; 0.25 ; 0.75 ; 1"
    />
  </rect>
  <text x="16" y="20" fill="#888" font-size="1em">
    <tspan font-family="Times" font-style="Italic">x</tspan>
    <animate attributeName="x" dur="4s"
      repeatCount="indefinite"
      values="16 ; 16 ; 176 ; 176"
      keyTimes="0 ; 0.25 ; 0.75 ; 1"
    />
  </text>
  <text x="80" y="55" fill="#888" font-size="1em">
    <tspan font-family="Times" font-style="Italic">v</tspan>
    <animate attributeName="x" dur="4s"
      repeatCount="indefinite"
      values="80 ; 80 ; 240 ; 240"
      keyTimes="0 ; 0.25 ; 0.75 ; 1"
    />
  </text>
</svg>
```
