import math
import numpy as np


def calculate_vapor_pressure(T, A_plus, B_plus, C_plus, D_plus, T_c, P_c, units='mm.rt.st'):
    T_r = T / T_c
    P_vp_r = math.exp(A_plus - B_plus / T_r + C_plus * math.log(T_r) + D_plus * T_r ** 6)

    units_conversion = {
        'Pa': P_vp_r * P_c * 1.01325 * 1e5,
        'atm': P_vp_r * P_c,
        'mm.rt.st': P_vp_r * P_c * 760
    }

    P_vp = units_conversion.get(units, units_conversion['mm.rt.st'])

    return P_vp


def main():
    try:
        with open('parameters.txt', 'r') as params_file:
            params_lines = params_file.readlines()

        T_c, P_c, A_plus, B_plus, C_plus, D_plus = map(
            float, [line.split(': ')[1] for line in params_lines])

        start_temp = float(input('Vvedite first temparutere point: '))
        end_temp = float(input('Vvedite last temperature point: '))
        num_points = int(input('Vvedite shag: '))

        temperature_range = np.arange(start_temp, end_temp + 1, num_points)

        # Расчет и вывод результатов
        with open('results.txt', 'w') as output_file:
            output_file.write('Temperature (K)\tVapor Pressure (mmHg)\tVapor Pressure (Pa)\tVapor Pressure (atm)\n')
            for temp in temperature_range:
                vapor_pressure_mmHg = round(
                    calculate_vapor_pressure(temp, A_plus, B_plus, C_plus, D_plus, T_c, P_c, 'mm.rt.st'))
                vapor_pressure_Pa = round(
                    calculate_vapor_pressure(temp, A_plus, B_plus, C_plus, D_plus, T_c, P_c, 'Pa'))
                vapor_pressure_atm = round(
                    calculate_vapor_pressure(temp, A_plus, B_plus, C_plus, D_plus, T_c, P_c, 'atm'))

                output_file.write(f'{temp}\t{vapor_pressure_mmHg}\t{vapor_pressure_Pa}\t{vapor_pressure_atm}\n')

        print('\nРезультаты сохранены в файл: results.txt')

    except ValueError as e:
        print(f'Wrong value: {e}')

    except FileNotFoundError:
        print('File not found.')

    except Exception as e:
        print(f'proizoshla oshibka: {e}')


if __name__ == "__main__":
    main()
