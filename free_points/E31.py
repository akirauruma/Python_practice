counter = 0  # подсчет кол-ва способов

for a in range(3):  # перебор монет номиналом один фунт (от 0 до 2)
    for b in range(1 + (200 - 100 * a) // 50):  # перебор 50 пенсов
        for c in range(1 + (200 - 100 * a - 50 * b) // 20):  # перебор 20 пенсов
            for d in range(1 + (200 - 100 * a - 50 * b - 20 * c) // 10):  # перебор 10 пенсов
                for e in range(1 + (200 - 100 * a - 50 * b - 20 * c - 10 * d) // 5):  # перебор 5 пенсов
                    for f in range(1 + (200 - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e) // 2):  # перебор 2 пенсов
                        counter += 1

print(counter + 1)