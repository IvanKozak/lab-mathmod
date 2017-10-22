import numpy as np
import matplotlib.pyplot as plt
from lab1 import *

def ai(i):
    return f + f / i

def ci(i):
    return f - f / i

# вхідні дані для розрахунку
# інші дані є в lab1
radius = 0.05  # m
length = 0.1  # m

# розрахунок середньої теплоємності через лінійний закон
fit_lambda = np.polyfit([300, 800], therm_conduct, 1)
lambda_line = np.poly1d(fit_lambda)
thermcon = lambda_line(np.mean([T_spec, T_furn]))

a = thermcon / (hcap_av * density)

# coord step
N = np.arange(0, 3)
h = radius / len(N)

# time step from model accuracy condition
tau = (h ** 2) / (2 * a)

# time steps count
M = int(t_heat / tau)
M = np.arange(0, M)
# finding f
f = (a * tau) / (h ** 2)

# Введення початкових умов
T_arr = np.full((len(M), len(N)), T_spec)

# розрахунок масиву T_arr
bi = 1 - 2 * f
nested_k1 = (1 - 2 * f * (1 + alpha * h / thermcon))
nested_k2 = 2 * f * T_furn * alpha * h / thermcon
for j in M[1::]:

    # розраховуємо температури в граничних точках
    T_arr[j][0] = bi * T_arr[j-1][0] + 2 * f * T_arr[j-1][1]
    T_arr[j][-1] = 2 * f * T_arr[j-1][-2] + nested_k1 * T_arr[j-1][-1] + nested_k2

    # розраховуємо НЕ крайові температури
    for i in N[1:-1]:
        T_arr[j][i] = ai(i) * T_arr[j-1][i+1] + bi * T_arr[j-1][i] + ci(i) * T_arr[j-1][i-1]

print(T_arr)