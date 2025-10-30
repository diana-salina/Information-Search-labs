def get_positive_integer():
    while True:
        try:
            n = int(input("Введите количество строк треугольника Паскаля: "))
            if n > 0:
                return n
            else:
                print("Ошибка: нужно ввести целое положительное число больше 0.")
        except ValueError:
            print("Ошибка: нужно ввести целое положительное число.")

def pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)
    return triangle

def main():
    n = get_positive_integer()
    triangle = pascal_triangle(n)

    print("\nТреугольник Паскаля:")
    for row in triangle:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
