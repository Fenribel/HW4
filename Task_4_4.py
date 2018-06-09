from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x):
    return exp(x)

lg_er = []
lg_h_list = []
for i in range (300000):
    h = 10 ** (-i / 1000)
    def der(x):
        der = (f(x + h) - f(x - h)) / (2 * h)
        return der

    error = 0

    for j in range(1000):
        x = j / 70
        error += (exp(x) - der(x)) ** 2
    error = sqrt(error/1000)

    lg_er += [log10(error)]
    lg_h_list += [-log10(h)]


dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 12, -1.5, 1.5])

plt.title('')
plt.xlabel('-lg(h)')
plt.ylabel('lg(error^2)')

plt.xlim(min(lg_h_list), max(lg_h_list))
plt.ylim(min(lg_er), max(lg_er))
plt.plot(lg_h_list, lg_er, color='red', linestyle='solid',
    label='cos(x)')
plt.show()