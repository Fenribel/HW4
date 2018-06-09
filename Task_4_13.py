from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x):
    try:
        return 1/x**3
    except:
        return inf

def integr(a,b):
    sum = 0
    N = 8000
    h = (b-a) / N
    for i in range (N):
        try:
            sum += h*(f(a+h*(i+1/2))+f(a+h*(i-1/2)))/2
        except:
            sum+= inf
    return sum

print(integr(-1, 1))