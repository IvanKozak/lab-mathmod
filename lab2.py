# importing
from lab1 import *

# fit_a[1] = c_ave
# fit_a[0] = 0
# const_SB = 0

def lab2_data(a0, a1, epsilon):
    # коефіцієнти
    k1 = alpha * square / mass
    k2 = Stefan_Bolzman * epsilon * square / mass
    step = 10  # крок

    time_array = [0]
    i = 0

    T_array = [T_specimen]
    T_next = T_array[0]

    while T_next <= T_last:
        T_next = T_next + step * (k1 * (T_furnace - T_next) +
                                  k2 * (T_furnace ** 4 - T_next ** 4)
                                  ) / (a0 + a1 * T_next)
        T_array.append(T_next)
        time_array.append(step*i)
    return time_array, T_array

lab2_data(0, heat_capacity_mean, 0)

