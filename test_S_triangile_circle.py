from S_triangle_circle import S_triangle_and_circle

def test_S_triangle():
    obj = S_triangle_and_circle()

    assert obj.S_triangle("1", 12, True) == "TypeError: Нужно ввести только числа!"
    assert obj.S_triangle(23, 12, 10) == "Такого треугольника не существует!"
    assert obj.S_triangle(-5, -12, -13) == "Такого треугольника не существует!"
    assert obj.S_triangle(5, 12, 13) == 30.0

    assert obj.S_circle(10) == 314.159
    assert obj.S_circle(0) == "Такого радиуса нет!"
    assert obj.S_circle(-12) == "Такого радиуса нет!"
    assert obj.S_circle(None) == "TypeError: Нужно ввести только число!"


# Для теста в терминале ввести: pytest test_S_triangile_circle.py