#!/usr/bin/env python3

# Algo: https://rosettacode.org/wiki/Pi#Python

pi_digits = str()

q, r, t, k, n, l, c = 1, 0, 1, 1, 3, 3, 0

while c <= 10000:
  if 4*q+r-t < n*t:
      pi_digits += (str(n))
      nr = 10*(r-n*t)
      n  = ((10*(3*q+r))//t)-10*n
      q  *= 10
      r  = nr
      c += 1
  else:
      nr = (2*q+r)*l
      nn = (q*(7*k)+2+(r*l))//(t*l)
      q  *= k
      t  *= l
      l  += 2
      k += 1
      n  = nn
      r  = nr
 
print("3.{}".format(pi_digits[1:]))