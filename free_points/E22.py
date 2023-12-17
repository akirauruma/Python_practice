def main():
    with open('p022_names.txt', 'r') as file:
        names = sorted(file.read().replace('"', '').split(','))

    total_score = sum((sum(ord(char) - ord('A') + 1 for char in name) * (i + 1)) for i, name in enumerate(names))

    print("сумма баллов по всем именам в файле:", total_score)


if __name__ == "__main__":
    main()
