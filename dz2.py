# задача 1. Создать список с разными типами данных, реализовать скрипт провоерки типа данных каждого элемента. Использовать функцию type

top_list = ['цветы', 5.3, 7, 325, None, True]
for el in top_list :
    print(type(el))

# задача 2. Для списка реализовать обмен значений соседних элементов. Список заполнить с использованием функции input
new_list = input('введите значения списка через пробел:')
new_list = new_list.split()
i=0
for i in range (1, len(new_list), 2):
    new_list[i-1], new_list[i] = new_list[i], new_list[i-1]
print(new_list)

# задача 3. Польователь вводит месяц в виде целого числа от 1 до 12. Сообщить, какому времени года это соответствует, использовать dict и list

mounth = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето', 7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}
keyd = int(input('введите номер месяца: '))
print(mounth.get(keyd))

# задача 4. Запросить 10 слов. Выводить слова в 10 нумерованных строк, выводить первые 10 символов в слове

ten_word = input("введите 10 слов через пробел: ")
ten_list = ten_word.split()
for ind,el in enumerate ((ten_list),1):
    print(ind, el[:10])

# задача 5. Реализовать структуру рейтинги, предсавляющую собой набор не возрастающий набор натуральных чисел. Каждон новое от пользователя встает последним за аналогичными

my_rating = [10, 4, 3]
new_rate = int(input('введите рейтинг: '))
n = len(my_rating)
my_rating.insert(0, new_rate)
n = len(my_rating)
for i in range (1, n, 1):
    if my_rating[i] > my_rating[i-1]:
        my_rating[i-1], my_rating[i] = my_rating[i], my_rating[i-1]
    else:
        print(my_rating)














