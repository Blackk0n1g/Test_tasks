import os
try:
    filepath = "/home/alexandervmu/tasks_from_Pasha/names.txt"
    with open(filepath, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("File not found")
text_1 = text.split("BREAK") #разделяю текст файла на элементы по "БРЕЙК"
slovar = dict() #Создаем словарь
for elem in text_1: #циклом заменяю в каждом элементе пробелы на 'ничего'
    text_2 = elem.replace(" ", "")
    text_3 = text_2.split("\n") #в том же цикле разделяю элементы на отдельные значения по знаку переноса строки
    text_3 = [val for val in text_3 if val] #убираю 'пустые' элементы для обращения к "нормальным" элементам по индексу
    if text_3[1].endswith('0'):
        continue #если элемент к которому идет обращение оканчивается на "0" - пропускаем это дйствие и продолжаем цикл
    slovar[text_3[0]] = [text_3[1], text_3[2]] #наполняю словарь информацией [ключ] = [значение, значение]
print(slovar)
if len(slovar) > 10: #условие, обрабатывающее "длину словаря" т.е. количество элементов в словаре
    print("Нам хватает {} сотрудников".format(len(slovar)))
else:
    print("Нам не хватает {} сотрудников".format(len(slovar)))
