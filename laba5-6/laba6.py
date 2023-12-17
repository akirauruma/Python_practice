import math
import numpy as np

def calculate_vapor_pressure(T, units='mmHg'):
    T_c = 617.1  # Критическая температура
    P_c = 35.6  # Критическое давление
    coefficients = {
        'A_plus': 10.353,
        'B_plus': 10.649,
        'C_plus': -5.136,
        'D_plus': 0.2958
    }

    T_r = T / T_c  # Безразмерная температура
    P_vp_r = math.exp(coefficients['A_plus'] - coefficients['B_plus'] / T_r + coefficients['C_plus'] * math.log(T_r) + coefficients['D_plus'] * T_r ** 6)  # Безразмерное давление паров

    units_conversion = {
        'Pa': P_vp_r * P_c * 1.01325 * 1e5,
        'atm': P_vp_r * P_c,
        'mmHg': P_vp_r * P_c * 760
    }

    P_vp = units_conversion.get(units, units_conversion['mmHg'])  # По умолчанию в мм. рт. ст.

    return P_vp

# Пример использования:
temperature_range = np.arange(273, 474, 10)

# Вывод давления паров в столбце
for temp in temperature_range:
    vapor_pressure_mmHg = calculate_vapor_pressure(temp)
    vapor_pressure_Pa = calculate_vapor_pressure(temp, 'Pa')
    vapor_pressure_atm = calculate_vapor_pressure(temp, 'atm')
    print(f'Temperature: {temp} K, Vapor Pressure (mmHg): {vapor_pressure_mmHg}, Vapor Pressure (Pa): {vapor_pressure_Pa}, Vapor Pressure (atm): {vapor_pressure_atm}')
