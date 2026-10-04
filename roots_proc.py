import math
import sys


def get_coef(index, name, nonzero=False):
    """Получает коэффициент из командной строки или с клавиатуры."""
    value_str = None

    if index < len(sys.argv):
        value_str = sys.argv[index]

    while True:
        if value_str is None:
            value_str = input(f"Введите коэффициент {name}: ")

        try:
            value = float(value_str)
            if not math.isfinite(value):
                raise ValueError
            if nonzero and value == 0:
                print(f"Коэффициент {name} не может быть равен нулю.")
            else:
                return value
        except ValueError:
            print(f"Некорректное значение коэффициента {name}.")

        value_str = None


def get_roots(A, B, C):
    """Вычисляет дискриминант и действительные корни уравнения."""
    D = B * B - 4 * A * C

    if D < 0:
        return D, []

    if D == 0:
        y_values = [-B / (2 * A)]
    else:
        sqrt_D = math.sqrt(D)
        y_values = [
            (-B + sqrt_D) / (2 * A),
            (-B - sqrt_D) / (2 * A),
        ]

    roots = []
    for y in y_values:
        if y > 0:
            sqrt_y = math.sqrt(y)
            roots.extend([-sqrt_y, sqrt_y])
        elif y == 0:
            roots.append(0.0)

    roots.sort()
    return D, roots


def print_result(A, B, C, D, roots):
    """Выводит коэффициенты, дискриминант и действительные корни."""
    print(f"Коэффициенты: A = {A}, B = {B}, C = {C}")
    print(f"Дискриминант: D = {D}")

    number_of_roots = len(roots)
    if number_of_roots == 0:
        print("Действительных корней нет.")
    elif number_of_roots == 1:
        print(f"Один действительный корень: {roots[0]}")
    else:
        roots_str = ", ".join(str(root) for root in roots)
        print(f"Действительные корни ({number_of_roots}): {roots_str}")


def main():
    """Основная функция программы."""
    A = get_coef(1, "A", nonzero=True)
    B = get_coef(2, "B")
    C = get_coef(3, "C")

    D, roots = get_roots(A, B, C)
    print_result(A, B, C, D, roots)


if __name__ == "__main__":
    main()
