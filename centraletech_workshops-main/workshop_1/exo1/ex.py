from random import random
from math import pi

N = int(1e6)
P = [(random(),random()) for i in range(N)]
C = [p for p in P if pow(p[0],2)+pow(p[1],2)<=1]
PI = (4*len(C))/N

print(abs(PI-pi))