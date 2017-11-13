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
Stefan_Bolzman = 5.6704e-8  # Вт / (м^2 * К^4)

# geometry, m
width, length, high = 0.1, 0.1, 0.1

# температура печі
T_furnace = 600 + 273.0  # K
T_specimen = 20 + 273.0  # K
DeltaT = 1  # %

# Розрахунок площі поверхні та маси зразка
square = (width * length + width * high + length * high) * 2
volume = width * length * high
mass = volume * density

# Визначити температуру закінчення розрахунків Тк
T_last = (1 - 0.01 * DeltaT) * T_furnace

# розрахунок середньої теплоємності через лінійний закон
heat_capacity_line = np.poly1d(np.polyfit([300, 800], heat_capacity, 1))
heat_capacity_mean = heat_capacity_line(np.mean([T_furnace, T_specimen]))

# розрахунок коефіцієнта k
k = alpha * square / (heat_capacity_mean * mass)

#  Розрахувати час нагріву
heat_time = -log((T_furnace - T_last) / (T_furnace - T_specimen)) / k

# for plotting
lab1_x = np.arange(0, heat_time, 0.5)
lab1_y = T_furnace - (T_furnace - T_specimen) * np.exp(-k * lab1_x)

if __name__ == '__main__':

    # plotting
    plt.plot(lab1_x, lab1_y - 273.0)
    plt.xticks(np.arange(lab1_x[0], lab1_x[-1] + 60, 120))
    plt.yticks(np.arange(0, 601, 50))

    plt.title("Процес нагрівання")
    plt.ylabel(u"Температура нагріву, ℃")
    plt.xlabel(u"Час нагріву, c")
    plt.grid()
    plt.tight_layout(0.2)
    plt.show()

    # print variables
    print(f'm = {round(mass, 3)} g\n'
          f'k = {round(k, 3)}\n'
          f'T_k = {int(T_last)}\n'
          f'Час нагріву: {int(heat_time)} с\n')
