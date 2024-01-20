import matplotlib.pyplot as plt
from math import *

def point_milieu(f, tt, h, y0):
    yy = [y0, y0 + h * f(tt[0],y0)]
    for i in range(len(tt) - 1):
        yy.append(yy[i] + 2 * h * f(tt[i + 1], yy[i + 1]))
    return yy

def adams_bashforth_pas_de_2(f, tt, h, y0):
    yy = [y0, y0 + h**f(tt[0],y0)]
    for i in range(len(tt) - 1):
        yy.append(yy[i + 1] + 0.5 * h * (3 * f(tt[i + 1], yy[i + 1]) + f(tt[i], yy[i])))
    return yy

def adams_bashforth_pas_de_3(f, tt, h, y0):
    yy = [y0, y0 + h * f(tt[0], y0), y0 + h * f(tt[0], y0) + 0.5 * h * (3 * f(tt[1], y0 + h * f(tt[0], y0)) - f(tt[0], y0))]
    for i in range(len(tt) - 2):
        yy.append(yy[i + 2] + (1/12) * h * (23 * f(tt[i + 2], yy[i + 2]) - 16 * f(tt[i + 1], yy[i + 1]) + 5 * f(tt[i], yy[i])))
    return yy

def f(tt, y):
    # Définissez votre fonction ici
    # Par exemple, retournez une expression impliquant tt et y
    return tt + y

# Exemple d'utilisation :
print(point_milieu(f, [0, 1, 2, 3], 0.5, 1.0))
print(adams_bashforth_pas_de_2(f, [0, 1, 2, 3], 0.5, 1.0))
print(adams_bashforth_pas_de_3(f, [0, 1, 2, 3], 0.5, 1.0))


 