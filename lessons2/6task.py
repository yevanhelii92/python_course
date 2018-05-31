print('Вас приветствует калькулятор')
a1 = int (input('Число 1: '))
a2 = str (input('Введите действие:'))
a3 = int (input('Число 2: '))
if a2 == '+':
    print (a1 + a2)
elif a2 == '-':
    print (a1 - a2)
elif a2 == '*':
    print (a1 * a2)
elif a2 == '/':
    print (a1 / a2)
elif a2 == '**':
    print (a1 ** a2)    