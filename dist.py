import sys
import math
def distance(p1, p2):
   if len(p1)!=len(p2): sys.exit("Vectors have different length")
   sum=0
   for i in range(len(p1)):
        sum+=(p1[i]-p2[i])**2
   return math.sqrt(sum)

a=[1.,2.,3.]
b=[5.,6.,7.]
distance(a,b)

#distance(a,b)= 6.928203230275509
