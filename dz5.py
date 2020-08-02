# Задание 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Окончание ввода - пустаяя строка.
f_ch1 = open('ch1.txt', 'a')
while True:
    line = input('введите строку данных для записи в файл или Enter для окончания ввода: ')
    if line != '':
        f_ch1.writelines(line + '\n')
    else:
        break
f_ch1.close()


#Задание 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, кол-ва слов в каждой строке.
with open ('ch2.txt') as f_ch2:
    lines = 0
    words = 0
    for line in f_ch2 :
        lines += 1
        position = 'true'
        for letter in line:
            if letter != ' ' and position == 'true':
                words += 1
                position = 'false'
            elif  letter == ' ':
                position = 'true'

    print(f'количество строк: {lines}, количество слов: {words}')


#Задание 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и их оклад.
#Определить, кто из сотрудников имеет оклад менее 20 тыс.руб., вывести их фамили
#Посчитать среднюю величину дохода сотрудников.
data_file = []
Sernames = []
with open('ch3.txt') as f_ch3:
    lines = (f_ch3.readlines())
    for line in lines:
        line = line.split()
        data_file.append(line)
staff = dict(data_file)
for key, value in staff.items():
    staff[key] = int(value)
for key, value in staff.items():
    if value < 20000 :
        Sernames.append(key)
print(f'Сотрудники с окладом менее 20000 руб: {Sernames}')
print(f'Средний доход всех сотрудников: {sum(staff.values())/len(staff.keys())}')

# Задание 4. Создать (не программно) текстовый файл со следующим содержимым: ...
#Написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f_ch4 = open('ch4.txt')
lines = f_ch4.readlines()
data = []
for line in lines:
    line = line.strip()
    line = line.split(' - ')
    data.append(line)
chisl = dict(data)
val = list(chisl.values())
keys = ['Один', 'Два', 'Три', "Четыре"]
new_chisl = {key: value for key, value in zip(keys, val)}
f_ch4.close()
f_ch4_1 = open('ch4_1.txt', 'a')
for keys, val in new_chisl.items():
    f_ch4_1.writelines(keys + ' - ' + val + '\n')
f_ch4_1.close()

# Задание 5. Создать программно текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
f_ch5 = open('ch5.txt', 'a')
line = '1 2 3 4'
f_ch5.writelines(line)
f_ch5.close()
line = line.split()
line2 = []
for el in line:
    el2 = int(el)
    line2.append(el2)
print(f'сумма всех чисел в файле: {sum(line2)}')

# Задание 6. Создать непрограммно текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
#практических и лабораторных занятий по этому предмету и их кол-во. Для каждого премета не обязательно все виды занятий.
#Сформировать словарь, содержащий название предмета и общее кол-во занятий по нему. Вывести словарь на экран.

d_lesson = {}
sum_hours = []
lesson = []
with open('ch6.txt') as f_ch6:
    lines = f_ch6.readlines()
    for line in lines:
        line = line.split(':')
        lesson = line[0]
        for el in line[1:]:
            el = el.split()
            hours = []
            for var in el:
                var = var[:var.find('(')]
                var = int(var)
                hours.append(var)
        sum_hours1 = sum(var for var in hours)
        d_lesson[lesson] = sum_hours1
print(d_lesson)

# Задание 7. Создать не программно текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Необходимо: построчно прочитать файл, вычислить прибыль каждой компании.
# расчитать среднюю прибыль, если фирма с убытком, его в расечт средней прибыли не включать.
# Реализовать список содержащий: словарь с фирмами и их прибылями и словарь со средней прибылью. Если фирма получила убытки,
# добавить ее в словарь (со значением убытков). Итоговый список сохранить в виде json-объекта в соотв.файл.

d_firm = {}
sr_prof = []
with open('Ch7.txt') as f_ch7:
    lines = f_ch7.readlines()
    for line in lines:
        name, form, incom, costs = line.split()
        prof = int(incom) - int(costs)
        d_firm[name] = prof
        if prof > 0:
            sr_prof.append(prof)
out_prof = sum(sr_prof) / len(sr_prof)
resoult = [d_firm, {'средняя прибыль': out_prof}]

import json
with open('ch7_1.json', 'w') as f_ch71:
    json.dump(resoult, f_ch71)

with open('ch7_1.json') as f_ch71:
    line = json.load(f_ch71)
    print(line)







