class Calculator:
    def convert_to_float(self, value: str) -> float:
        try:
            result = float(value)
            print(f'Конвертація успішна: {value} -> {result}')
            return result
        except ValueError as e:
            print(f'Помилка конвертації: {e}')
            return 0.0
        finally:
            print('Операція конвертації завершена.')

    def add(self, a: float, b: float) -> float:
        result = a + b
        print(f'{a} + {b} = {result}')
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        print(f'{a} - {b} = {result}')
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        print(f'{a} * {b} = {result}')
        return result

    def divide(self, a: float, b: float) -> float:
        try:
            result = a / b
            print(f'{a} / {b} = {result}')
            return result
        except ZeroDivisionError as e:
            print(f'Помилка ділення: {e}')
            return 0.0
        finally:
            print('Операція ділення завершена.')

calc = Calculator()

calc.convert_to_float("23.5")
calc.convert_to_float("23a")

calc.add(10, 5)
calc.subtract(10, 5)
calc.multiply(10, 5)
calc.divide(10, 5)
calc.divide(10, 0)
