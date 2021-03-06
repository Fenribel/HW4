from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x):
    return exp(x)

def der(x):
    h = 10**(-6.9)
    der = (f(x+h)- 2 * f(x) + f(x-h))/(h**2)
    return der

xs = []
f_vals = []
der_vals = []
cos_vals =[]
z_vals = []

for i in range (1000):
    x = i/70
    f_vals += [f(x)]
    der_vals += [der(x)]
    xs += [x]
    z_vals += [0]


dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 12, -1.5, 1.5])

plt.title('exp(x), dexp(x)/dx')
plt.xlabel('x')
plt.ylabel('F(x)')

plt.xlim(0, max(xs))

plt.plot(xs, f_vals, color='red', linestyle='solid',
         label='cos(x)')
plt.plot(xs, der_vals, color='blue', linestyle='dashed',
    label='cos(x)')

plt.plot(xs, z_vals, color='black', linestyle='dashed')
plt.show()

er = []
for i in range (100):

    def der(x):
        h = 10 ** (-(2+ i/10))
        der = (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
        return der

    error = 0

    for j in range(1000):
        x = j / 70
        error += (exp(x) - der(x)) ** 2
    error = sqrt(error/1000)

    print(error, ',', 2+i/10)
    er += [error]
print(min(er))