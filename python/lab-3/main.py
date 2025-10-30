def caesar_cipher(text: str, shift: int, lang: str) -> str:
    if lang == "en":
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif lang == "ru":
        alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        raise ValueError("Поддерживаются только языки: 'en' или 'ru'.")

    result = []
    alphabet_size = len(alphabet_lower)

    for ch in text:
        if ch in alphabet_lower:
            new_index = (alphabet_lower.index(ch) + shift) % alphabet_size
            result.append(alphabet_lower[new_index])
        elif ch in alphabet_upper:
            new_index = (alphabet_upper.index(ch) + shift) % alphabet_size
            result.append(alphabet_upper[new_index])
        else:
            result.append(ch)

    return "".join(result)


def main():
    filepath = input("Введите путь к исходному файлу: ").strip()
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        return

    try:
        shift = int(input("Введите величину сдвига (целое число): "))
    except ValueError:
        print("Ошибка: сдвиг должен быть целым числом.")
        return

    lang = input("Введите язык текста (en или ru): ").strip().lower()
    if lang not in ("en", "ru"):
        print("Ошибка: язык должен быть 'en' или 'ru'.")
        return

    encrypted_text = caesar_cipher(text, shift, lang)

    output_file = "encrypted.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted_text)

    print(f"Шифрование завершено. Результат сохранён в файл: {output_file}")


if __name__ == "__main__":
    main()
