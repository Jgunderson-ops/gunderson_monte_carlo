# some card identification tests to run
## (initialize player first)
## (jaxon = poker_monte_carlo.Player())

a = poker_monte_carlo.Card("3s")
b = poker_monte_carlo.Card("0d")
c = poker_monte_carlo.Card("8h")
d = poker_monte_carlo.Card("5d")
e = poker_monte_carlo.Card("2h")
f = poker_monte_carlo.Card("9h")
g = poker_monte_carlo.Card("6h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## high card
## 0d, 9h, 8h, 6h, 5d

a = poker_monte_carlo.Card("7s")
b = poker_monte_carlo.Card("2h")
c = poker_monte_carlo.Card("ad")
d = poker_monte_carlo.Card("4h")
e = poker_monte_carlo.Card("9c")
f = poker_monte_carlo.Card("ks")
g = poker_monte_carlo.Card("8h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## high card
## 7s, ad, 9c, ks, 8h

a = poker_monte_carlo.Card("0c")
b = poker_monte_carlo.Card("ks")
c = poker_monte_carlo.Card("5h")
d = poker_monte_carlo.Card("7h")
e = poker_monte_carlo.Card("4h")
f = poker_monte_carlo.Card("ac")
g = poker_monte_carlo.Card("9c")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## high card
## 0c, ks, 7h, ac, 9c

a = poker_monte_carlo.Card("6s")
b = poker_monte_carlo.Card("jd")
c = poker_monte_carlo.Card("3d")
d = poker_monte_carlo.Card("7h")
e = poker_monte_carlo.Card("9s")
f = poker_monte_carlo.Card("2s")
g = poker_monte_carlo.Card("qh")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## high card
## 6s, jd, 7h, 9s, qh

a = poker_monte_carlo.Card("9c")
b = poker_monte_carlo.Card("6s")
c = poker_monte_carlo.Card("2s")
d = poker_monte_carlo.Card("qs")
e = poker_monte_carlo.Card("4d")
f = poker_monte_carlo.Card("as")
g = poker_monte_carlo.Card("jc")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## high card
## 9c, 6s, qs, as, jc

a = poker_monte_carlo.Card("ah")
b = poker_monte_carlo.Card("qh")
c = poker_monte_carlo.Card("js")
d = poker_monte_carlo.Card("0c")
e = poker_monte_carlo.Card("7h")
f = poker_monte_carlo.Card("6h")
g = poker_monte_carlo.Card("3d")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## High card
## ah, qh, js, 0c, 7h

a = poker_monte_carlo.Card("0d")
b = poker_monte_carlo.Card("0h")
c = poker_monte_carlo.Card("kh")
d = poker_monte_carlo.Card("jc")
e = poker_monte_carlo.Card("7s")
f = poker_monte_carlo.Card("6h")
g = poker_monte_carlo.Card("3h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 0d, 0h, kh, jc, 7s

a = poker_monte_carlo.Card("qh")
b = poker_monte_carlo.Card("qs")
c = poker_monte_carlo.Card("0c")
d = poker_monte_carlo.Card("ks")
e = poker_monte_carlo.Card("jd")
f = poker_monte_carlo.Card("7s")
g = poker_monte_carlo.Card("6c")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## qh, qs, ks, jd, 0c

a = poker_monte_carlo.Card("qs")
b = poker_monte_carlo.Card("jc")
c = poker_monte_carlo.Card("2c")
d = poker_monte_carlo.Card("3h")
e = poker_monte_carlo.Card("6c")
f = poker_monte_carlo.Card("0s")
g = poker_monte_carlo.Card("jd")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## jc, jd, qs, 0s, 6c

a = poker_monte_carlo.Card("5h")
b = poker_monte_carlo.Card("5c")
c = poker_monte_carlo.Card("8h")
d = poker_monte_carlo.Card("4h")
e = poker_monte_carlo.Card("3d")
f = poker_monte_carlo.Card("kc")
g = poker_monte_carlo.Card("6s")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 5h, 5c, kc, 8h, 6s

a = poker_monte_carlo.Card("5d")
b = poker_monte_carlo.Card("2d")
c = poker_monte_carlo.Card("8h")
d = poker_monte_carlo.Card("5c")
e = poker_monte_carlo.Card("4s")
f = poker_monte_carlo.Card("6c")
g = poker_monte_carlo.Card("as")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 5d, 8h, 5c, 6c, as

a = poker_monte_carlo.Card("6s")
b = poker_monte_carlo.Card("2s")
c = poker_monte_carlo.Card("5d")
d = poker_monte_carlo.Card("7c")
e = poker_monte_carlo.Card("2c")
f = poker_monte_carlo.Card("kh")
g = poker_monte_carlo.Card("js")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 2s, 7c, 2c, kh, js

a = poker_monte_carlo.Card("3c")
b = poker_monte_carlo.Card("6c")
c = poker_monte_carlo.Card("3s")
d = poker_monte_carlo.Card("qd")
e = poker_monte_carlo.Card("9d")
f = poker_monte_carlo.Card("kd")
g = poker_monte_carlo.Card("ac")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 3c, 3s, qd, kd, ac

a = poker_monte_carlo.Card("0s")
b = poker_monte_carlo.Card("0c")
c = poker_monte_carlo.Card("4d")
d = poker_monte_carlo.Card("kd")
e = poker_monte_carlo.Card("6d")
f = poker_monte_carlo.Card("5c")
g = poker_monte_carlo.Card("9s")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 0s, 0c, kd, 6d, 9s

a = poker_monte_carlo.Card("6d")
b = poker_monte_carlo.Card("7d")
c = poker_monte_carlo.Card("3d")
d = poker_monte_carlo.Card("2h")
e = poker_monte_carlo.Card("9s")
f = poker_monte_carlo.Card("qh")
g = poker_monte_carlo.Card("qs")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 6d, 7d, 9s, qh, qs

a = poker_monte_carlo.Card("qs")
b = poker_monte_carlo.Card("8h")
c = poker_monte_carlo.Card("4s")
d = poker_monte_carlo.Card("qh")
e = poker_monte_carlo.Card("2d")
f = poker_monte_carlo.Card("9d")
g = poker_monte_carlo.Card("5c")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## qs, 8h, qh, 9d, 5c

a = poker_monte_carlo.Card("4h")
b = poker_monte_carlo.Card("4c")
c = poker_monte_carlo.Card("ad")
d = poker_monte_carlo.Card("8s")
e = poker_monte_carlo.Card("qh")
f = poker_monte_carlo.Card("6d")
g = poker_monte_carlo.Card("2c")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 4h, 4c, ad, 8s, qh

a = poker_monte_carlo.Card("3h")
b = poker_monte_carlo.Card("8d")
c = poker_monte_carlo.Card("6d")
d = poker_monte_carlo.Card("2c")
e = poker_monte_carlo.Card("0c")
f = poker_monte_carlo.Card("jh")
g = poker_monte_carlo.Card("6c")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 8d, 6d, 0c, jh, 6c

a = poker_monte_carlo.Card("jh")
b = poker_monte_carlo.Card("8d")
c = poker_monte_carlo.Card("4c")
d = poker_monte_carlo.Card("5s")
e = poker_monte_carlo.Card("0d")
f = poker_monte_carlo.Card("5h")
g = poker_monte_carlo.Card("kh")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## jh, 5s, 0d, 5h, kh

a = poker_monte_carlo.Card("qh")
b = poker_monte_carlo.Card("5c")
c = poker_monte_carlo.Card("3c")
d = poker_monte_carlo.Card("2s")
e = poker_monte_carlo.Card("9s")
f = poker_monte_carlo.Card("4h")
g = poker_monte_carlo.Card("3d")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## qh, 5c, 3c, 9s, 3d

a = poker_monte_carlo.Card("kd")
b = poker_monte_carlo.Card("ad")
c = poker_monte_carlo.Card("2d")
d = poker_monte_carlo.Card("2h")
e = poker_monte_carlo.Card("qc")
f = poker_monte_carlo.Card("8s")
g = poker_monte_carlo.Card("jc")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## kd, ad, 2d, 2h, qc

a = poker_monte_carlo.Card("0d")
b = poker_monte_carlo.Card("4s")
c = poker_monte_carlo.Card("7d")
d = poker_monte_carlo.Card("8s")
e = poker_monte_carlo.Card("ks")
f = poker_monte_carlo.Card("9d")
g = poker_monte_carlo.Card("0s")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## pair
## 0d, 8s, ks, 9d, 0s

a = poker_monte_carlo.Card("8s")
b = poker_monte_carlo.Card("4d")
c = poker_monte_carlo.Card("8d")
d = poker_monte_carlo.Card("kd")
e = poker_monte_carlo.Card("js")
f = poker_monte_carlo.Card("7s")
g = poker_monte_carlo.Card("7d")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## two pair
## 8s, 8d, 7s, 7d, kd

a = poker_monte_carlo.Card("qs")
b = poker_monte_carlo.Card("jc")
c = poker_monte_carlo.Card("2c")
d = poker_monte_carlo.Card("3h")
e = poker_monte_carlo.Card("3d")
f = poker_monte_carlo.Card("0s")
g = poker_monte_carlo.Card("jd")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## two pair
## 3h, 3d, jc, jd, qs

a = poker_monte_carlo.Card("9c")
b = poker_monte_carlo.Card("4c")
c = poker_monte_carlo.Card("5h")
d = poker_monte_carlo.Card("qh")
e = poker_monte_carlo.Card("5c")
f = poker_monte_carlo.Card("qc")
g = poker_monte_carlo.Card("6d")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## two pair
## 9c, 5h, qh, 5c, qc

a = poker_monte_carlo.Card("3d")
b = poker_monte_carlo.Card("3c")
c = poker_monte_carlo.Card("3h")
d = poker_monte_carlo.Card("kd")
e = poker_monte_carlo.Card("7c")
f = poker_monte_carlo.Card("2c")
g = poker_monte_carlo.Card("9c")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## trips
## 3d, 3c, 3h, kd, 9c

a = poker_monte_carlo.Card("3s")
b = poker_monte_carlo.Card("2s")
c = poker_monte_carlo.Card("jc")
d = poker_monte_carlo.Card("5c")
e = poker_monte_carlo.Card("2c")
f = poker_monte_carlo.Card("2h")
g = poker_monte_carlo.Card("qc")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## trips
## 2s, jc, 2c, 2h, qc

a = poker_monte_carlo.Card("7c")
b = poker_monte_carlo.Card("kc")
c = poker_monte_carlo.Card("6s")
d = poker_monte_carlo.Card("3d")
e = poker_monte_carlo.Card("4h")
f = poker_monte_carlo.Card("5c")
g = poker_monte_carlo.Card("5h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## straight
## 3d, 4h, 5(c or h), 6s, 7c

a = poker_monte_carlo.Card("5h")
b = poker_monte_carlo.Card("3h")
c = poker_monte_carlo.Card("2s")
d = poker_monte_carlo.Card("4c")
e = poker_monte_carlo.Card("kd")
f = poker_monte_carlo.Card("as")
g = poker_monte_carlo.Card("2c")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## straight
## 5h, 3h, 4c, as, 2c

a = poker_monte_carlo.Card("jd")
b = poker_monte_carlo.Card("9s")
c = poker_monte_carlo.Card("5c")
d = poker_monte_carlo.Card("0c")
e = poker_monte_carlo.Card("4c")
f = poker_monte_carlo.Card("kc")
g = poker_monte_carlo.Card("jc")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## flush
## jc, kc, 4c, 0c, 5c

a = poker_monte_carlo.Card("4h")
b = poker_monte_carlo.Card("2h")
c = poker_monte_carlo.Card("qh")
d = poker_monte_carlo.Card("kh")
e = poker_monte_carlo.Card("ac")
f = poker_monte_carlo.Card("qs")
g = poker_monte_carlo.Card("9h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## flush
## 4h, 2h, qh, kh, 9h

a = poker_monte_carlo.Card("ad")
b = poker_monte_carlo.Card("3d")
c = poker_monte_carlo.Card("kd")
d = poker_monte_carlo.Card("9c")
e = poker_monte_carlo.Card("jd")
f = poker_monte_carlo.Card("7h")
g = poker_monte_carlo.Card("5d")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## flush
## ad, 3d, kd, jd, 5d

a = poker_monte_carlo.Card("ks")
b = poker_monte_carlo.Card("8d")
c = poker_monte_carlo.Card("6d")
d = poker_monte_carlo.Card("2d")
e = poker_monte_carlo.Card("3d")
f = poker_monte_carlo.Card("9d")
g = poker_monte_carlo.Card("4d")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## flush
## 8d, 6d, 3d, 9d, 4d

a = poker_monte_carlo.Card("2c")
b = poker_monte_carlo.Card("9c")
c = poker_monte_carlo.Card("kc")
d = poker_monte_carlo.Card("qc")
e = poker_monte_carlo.Card("ac")
f = poker_monte_carlo.Card("3c")
g = poker_monte_carlo.Card("jc")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## flush
## 9c, kc, qc, ac, jc

a = poker_monte_carlo.Card("6c")
b = poker_monte_carlo.Card("2s")
c = poker_monte_carlo.Card("ad")
d = poker_monte_carlo.Card("8h")
e = poker_monte_carlo.Card("8s")
f = poker_monte_carlo.Card("ah")
g = poker_monte_carlo.Card("ac")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## boat
## ad, ah, ac, 8h, 8s

a = poker_monte_carlo.Card("8c")
b = poker_monte_carlo.Card("6c")
c = poker_monte_carlo.Card("4c")
d = poker_monte_carlo.Card("3c")
e = poker_monte_carlo.Card("5c")
f = poker_monte_carlo.Card("ac")
g = poker_monte_carlo.Card("2c")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## straight flush
## 6c, 4c, 3c, 5c, 2c

a = poker_monte_carlo.Card("0c")
b = poker_monte_carlo.Card("jc")
c = poker_monte_carlo.Card("qc")
d = poker_monte_carlo.Card("kc")
e = poker_monte_carlo.Card("ac")
f = poker_monte_carlo.Card("5c")
g = poker_monte_carlo.Card("5h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## royal
## ac, kc, qc, jc, 0c

a = poker_monte_carlo.Card("0h")
b = poker_monte_carlo.Card("jh")
c = poker_monte_carlo.Card("qh")
d = poker_monte_carlo.Card("kh")
e = poker_monte_carlo.Card("ah")
f = poker_monte_carlo.Card("5c")
g = poker_monte_carlo.Card("5h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## royal
## ah, kh, qh, jh, 0h

a = poker_monte_carlo.Card("0d")
b = poker_monte_carlo.Card("jd")
c = poker_monte_carlo.Card("qd")
d = poker_monte_carlo.Card("kd")
e = poker_monte_carlo.Card("ad")
f = poker_monte_carlo.Card("5c")
g = poker_monte_carlo.Card("5h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## royal
## ad, kd, qd, jd, 0d

a = poker_monte_carlo.Card("0s")
b = poker_monte_carlo.Card("js")
c = poker_monte_carlo.Card("qs")
d = poker_monte_carlo.Card("ks")
e = poker_monte_carlo.Card("as")
f = poker_monte_carlo.Card("5c")
g = poker_monte_carlo.Card("5h")
jaxon.hand = []
jaxon.hand.append(a)
jaxon.hand.append(b)
jaxon.hand.append(c)
jaxon.hand.append(d)
jaxon.hand.append(e)
jaxon.hand.append(f)
jaxon.hand.append(g)
## royal
## as, ks, qs, js, 0s