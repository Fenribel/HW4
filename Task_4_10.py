from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x):
    try:
        return cosh(1/x)
    except:
        return inf

def trueder(x):
    try:
        return -sinh(1/x)/x**2
    except:
        return inf

def der(x):
    h = 10**(-8.1)
    der = (f(x+h)-f(x-h))/(2*h)
    return der



xs = []
f_vals = []
der_vals = []
cos_vals =[]
z_vals = []

for i in range (1000):
    x = (i-500)/70
    f_vals += [f(x)]
    der_vals += [der(x)]
    xs += [x]
    z_vals += [0]
    cos_vals += [trueder(x)]


dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 12, -1.5, 1.5])

plt.title('cosh(1/x), dcosh(1/x)/dx and -sinh(1/x)/x^2')
plt.xlabel('x')
plt.ylabel('F(x)')

plt.xlim(min(xs), max(xs))

plt.plot(xs, cos_vals, color='yellow', linestyle='dashed',
    label='cos(x)')
plt.plot(xs, f_vals, color='red', linestyle='solid',
         label='cos(x)')
plt.plot(xs, der_vals, color='blue', linestyle='dashed',
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