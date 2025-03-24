from sympy import sympify

text = input("Напишите пример:")
expr = sympify(text)
result = expr.evalf(2)
print(float(result))



