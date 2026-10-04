import math
import sys


class BiquadraticEquation:
    """Класс для решения биквадратного уравнения."""

    def __init__(self):
        """Инициализирует коэффициенты, дискриминант и список корней."""
        self.A = 0.0
        self.B = 0.0
        self.C = 0.0
        self.D = 0.0
        self.roots = []

    def get_coef(self, index, name, nonzero=False):
        """Читает и проверяет один коэффициент."""
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

    def get_coefs(self):
        """Получает коэффициенты A, B и C."""
        self.A = self.get_coef(1, "A", nonzero=True)
        self.B = self.get_coef(2, "B")
        self.C = self.get_coef(3, "C")

    def calculate_roots(self):
        """Вычисляет дискриминант и действительные корни уравнения."""
        self.D = self.B * self.B - 4 * self.A * self.C
        self.roots = []

        if self.D < 0:
            return

        if self.D == 0:
            y_values = [-self.B / (2 * self.A)]
        else:
            sqrt_D = math.sqrt(self.D)
            y_values = [
                (-self.B + sqrt_D) / (2 * self.A),
                (-self.B - sqrt_D) / (2 * self.A),
            ]

        for y in y_values:
            if y > 0:
                sqrt_y = math.sqrt(y)
                self.roots.extend([-sqrt_y, sqrt_y])
            elif y == 0:
                self.roots.append(0.0)

        self.roots.sort()

    def print_result(self):
        """Выводит коэффициенты, дискриминант и действительные корни."""
        print(
            f"Коэффициенты: A = {self.A}, "
            f"B = {self.B}, C = {self.C}"
        )
        print(f"Дискриминант: D = {self.D}")

        number_of_roots = len(self.roots)
        if number_of_roots == 0:
            print("Действительных корней нет.")
        elif number_of_roots == 1:
            print(f"Один действительный корень: {self.roots[0]}")
        else:
            roots_str = ", ".join(str(root) for root in self.roots)
            print(f"Действительные корни ({number_of_roots}): {roots_str}")


def main():
    """Основная функция программы."""
    equation = BiquadraticEquation()
    equation.get_coefs()
    equation.calculate_roots()
    equation.print_result()


if __name__ == "__main__":
    main()
