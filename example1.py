from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def Calculate_SquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Вычисляет корень."""
    if your_number <= 0:
        return

    root = Calculate_SquareRoot(your_number)
    print('Мы вычислили корень квадратный из введенного вами числа. '
          f'Это будет: {root}')


print(message)
calc(25.5)