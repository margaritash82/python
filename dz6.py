# Задание 1. Создать класс TrafficLight и определить у него один атрибут color и метод running. Атрибут реализовать как
# приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность красного - 7 секунд, желтого - 2 секунды, зеленого - какая хотите. Переключение только в указанном порядке.
# Проверить работу примера, создав экземпляр и вызвав указанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, при нарушении выводить сообщение и завершить скрипт.

from time import sleep

class TeafficLight:
    def __init__(self):
        self.color = {'red': 7, 'yellow': 2, 'green': 5}
    def running(self):
        out = int(input('укажите количество циклов работы светофора: '))
        for out in range (0,out):
            for key, value in self.color.items():
                    print(key)
                    sleep(value)

my_teafflight = TeafficLight ()
my_teafflight.running()

#Задание 2. Реализовать класс Road, в котором определить атрибуты: lenght, width. Значения данных атрибутов должны передаваться
#при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для
# покрытия всего полотна длина*ширина*масса на 1 кв.см*толщина. Проверить работу метода.

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def weight (self):
        return self._lenght * self._width * 25 * 5/ 1000
my_Road = Road(int(input('введите длину дороги в метрах: ')), int(input('введите ширину дороги в метрах: ')))
# my_Road._lenght = int(input('введите длину дороги в метрах: '))
# my_Road._width = int(input('введите ширину дороги в метрах: '))
print(f' масса асфальта в тоннах: {my_Road.weight()}')

# Задание 3. Реализовать базовый класс Worker, в котором определить атрибуты: name, surname, position, income.
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элеметы: оклад и премия, например,
# {'wage': wage, 'bonus': bonus}. Создать класс Position на базе класса Worker. В коассе Position реализовать методы
# получения полного имени сотрудника (get full name) и дохода с учетом премии (get total income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, sername, position, income):
        self.name = name
        self.sername = sername
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position (Worker):
    def get_full_name (self):
        print(self.name + ' ' + self.sername)

    def get_total_income (self):
        print(self._income_wage + self._income_bonus)

my_Position = Position('Шарова', 'Маргарита', 'менеджер', {'wage': 5000, 'bonus': 7000})
my_Position.get_full_name()
my_Position.get_total_income()


# Задание 4. Реализуйте базовый класс Car.У класса д.б. атрибуты: speed, color, name, is_police (булево). А так же
# методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed
# который должен показывать текущую скорость автомобиляю Для классов TownCar и WorkCar переопределите метод show_speedю
# При значении скорости свыше 60 (TownCar) и 40 (WorKCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и так же покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f'{self.name} едет')

    def stop(self):
        if self.speed == 0:
            print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} = {self.speed}')

class TownCar (Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает допустимую скорость')

class SportCar (Car):
    def volume (self, volume):
        print(f'{self.color} спортивная машина c объемом двигателя {volume}')

class WorkCar (Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает допустимую скорость')

class PoliceCar (Car):
    pass

test_car = Car(0, 'красная', 'KIA', False)
test_car.stop()
test_car.show_speed()

my_car = TownCar(80, 'красная', 'KIA', False)
my_car.go()
my_car.turn('налево')
my_car.show_speed()
my_car.stop()

s_car = SportCar(80, 'красная', 'KIA', False)
s_car.volume(210)


# Задание 5. Реализовать класс Stationery (канцелярская принадлежность).Определить в нем атрибут title (название)и метод
# draw (отрисовка). Метод выводит сообщение "Запуск отрисовки". Создать три дочерних класса Pen, Pencil, Handle.
# В каждом из классов реализовать переопределение метода draw. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw (self):
        print ('запуск отрисовки')

class Pen (Stationery):
    def draw(self):
        print ('отрисовка ручкой')

class Pencil (Stationery):
    def draw(self):
        print('отрисовка карандашом')

class Handle (Stationery):
    def draw(self):
        print('отрисовка маркером')

my_stat = Stationery ('Инструмент')
my_stat.draw()

my_pen = Pen ('Ручка')
my_pen.draw()

my_pencil = Pencil ('Карандаш')
my_pencil.draw()

my_handle = Handle ('Маркер')
my_handle.draw()





