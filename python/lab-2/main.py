def is_valid_brackets(seq):
    balance = 0
    for ch in seq:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1

        if balance < 0:
            return False
    return balance == 0


def choice_input_type():
    choice = input(f"Введите\n1: ввести строку вручную\n2: прочитать из файла\nВаш выбор: ")

    if choice == "1":
        return input("Введите скобочную последовательность: ").strip()
    elif choice == "2":
        filename = input("Введите имя файла: ").strip()
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            print("Ошибка: файл не найден.")
            return None
    else:
        print("Некорректный выбор.")
        return None


def main():
    seq = choice_input_type()
    if seq is None:
        return

    if is_valid_brackets(seq):
        print(f'"{seq}" - Правильная последовательность')
    else:
        print(f'"{seq}" - Неправильная последовательность')


if __name__ == "__main__":
    main()
