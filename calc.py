import sympy as sp

def calculate_derivative(expression, variabe):
    try:
        var = sp.symbols(variabe) #Обозначаем с каким символом или переменной будем работать(х, у или т.д.)
        expr = sp.sympify(expression) #Преобразуем в математическое выражение
        derivative = sp.diff(expr, var)
        return f"Производная f({variabe})={expression} по {variable}: f'({variable}) = {derivative}"
    except Exception as e:
        print(f'Ошибка: {e}')

def calculate_integral(expression, variable, limits = None):
    try:
        var = sp.symbols(variable)
        expr = sp.sympify(expression)
        if limits:
            lower, upper = map(float, limits.split(',')) #Преобразуем пределы(от lower-нижнего до upper-верхнего)
            integral = sp.integrate(expr, (var, lower, upper))
            integral_str = str(integral).replace('log', 'ln') # Заменяем log(x) на ln(x) в итоговом выражении
            return f'Вычисляем определённый интеграл S({expr} по {var} от {int(lower)}-нижнего предела до {int(upper)}-верхнего предела) dx = {integral_str} + C'
        else:
            integral = sp.integrate(expr, var)
            integral_str = str(integral).replace('log', 'ln')
            return f'Вычисляем неопределённый интеграл S({expr})dx по {var} = {integral_str} + C' 
    except Exception as e:
        print(f'Ошибка: {e}')

print('1. Проиводные')
print('2. Интеграл')
user = input('С какими функциями будем работать(1 или 2)? ')

if user == '1':
    print('Производные')
    variable = input('Введите переменную, с которой вы будете проводить вычисление(x, y или др.): ')
    expression = input("Введите выражение (например, x**2 + 3*x + 5): ").strip()
    result = calculate_derivative(expression, variable)
    print(result)

elif user == '2':
    print('Интеграл')
    variable = input('Введите переменную, через которую вы хотите произвести решение(например, х, у или др.): ')
    expression = input('Введите выражение (например, x**2 + 3x + 1): ')
    limits = input('Введите пределы(например, вместе через запятую 2,1 ), если вы хотите решить определённый интеграл, то можете не пропускать этот шаг: ')
    result = calculate_integral(expression, variable, limits if limits else None)
    print(result)
else:
    print('Ошибка, попробуйте ввести команду повторно!')
    

        

