""""
Решение задачи 1 предпроффессионального экзамена.
Программа читает данные из csv-файла, ищет результат учащегося.
Затем подсчитывает средний баллЭ заменяет им результаты None.
И сохраняет новый файл.
"""
from csv import reader, writer
with open('students.csv', encoding= 'utf-8') as data_file:
    csv_data = reader(data_file, delimiter = ",")
    for row in csv_data:
        if "Хадаров Владимир" in row[1]:
            print(f"Ты получил: {row[4]}, за проект -{row[2]}")