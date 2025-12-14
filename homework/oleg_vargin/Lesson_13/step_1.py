import os
import datetime

base_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(base_dir)))
file_path = os.path.join(
    root_dir, "homework", "eugene_okulik", "hw_13", "data.txt"
)

with open(file_path, 'r', encoding='utf-8') as data_file:
    for line in data_file:
        left_part = line.strip().split(' - ')[0]
        right_part = line.strip().split(' - ')[1]
        number, date_str = left_part.split('. ', 1)
        dt = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        if number == '1':
            print(f'Дата из первой строки: {dt}')
            print(f'Задание к дате первой строки: {right_part}')
            print((dt + datetime.timedelta(days=7)).strftime('%Y-%m-%d' ' %H:%M:%S.%f'))
            print()
        elif number == '2':
            days = ["Понедельник", "Вторник", "Среда",
                    "Четверг", "Пятница", "Суббота", "Воскресенье"]
            print(f'Дата из второй строки: {dt}')
            print(f'Задание к дате второй строки: {right_part}')
            print(f'{days[dt.weekday()]}')
            print()
        elif number == '3':
            print(f'Дата из третьей строки: {dt}')
            print(f'Задание к дате третьей строки: {right_part}')
            now = datetime.datetime.now()
            delta = now - dt
            print(f"{delta.days} дней назад")
