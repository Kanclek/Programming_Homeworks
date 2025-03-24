from sympy import sympify

class Calculator:

    def __init__(self, text):
        '''Принимает стоку-выражение str и вызывает вычисления'''
        self.__text = text
        self.__result = self.calculate()
        if round(self.__result) == self.__result:
            self.__result = int(self.__result)

        print(text, " = ", self.__result)

    def calculate(self):
        '''Вычисление значения, возвращает float'''
        expr = sympify(self.__text)
        result = expr.evalf(2)
        return float(result)

    def __doc__(self):
        text = '''
        Принимает стоку-выражение типа:
         A оператор B
         или для унарных операторов
         оператор(A)
         
         Вычисляет значение
        '''
        return text


text = input("Напишите пример:")

instance = Calculator(text)
print(instance.__doc__())

