from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x):
    try:
        return sin(x)
    except:
        return inf

def trueder(x):
    try:
        return cos(x)
    except:
        return inf

def trueint(x):
    try:
        return -cos(x)
    except:
        return inf


def der(x):
    h = 10**(-8.1)
    der = (f(x+h)-f(x-h))/(2*h)
    return der

def integr(a,b):
    sum = 0
    N = 1000
    h = (b-a) / N
    for i in range (N):
        try:
            sum += h*der(a+h*i)
        except:
            sum+= inf
    return sum

xs = []
f_vals = []
der_vals = []
cos_vals =[]
z_vals = []
in_vals = []

for i in range (1000):
    x = (i-500)/70
    f_vals += [f(x)]
    der_vals += [der(x)]
    xs += [x]
    z_vals += [0]
    cos_vals += [trueder(x)]
    in_vals += [integr(0, x)]


dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 12, -1.5, 1.5])

plt.title('sin(x), cos(x) and integral from 0 to x of d-sin(x)/dx')
plt.xlabel('x')
plt.ylabel('F(x)')

plt.xlim(min(xs), max(xs))

plt.plot(xs, cos_vals, color='yellow', linestyle='dashed',
    label='cos(x)')
plt.plot(xs, f_vals, color='red', linestyle='solid',
         label='cos(x)')
plt.plot(xs, der_vals, color='blue', linestyle='dashed',
    label='cos(x)')
plt.plot(xs, in_vals, color='brown', linestyle='dashed',
    label='cos(x)')

plt.plot(xs, z_vals, color='black', linestyle='dashed')
plt.show()

er = []
for i in range (100):

    def der(x):
        h = 10 ** (-(2 + i/10))
        der = (f(x + h) - f(x - h)) / (2 * h)
        return der

    error = 0

    for j in range(1000):
        x = (j) / 70
        error += (trueder(x) - der(x)) ** 2
    error = sqrt(error/1000)

    print(error, ',', 2+i/10)
    er += [error]
print(min(er))
errorint = 0
for j in range(1000):
    x = (j-500) / 70
    try:
        errorint += ((f(x) - integr(0, x))) ** 2
    except:
        errorint = errorint
print(sqrt(errorint / 1000))
