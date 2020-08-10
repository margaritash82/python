# задание 1. Реализовать класс "Дата", функция-конструктор которого должна принимать дату в виде строки формата
# день-месяц-год. В рамка класса реализовать два метода. Первый с декоратором класса @classmethod, должен извлекать
# чило, месяц, год и преобразовывать их тип к типу Число. Второй с декоратором @staticmethod должен проводить валидацию
# числа, месяца и года (например, месяц от 1 до 12). Проверить работу структуры на реальных данных.

class Data:
    def __init__(self):
         self.data = '2-5-2020'

    @classmethod
    def chislo(cls, data):
        data = data.split('-')
        for el in data:
            el = int(el)
            print(el, type(el))

    @staticmethod
    def valid(data):
        data = data.split('-')
        datanew = []
        for el in data:
            el = int(el)
            datanew.append(el)
        if datanew[0] < 1 or datanew[0] > 30:
            print(f'некорректно введено число: {datanew[0]}, измените данные')
        if datanew[1] < 1 or datanew[1] > 12:
            print(f'некорректно введен месяц: {datanew[1]}, измените данные')
        if datanew[2] > 2020:
            print(f'некорректно введен год: {datanew[2]}, измените данные')

Data.chislo('10-8-2020')
my_data = Data()
my_data.chislo('1-5-2020')
Data.valid('55-55-5000')


# Задание 2. Создайте собственный класс-исключение, обраюатывающий ситуацию деления на 0. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должны корректно отработать эту
# ситуацию и не завершиться с ошибкой.

class ZeroError (Exception):
    def __init__(self, znam):
        self.znam = znam

ch = int(input('введите число для деления: '))
znam = int(input('введите делитель: '))
try:
    if znam == 0:
        raise ZeroError ('деление на ноль невозможно')
except ZeroError as err:
    print(err)
else:
    print(f'итог деления: {ch / znam}')


# Задание 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наичие только чисел.
# ПРоверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка. Примечание: Длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановитработу скрипта, введя, например, командду stop.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка.

class ErrType(Exception):
    def __init__(self, chisl):
        self.chisl = chisl

i=0
string = []
while True:
    i = +1
    chisl = input('введите целое положительное число для добавления в список или stop для выхода: ')
    if chisl == 'stop':
        print(string)
        break
    else:
        try:
            ch = chisl.isdigit()
            if ch == False:
                raise ErrType ('Вы ввели не целое положительное число')
        except ErrType as err:
            print(err)
        else:
            chisl = int(chisl)
            string.append(chisl)

# Задание 4. Начните работу над проктом Склад оргтехники. Создайте класс, описывающий склад. А так же класс Оргтехника,
# который будет базовым для классов - наследников. Эти классы - конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры,общие для приведенных типов. В классах - наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Skl():
    def __init__(self, volume, clsteh):
        self.tech = {'clsteh' : clsteh, 'volume': volume}

    def inorg(self):
        pass

    def outorg(self):
        pass


class Orgteh(Skl):
    def __init__(self, clsteh, volume, place):
        super().__init__(clsteh, volume)
        self.place = place

class Print(Orgteh):
    def __init__(self, clsteh, place, type, volume):
        super().__init__(clsteh, place, volume)
        self.type = type


class Skan(Orgteh):
    def __init__(self, clsteh, place, volume, model):
        super().__init__(clsteh, place, volume)
        self.model = model

class Telefone(Orgteh):
    def __init__(self, clsteh, place, volume, type):
        super().__init__(clsteh, place, volume)
        self.typy = type

# Задание 5. Продолжнить работу над первым заданием. Разработать методы, отвечающие за прием оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например, словарь.

# Не успеваю по времени завершить задание

# Задание 6. ПРодолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка. Пострайтесь по максимуму использовать возможности ООП в проекте Склад оргтехники.

# Не успеваю по времени завершить задание

# Задание 7. Реализовать проект Операции с комплексными числами. Создайте класс Комплексное число, реализуйте перегрузку
# методов сложеня и умножения комплексных числел. ПРоверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. ПРоверьте корректность полученного результата.

class Complesch():
    def __init__(self, ch1, ch2):
        self.ch = complex(ch1, ch2)

    def out(self):
        print(f'комплексное число = {self.ch}')

    def __add__(self, ch3, ch4):
        return self.ch + complex(ch3, ch4)

    def __mul__(self, ch3, ch4):
        return self.ch * complex(ch3, ch4)

my_complex = Complesch(2, 3)
my_complex.out()

print(f'итог суммирования комплексных чисел = {my_complex.__add__(5, 8)}')
print(f'итог перемножения комплексных чисел = {my_complex.__mul__(9, 15)}')


