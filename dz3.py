# Задание 1. Реализовать функцию, принимающую два числа и выполняющую их деление. Числа запрашиваются у пользователя, предусмотрть ситуацию деления на 0.

def f_division():
    try:
        chisl=float(input('введите числитель дроби '))
        znam=float(input('введите знаменатель дроби '))
        resault=chisl/znam
    except ZeroDivisionError:
        print('деление на ноль недопустимо')
        return
    else:
        resault=chisl/znam
        return resault

print(f_division())


 # Задание 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
 # Функция должна принимать параметры как именованные аргумены. Реализовать вывод данных о пользователе одной строкой.

def users(**kwargs):
    print(kwargs)

users(name='Mari', sermame='Davu', dateberth='20.07.1991', city='Marsel', email='mari91@gmail.com', tel='+36548562546')


 # Задание 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(x,y,z):
   if x>z and y>z:
       return x+y
   elif y>x and z>x:
       return y+z
   else:
       return x+z

print(my_func(5, 6, 7))


# Задание 4. Программа принимает действительное положительное чиcло х и целое отрицательное число у. Выполнить возведение х в степень у.
# Задание необходимо реализовать в виде функции my_func(x,y). При решении обойтись без встроенной функции.
# Попробуйте решить 2 способами: через оператор ** и с использованием цикла.

def my_func2(x,y):
    return x ** y
print(my_func2(4,-4))

# задание 4. Способ 2 через цикл (возведение в отрицательную степень = 1/ возведение в положительную степень или умножение на само себя чтолько раз, сколько стоит в степени)
def my_func3(x,y):
    znam=x
    for i in range(1,abs(y)):
        znam=znam*x
        i=+1
    return 1/znam
print(my_func3(4,-4))

 # Задание 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажании Enter должна выводиться сумма чисел.
 # Пользователь может продолжить ввод чисел, разделенных побелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже одсчитанной сумме.
 # Но если вместо числа вводится специальный символ, выполнение программы завершается.
 # Если специальны символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после завершить программу.

resault_list = []
num = 0
i=0
while True:
    num=+1
    args = input('введите числа, разделенные пробелом и нажмие Enter; для выхода из программы нажмите q: ')
    args = args.split()
    if 'q' in args and len(args) < 2:
        break
    elif 'q' in args and len(args) >= 2:
        args.remove('q')
        for i in range(len(args)):
            args[i] = float(args[i])
        resault = sum(args)
        resault_list.append(resault)
        res_summ = sum(resault_list)
        print(res_summ)
        break
    else:
        for i in range(len(args)):
            args[i] = float(args[i])
        resault = sum(args)
        resault_list.append(resault)
        res_summ = sum(resault_list)
        print(res_summ)


 # Задание 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
 # Продолжите работу над заданием. В программу должны попадать строка из слов, разделенных пробелом. Каждое слово состоит из лаинских букв в нижнем регистре.
 # Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_fanc(*args):
    words = str(args).title()
    return words
print(int_fanc('lord of ring'))


