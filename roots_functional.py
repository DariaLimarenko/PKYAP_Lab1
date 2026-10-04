import math
import sys
from typing import NamedTuple


class BiquadraticResult:
    """
    Варианты результата решения биквадратного уравнения.
    """

    NoRoots = NamedTuple("NoRoots", [])

    OneRoot = NamedTuple(
        "OneRoot",
        [("root", float)]
    )

    TwoRoots = NamedTuple(
        "TwoRoots",
        [
            ("root1", float),
            ("root2", float)
        ]
    )

    ThreeRoots = NamedTuple(
        "ThreeRoots",
        [
            ("root1", float),
            ("root2", float),
            ("root3", float)
        ]
    )

    FourRoots = NamedTuple(
        "FourRoots",
        [
            ("root1", float),
            ("root2", float),
            ("root3", float),
            ("root4", float)
        ]
    )


def get_coef(index, name, nonzero=False):
    """
    Читаем коэффициент из командной строки
    или вводим его с клавиатуры.

    Args:
        index (int): номер параметра командной строки
        name (str): название коэффициента
        nonzero (bool): запрет нулевого значения

    Returns:
        float: корректное значение коэффициента
    """
    value_str = None

    # Проверяем наличие коэффициента в командной строке
    if index < len(sys.argv):
        value_str = sys.argv[index]

    # Повторяем ввод до получения корректного значения
    while True:
        if value_str is None:
            value_str = input(
                f"Введите коэффициент {name}: "
            )

        try:
            # Преобразуем строку в действительное число
            value = float(value_str)

            # Исключаем значения inf и nan
            if not math.isfinite(value):
                raise ValueError

            # Коэффициент A не может быть равен нулю
            if nonzero and value == 0:
                print(
                    f"Коэффициент {name} "
                    f"не может быть равен нулю."
                )
            else:
                return value

        except ValueError:
            print(
                f"Некорректное значение "
                f"коэффициента {name}."
            )

        # Игнорируем ошибочное значение
        value_str = None


def get_x_roots(y):
    """
    Получаем действительные корни x
    для одного значения y = x^2.

    Args:
        y (float): корень вспомогательного уравнения

    Returns:
        tuple: кортеж действительных корней x
    """
    if y > 0:
        sqrt_y = math.sqrt(y)
        return -sqrt_y, sqrt_y

    if y == 0:
        return (0.0,)

    # При y < 0 действительных корней x нет
    return ()


def make_result(roots):
    """
    Преобразуем кортеж корней в один
    из вариантов результата.

    Для определения количества корней
    используется сопоставление с образцом.
    """
    match roots:
        case ():
            return BiquadraticResult.NoRoots()

        case (root,):
            return BiquadraticResult.OneRoot(root)

        case (root1, root2):
            return BiquadraticResult.TwoRoots(
                root1,
                root2
            )

        case (root1, root2, root3):
            return BiquadraticResult.ThreeRoots(
                root1,
                root2,
                root3
            )

        case (root1, root2, root3, root4):
            return BiquadraticResult.FourRoots(
                root1,
                root2,
                root3,
                root4
            )


def get_roots(A, B, C):
    """
    Вычисляем дискриминант и действительные корни
    биквадратного уравнения:

        A*x^4 + B*x^2 + C = 0.

    Выполняем замену y = x^2 и решаем
    квадратное уравнение:

        A*y^2 + B*y + C = 0.

    Args:
        A (float): коэффициент A
        B (float): коэффициент B
        C (float): коэффициент C

    Returns:
        tuple: дискриминант D и результат решения
    """
    # Вычисляем дискриминант
    D = B * B - 4 * A * C

    # При D < 0 действительных корней y нет
    if D < 0:
        return D, BiquadraticResult.NoRoots()

    # Находим корни вспомогательного уравнения
    if D == 0:
        y_values = (
            -B / (2 * A),
        )
    else:
        sqrt_D = math.sqrt(D)

        y_values = (
            (-B + sqrt_D) / (2 * A),
            (-B - sqrt_D) / (2 * A)
        )

    # Получаем действительные корни x
    roots = tuple(sorted(
        root
        for y in y_values
        for root in get_x_roots(y)
    ))

    return D, make_result(roots)


def print_result(A, B, C, D, result):
    """
    Выводим коэффициенты, дискриминант
    и действительные корни.

    Для выбора варианта вывода используется
    сопоставление с образцом.
    """
    print(
        f"Коэффициенты: "
        f"A = {A}, B = {B}, C = {C}"
    )

    print(f"Дискриминант: D = {D}")

    match result:
        case BiquadraticResult.NoRoots():
            print("Действительных корней нет.")

        case BiquadraticResult.OneRoot(root):
            print(
                f"Один действительный корень: "
                f"{root}"
            )

        case BiquadraticResult.TwoRoots(
            root1,
            root2
        ):
            print(
                f"Действительные корни (2): "
                f"{root1}, {root2}"
            )

        case BiquadraticResult.ThreeRoots(
            root1,
            root2,
            root3
        ):
            print(
                f"Действительные корни (3): "
                f"{root1}, {root2}, {root3}"
            )

        case BiquadraticResult.FourRoots(
            root1,
            root2,
            root3,
            root4
        ):
            print(
                f"Действительные корни (4): "
                f"{root1}, {root2}, "
                f"{root3}, {root4}"
            )


def main():
    """
    Основная функция программы.
    """
    # Получаем коэффициенты
    A = get_coef(1, "A", nonzero=True)
    B = get_coef(2, "B")
    C = get_coef(3, "C")

    # Вычисляем дискриминант и корни
    D, result = get_roots(A, B, C)

    # Выводим результат
    print_result(A, B, C, D, result)


if __name__ == "__main__":
    main()
