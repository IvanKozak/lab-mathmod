# importing
from lab1 import *

# fit_a[1] = c_ave
# fit_a[0] = 0
# const_SB = 0

fit_a_list = [[hcap_av, 0], fit_a, fit_a]
const_SB_list = [0, 0, 5.6704e-8]
j = 0
for a_list, const_SB in zip(fit_a_list, const_SB_list):
    fit_a = a_list

    k1, k2 = alpha * square / mass, const_SB * thermal_emissivity * square / mass # коефіцієнти
    step = 10  # крок

    time_array = np.array([0])
    temp_array = np.array([T_spec])
    i = 0
    while True:
        k1_part = k1 * (T_furn - temp_array[i])
        k2_part = k2 * (T_furn ** 4 - temp_array[i] ** 4)
        func_iter = (k1_part + k2_part) / hcap_line(temp_array[i])
        func_temp = temp_array[i] + step * func_iter
        if func_temp >= T_last:
            break
        temp_array = np.append(temp_array, func_temp)
        i += 1
        time_array = np.append(time_array, i * step)

    # plotting
    plt.plot(x, y)
    plt.plot(time_array, temp_array)
    plt.xticks(np.arange(x[0], x[-1] + 60, 120))
    plt.yticks(np.arange(temp_array[0], temp_array[-1], 50))

    plt.title("Процес нагрівання")
    plt.ylabel(u"Температура нагріву, ℃")
    plt.xlabel(u"Час нагріву, c")
    plt.grid()
    plt.tight_layout(0.2)
    plt.show()

    fmt = "pdf"
    plt.savefig("fig2_T-t." + fmt, format=fmt)
    j += 1

    # %% print variables
    print(f'm = {round(mass, 3)} kg\n'
          # f'k = {round(k, 3)}\n'
          f'T_k = {int(T_last)}\n'
          f'Час нагріву: {int(time_array[-1])} с\n')
