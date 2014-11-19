#!/usr/bin/env python

from elliptic import *
from point import *
from diffiehellman import *
#from fractions import Fraction as frac


p=8884933102832021670310856601112383279507496491807071433260928721853918699951
n=8884933102832021670310856601112383279454437918059397120004264665392731659049
a4=2481513316835306518496091950488867366805208929993787063131352719741796616329
a6=4387305958586347890529260320831286139799795892409507048422786783411496715073
r4=5473953786136330929505372885864126123958065998198197694258492204115618878079
r6=5831273952509092555776116225688691072512584265972424782073602066621365105518
gx=7638166354848741333090176068286311479365713946232310129943505521094105356372
gy=762687367051975977761089912701686274060655281117983501949286086861823169994
r=8094458595770206542003150089514239385761983350496862878239630488323200271273

f = primes(8888888888888)


print f[0]

C = EllipticCurve(p, n, a4, a6, r4, r6, gx, gy, r)


P = Point(C, C.gx, C.gy)
Q1 = Point(C,0,1,True)

for i in range(1,100):
   Q1 = Q1 + P
   Q2 = i*P
   assert Q1 == Q2, "Multiplication and addition have different results(%dP)" % i

print ("Multiplication->OK")

DH(C)

"""
p=5
n=8884933102832021670310856601112383279454437918059397120004264665392731659049
a4=1
a6=1
r4=5473953786136330929505372885864126123958065998198197694258492204115618878079
r6=5831273952509092555776116225688691072512584265972424782073602066621365105518
gx=7638166354848741333090176068286311479365713946232310129943505521094105356372
gy=762687367051975977761089912701686274060655281117983501949286086861823169994
r=8094458595770206542003150089514239385761983350496862878239630488323200271273


C = EllipticCurve(p, n, a4, a6, r4, r6, gx, gy, r)

#P = Point(C, C.gx, C.gy,False)
P = Point(C, 3, 1)
Q = Point(C, 2, 4)
R = Q + P
print(R)
print (P+Q)
"""
