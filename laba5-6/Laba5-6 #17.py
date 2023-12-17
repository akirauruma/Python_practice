import math


def calculate_vapor_pressure(t, units='mm.rt.st'):
    T_c = 617.1
    P_c = 35.6
    A_plus = 10.353
    B_plus = 10.649
    C_plus = -5.136
    D_plus = 0.2958

    T_r = t / T_c
    P_vp_r = math.exp(A_plus - B_plus / T_r + C_plus * math.log(T_r) + D_plus * T_r ** 6)  # Безразмерное давление паров

    if units == 'Pa':
        P_vp = P_vp_r * P_c * 1.01325 * 1e5
    elif units == 'atm':
        P_vp = P_vp_r * P_c
    else:
        P_vp = P_vp_r * P_c * 760

    return P_vp


#
temperature_range = range(273, 474, 10.5)


result_list = list(map(lambda temp: (temp, calculate_vapor_pressure(temp)), temperature_range))
for temp, pressure in result_list:
    print(f'Temperature: {temp} K, Vapor Pressure (mm.rt.st): {pressure} mm.rt.st')


vapor_pressure_Pa_list = list(map(lambda temp: (temp, calculate_vapor_pressure(temp, 'Pa')), temperature_range))
for temp, pressure in vapor_pressure_Pa_list:
    print(f'Temperature: {temp} K, Vapor Pressure (Pa): {pressure} Pa')


vapor_pressure_atm_list = list(map(lambda temp: (temp, calculate_vapor_pressure(temp, 'atm')), temperature_range))
for temp, pressure in vapor_pressure_atm_list:
    print(f'Temperature: {temp} K, Vapor Pressure (atm): {pressure} atm')
