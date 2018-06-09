from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x):
    return fabs(x)

def der(x):
    h = 10**(-10)
    der = (f(x+h)-f(x-h))/(2*h)
    return der

xs = []
f_vals = []
der_vals = []
z_vals = []

for i in range (100000):
    x = -50000/7000 + i/7000
    f_vals += [f(x)]
    der_vals += [der(x)]
    xs += [x]
    z_vals += [0]


dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 12, -1.5, 1.5])

plt.title('|x| and derivative')
plt.xlabel('x')
plt.ylabel('F(x)')

plt.xlim(min(xs), max(xs))

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
        x = j / 70
        try:
            error += (fabs(x)/x - der(x)) ** 2
        except:
            print('zero lol')
    error = sqrt(error/1000)

    print(error, ',', 2+i/10)
    er += [error]
print(min(er))