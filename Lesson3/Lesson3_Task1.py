# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def func_division(a,b):
    if a!=0 and b!=0:
        return round(a/b,2)
    else:
        return ('Число не должно быть равным нулю')
print(func_division(5,3))
print(func_division(-5,3))
print(func_division(5,0))