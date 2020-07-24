# Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:(выработка в часах*ставка в час)+премия.
# Для выполнения расчета для конкретных значений запускать скрипт с параметрами.

from sys import argv
script_name, virabotka, stavka, prem = argv

print('имя скрипта', script_name)
print('выработка в часах за месяц', virabotka)
print('ставка в час', stavka)
print('премия за месяц', prem)
virabotka=int(virabotka)
stavka=int(stavka)
prem=int(prem)

def zp_func(virabotka, stavka, prem):
    return (virabotka*stavka)+prem

print(zp_func(virabotka, stavka, prem))

# Задание 2. Представлен список чисел.Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Для формирования списка использовать генератор.
test_list=(input('введите список чисел через пробел: '))
test_list=test_list.split()
test_list_new=[float(test_list[i]) for i in range(len(test_list))]
resault_list=[test_list_new[i] for i in range(1, len(test_list_new)) if (test_list_new[i]>test_list_new[i-1])]
print(f'список значений больше предыдущего элемента: {resault_list}')

# Задание 3.Для чисел в пределах от 20 до 240 найти числа, кратные 20 и 21. Необходимо решить задание в одну строку.
# Исползовать range() и генератор

list20=[el for el in range(20,241) if (el/20==int(el/20) or el%21==0)]
print(f'числа кратные 20 или 21:{list20}')

# # Задание 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

test_list=input('введите список чисел через пробел: ')
test_list=test_list.split()
test_list_new=[float(test_list[i]) for i in range(len(test_list))]
resault_list=[]
for i in range(len(test_list_new)):
    if test_list_new[i] not in resault_list:
        resault_list.append(test_list_new[i])
print(f'список значений, не имеющих повторений: {resault_list}')

# Задание 5. Реализовать формирование списка, используя функцию range() и возможности генератора
# В список должны войти четные числа от 100 до 1000 (включая границы). Получить результат вычисления произведения всех элементов списка.
# Подстазка испоьзовать функцию reduce()

list_chet=[el for el in range(100,1001) if (el%2==0)]
print(f'четные числа от 100 до 1000: {list_chet}')
from functools import reduce
def func_pr (prev_el, el):
    return prev_el*el
print(f'произведение четных чисел от 100 до 1000: {reduce(func_pr, list_chet)}')


# Задание 6. Реализовать два небольших скрипта:
# 1) итератор, генерирующий целые числа, начиная с указанного
# 2) итератор, повторяющий элементы списка, определенного заранее, так же предусмотреть условия выхода.
# (исп count и cycle и предусмотреть условия завершения циклов)

from itertools import count
for el in count(11):
    if el > 17:
        break
    else:
        print(el)


from  itertools import cycle
elements=['red', 'white', 'grei', 5, 18, 'night']
el=cycle(elements)
i=0
for i in range(15):
    print(next(el))


# Задание 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение:
# При вызове функции должен создаваться объект-генератор.
# Функция должна выводиться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!

n=int(input('введите максимальное целое число, факториал которого будет получен: '))
from math import factorial
def fact(n):
    for el in range(1, n+1):
        yield factorial(el)

for el in fact(n):
    print(el)




