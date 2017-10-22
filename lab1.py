# coding=utf-8

# %% importing
from math import log
import numpy as np
import matplotlib.pyplot as plt

# Defining variables
# Материал Cu
# material constants
density = 8873  # густина металу кг/м3
alpha = 200  # Вт*м-2*К-1
heat_capacity = [385, 442]  # 300 K and 800 K
thermal_emissivity = 0.78  # для міді (epsilon)
therm_conduct = [401, 366]  # W m-1 K-1 300 K and 800 K lambda

# constants
const_SB = 5.6704e-8  # Вт / (м^2 * К^4)

# geometry, m
width, length, high = 0.1, 0.1, 0.1

# температура печі
T_furn = 600 + 273.0  # K
T_spec = 20 + 273.0  # K
DeltaT = 1  # %

# Розрахунок площі поверхні та маси зразка
square = (width * length + width * high + length * high) * 2
volume = width * length * high
mass = volume * density

# Визначити температуру закінчення розрахунків Тк
B = 1 - 0.01 * DeltaT
T_last = B * T_furn

# розрахунок середньої теплоємності через лінійний закон
fit_a = np.polyfit([300, 800], heat_capacity, 1)
hcap_line = np.poly1d(fit_a)
hcap_av = hcap_line(np.mean([T_furn, T_spec]))

# розрахунок коефіцієнта k
k = alpha * square / (hcap_av * mass)

#  Розрахувати час нагріву
in_ln = (T_furn - T_last) / (T_furn - T_spec)
t_heat = - log(in_ln) / k

# for plotting
x = np.arange(0, t_heat, 0.5)
y = T_furn - (T_furn - T_spec) * np.exp(-k * x)

if __name__ == '__main__':

    # plotting
    plt.plot(x, y)
    plt.xticks(np.arange(x[0], x[-1] + 60, 120))
    plt.yticks(np.arange(y[0], y[-1], 50))

    plt.title("Процес нагрівання")
    plt.ylabel(u"Температура нагріву, ℃")
    plt.xlabel(u"Час нагріву, c")
    plt.grid()
    plt.tight_layout(0.2)
    plt.show()

    fmt = "pdf"
    plt.savefig("fig2_T-t."+fmt, format=fmt)

    # print variables
    print(f'm = {round(mass, 3)} g\n'
          f'k = {round(k, 3)}\n'
          f'T_k = {int(T_last)}\n'
          f'Час нагріву: {int(t_heat)} с\n')
