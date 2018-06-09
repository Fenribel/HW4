from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x):
    return sin(x)

def der(x):
    h = 10**(-5.06)
    der = (2*f(x+h) + f(x+2*h) - 2*f(x-h) - f(x+2*h))/(4*h)
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
    cos_vals += [cos(x)]


dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 12, -1.5, 1.5])

plt.title('sin(x), dsin(x)/dx and cos(x)')
plt.xlabel('x')
plt.ylabel('F(x)')

plt.xlim(0, max(xs))

plt.plot(xs, cos_vals, color='yellow', linestyle='dashed',
    label='cos(x)')
plt.plot(xs, f_vals, color='red', linestyle='solid',
         label='cos(x)')
plt.plot(xs, der_vals, color='blue', linestyle='dashed',
    label='cos(x)')

plt.plot(xs, z_vals, color='black', linestyle='dashed')
plt.show()

er = []
for i in range (10000):

    def der(x):
        h = 10 ** (-(2 + i/100))
        der = (2 * f(x + h) + f(x + 2 * h) - 2 * f(x - h) - f(x + 2 * h)) / (4 * h)
        return der

    error = 0

    for j in range(1000):
        x = j / 70
        error += (cos(x) - der(x)) ** 2
    error = sqrt(error/1000)

    print(error, ',', 2+i/100)
    er += [error]
print(min(er))