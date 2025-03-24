from sympy import sympify, ask, Q
import sympy
import os
import logging

logging.basicConfig(filename="app.log",
                    filemode="w",
    level=logging.ERROR)


logger1 = logging.getLogger("Logging1")
logger1.setLevel(logging.DEBUG)



class Calculator:
    def __new__(cls, *args, **kwargs):
        logger1.debug("Create Calculator instance")
        return super().__new__(cls)


    def __init__(self, filename):
        '''Принимает стоку-выражение str и вызывает вычисления'''
        with open(filename, "r") as file:
            self.__text = tuple(map(str.strip, file.readlines()))
            logger1.info("Reading File")
        self.__result = []
        for i, line in enumerate(self.__text, start=1):
            logger1.info("Start calculation in File")
            try:
                result = self.calculate(line)
                if round(result) == result:
                    result = int(result)

                res = line  + " = " + str(result)
                self.__result.append(res)
            except ZeroDivisionError:
                logger1.error(f"Deviding by zero on {i} line")
            except ValueError:
                logger1.error(f"Value Error on {i} line")
            except TypeError:
                logger1.error(f"Operation is not implemented on {i} line")

    def calculate(self, text):
        '''Вычисление значения, возвращает float'''
        logger1.debug(f"Calculating text: {text}")
        expr = sympify(text)
        result = expr.evalf(2)
        if result == sympy.zoo:
            raise ZeroDivisionError
        if isinstance(result, (sympy.core.numbers.ComplexInfinity, sympy.core.add.Add)):
            raise ValueError
        elif not isinstance(result, sympy.core.numbers.Float):
            raise TypeError

        return float(result)

    @property
    def result(self):
        return "\n".join(self.__result)

    def __doc__(self):
        text = '''
        Принимает стоку-выражение типа:
         A оператор B
         или для унарных операторов
         оператор(A)
         
         Вычисляет значение
        '''
        return text




instance = Calculator(os.path.join(os.getcwd(), "examples.txt"))


