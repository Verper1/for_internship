# Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу
# и треугольника по трем сторонам.
# Дополнительно к работоспособности оценим:
# - Юнит-тесты
# - Легкость добавления других фигур
# - Вычисление площади фигуры без знания типа фигуры в compile-time
# - Проверку на то, является ли треугольник прямоугольным

from math import sqrt, pi


class S_triangle_and_circle:
    def S_triangle(self, a: int | float, b: int | float, c: int | float):
        """
        Метод, позволяющий найти площадь треугольника по трём сторонам и проверяющий прямоугольный ли треугольник.

        :param a: Сторона треугольника A
        :param b: Сторона треугольника B
        :param c: Сторона треугольника C
        :return: Площадь треугольника
        """

        try:
            if (a + b < c or c + b < a or c + a < b) or (a < 0 and b < 0 and c < 0):
                output = "Такого треугольника не существует!"
                return output
            elif c ** 2 == (a ** 2 + b ** 2):  # Проверка на прямоугольный треугольник
                output = round(a * b / 2, 3)
                return output
            else:
                p2 = (a + b + c) / 2
                output = round(sqrt(p2 * (p2 - a) * (p2 - b) * (p2 - c)), 3)
                return output
        except TypeError:
            return "TypeError: Нужно ввести только числа!"
        except Exception as e:
            return f"Ошибка: Непредвиденная ошибка! {e}"

    def S_circle(self, r: int | float):
        """
        Метод, позволяющий найти площадь круга по радиусу.

        :param r: Радиус круга
        :return: Площадь круга
        """

        try:
            if r <= 0:
                return "Такого радиуса нет!"
            else:
                output = round(pi * r ** 2, 3)
                return output
        except TypeError:
            return "TypeError: Нужно ввести только число!"
        except Exception as e:
            return f"Ошибка: Непредвиденная ошибка! {e}"
