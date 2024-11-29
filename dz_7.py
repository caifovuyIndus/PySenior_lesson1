numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('before', numbers)


def set_up_operation(operation: str, value: float):

    def validate_number(n):
        if not isinstance(n, (int, float)):
            try:
                n = float(n)
            except ValueError:
                raise ValueError(f"Значення '{n}' неможливо перетворити до числа.")
        return n

    def safe_divide(n, value):
        if value == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return n / value

    def apply_operation(n):
        n = validate_number(n)
        if operation == '+':
            return n + value
        elif operation == '-':
            return n - value
        elif operation == '*':
            return n * value
        elif operation == '/':
            return safe_divide(n, value)
        else:
            raise ValueError(f"Операція '{operation}' не підтримується.")

    return apply_operation


def check_n(n):
    return n >= 5


add = set_up_operation('+', 2)
subtract = set_up_operation('-', 2)
multiply = set_up_operation('*', 2)
divide = set_up_operation('/', 2)

numbers_add = [add(n) for n in numbers if check_n(n)]
numbers_subtract = [subtract(n) for n in numbers if check_n(n)]
numbers_multiply = [multiply(n) for n in numbers if check_n(n)]
numbers_divide = [divide(n) for n in numbers if check_n(n)]

print('add', numbers_add)
print('subtract', numbers_subtract)
print('multiply', numbers_multiply)
print('divide', numbers_divide)
