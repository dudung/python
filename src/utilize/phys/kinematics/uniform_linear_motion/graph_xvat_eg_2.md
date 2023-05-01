# graph_xvat_eg_2
$$
x_0 = 10, \ \ \ \ v_0 = 5

$$

$t_0 = 2$ | $t_0 = 4$ | $t_0 = 6$
:-: | :-: | :-:
![](img/xt4.svg) | ![](img/xt5.svg) | ![](img/xt6.svg)
![](img/vt4.svg) | ![](img/vt5.svg) | ![](img/vt6.svg)
![](img/at4.svg) | ![](img/at5.svg) | ![](img/at6.svg)



```shell
$ ../../../../../scripts/mdgnu.sh graph_xvat_eg.md
```


```bash
set term svg size 180,200 font "Times, 16" enhanced
set grid
set tics scale 0.4
set xlabel "{/Times:Italic t}" offset 0, 0.5
set xrange [0:6]
set ylabel '' offset 2
set lmargin 6
set rmargin 1

rcolor = '#0000ff'
vcolor = '#00ff00'
acolor = '#ff0000'

v_0 = 5
x_0 = 10
set xrange [-0.5:6.5]
set xtics 2

do for [i = 1:3] {
  t_0 = 2 * i
  r(t) = x_0 + v_0 * (t - t_0)
  v(t) = v_0
  a(t) = 0
  
  num = i + 3
  
  set output 'img/xt'.num.'.svg'
  set ylabel "{/Times:Italic x}"
  set yrange [-12:22]
  set ytics 10
  plot r(x) t '' w l lw 2 lc rgb rcolor

  set output 'img/vt'.num.'.svg'
  set ylabel "{/Times:Italic v}"
  set yrange [-6:6]
  set ytics 5
  plot v(x) t '' w l lw 2 lc rgb vcolor

  set output 'img/at'.num.'.svg'
  set ylabel "{/Times:Italic a}"
  set yrange [-1.2:1.2]
  set ytics 1
  plot a(x) t '' w l lw 2 lc rgb acolor
}

```
