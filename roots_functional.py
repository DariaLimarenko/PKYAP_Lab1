import math
import sys
from typing import NamedTuple


class BiquadraticResult:
    """Возможные результаты решения биквадратного уравнения."""

    NoRoots = NamedTuple("NoRoots", [])
    OneRoot = NamedTuple("OneRoot", [("root", float)])
    TwoRoots = NamedTuple(
        "TwoRoots",
        [("root1", float), ("root2", float)],
    )
    ThreeRoots = NamedTuple(
        "ThreeRoots",
        [("root1", float), ("root2", float), ("root3", float)],
    )
    FourRoots = NamedTuple(
        "FourRoots",
        [
            ("root1", float),
            ("root2", float),
            ("root3", float),
            ("root4", float),
        ],
    )


def get_coef(index, name, nonzero=False):
    """Читает и проверяет один коэффициент."""
    value_str = sys.argv[index] if index < len(sys.argv) else None

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


def make_result(roots):
    """Преобразует кортеж корней в один из вариантов результата."""
    match roots:
        case ():
            return BiquadraticResult.NoRoots()
        case (root,):
            return BiquadraticResult.OneRoot(root)
        case (root1, root2):
            return BiquadraticResult.TwoRoots(root1, root2)
        case (root1, root2, root3):
            return BiquadraticResult.ThreeRoots(root1, root2, root3)
        case (root1, root2, root3, root4):
            return BiquadraticResult.FourRoots(root1, root2, root3, root4)


def get_x_roots(y):
    """Возвращает кортеж действительных корней для значения y."""
    if y > 0:
        sqrt_y = math.sqrt(y)
        return -sqrt_y, sqrt_y
    if y == 0:
        return (0.0,)
    return ()


def get_roots(A, B, C):
    """Вычисляет дискриминант и результат решения уравнения."""
    D = B * B - 4 * A * C

    if D < 0:
        return D, BiquadraticResult.NoRoots()

    if D == 0:
        y_values = (-B / (2 * A),)
    else:
        sqrt_D = math.sqrt(D)
        y_values = (
            (-B + sqrt_D) / (2 * A),
            (-B - sqrt_D) / (2 * A),
        )

    roots = tuple(sorted(
        root
        for y in y_values
        for root in get_x_roots(y)
