Poker Monte Carlo Jaxon Gunderson. Will edit later.

# some card identification tests to run
# (initialize player first)
# (jaxon = poker_monte_carlo.Player())

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
# high card
# 0d, 9h, 8h, 6h, 5d

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
# pair
# jc, jd, qs, 0s, 6c

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
# pair
# 5h, 5c, kc, 8h, 6s

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
# two pair
# 8s, 8d, 7s, 7d, kd

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
# two pair
# 3h, 3d, jc, jd, qs

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
# trips
# 3d, 3c, 3h, kd, 9c

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
# straight
# 3d, 4h, 5(c or h), 6s, 7c

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
# flush
# jc, kc, 4c, 0c, 5c

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
# boat
# ad, ah, ac, 8h, 8s

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
# royal
# ac, kc, qc, jc, 0c

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
# royal
# ah, kh, qh, jh, 0h

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
# royal
# ad, kd, qd, jd, 0d

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
# royal
# as, ks, qs, js, 0s

______________________________________________________________

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
# High card
# ah, qh, js, 0c, 7h

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
# pair
# 0d, 0h, kh, jc, 7s

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
# pair
# qh, qs, ks, jd, 0c