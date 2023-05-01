# graph_xvat_eg_3
$$
v_0 = 5, \ \ \ \ t_0 = 4

$$

$x_0 = 0$ | $x_0 = 10$ | $x_0 = 20$
:-: | :-: | :-:
![](img/xt7.svg) | ![](img/xt8.svg) | ![](img/xt9.svg)
![](img/vt7.svg) | ![](img/vt8.svg) | ![](img/vt9.svg)
![](img/at7.svg) | ![](img/at8.svg) | ![](img/at9.svg)



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
t_0 = 4
set xrange [-0.5:6.5]
set xtics 2

do for [i = 1:3] {
  x_0 = 10*i - 10
  r(t) = x_0 + v_0 * (t - t_0)
  v(t) = v_0
  a(t) = 0
  
  num = i + 6
  
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
