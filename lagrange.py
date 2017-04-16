import numpy as np
import matplotlib.pyplot as plt
import sys

def lagrange(f, x):
    	total = 0
    	n = len(f)
    	for i in xrange(n):
    		xi, yi = f[i]
    			
    		def g(i, n):
    				
    			g_tot = 1
    			for j in xrange(n):
    				if i == j:
    					continue
    				xj, yj = f[j]
    				g_tot *= (x - xj) / float(xi - xj)
    					
    			return g_tot 
    
    		total += yi * g(i, n)
    	return total 

points =[(0,0),(45,30),(23,10), (48,0)]
xlist = [i for i in range(100)]
P = [lagrange(points, xlist[i]) for i in range(100)]
print(P)
plt.plot(xlist, P)
plt.show()
