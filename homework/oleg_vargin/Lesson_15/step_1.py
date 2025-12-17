import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Создаем студента
cursor.execute(
    'INSERT INTO students (name, second_name) VALUES (%s, %s)',
    ("Oleg", "Vargin")
)
student_id = cursor.lastrowid
print(f'Студент добавлен с ID: {student_id}')
print()

# Добавляем книги
cursor.execute(
    'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)',
    ('Sketchbook_1', student_id)
)
cursor.execute(
    'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)',
    ('Sketchbook_2', student_id)
)

# Создаем группу
cursor.execute(
    'INSERT INTO `groups` (title) VALUES (%s)',
    ('Group for Oleg',)
)
group_id = cursor.lastrowid
print(f'Создана группа с ID: {group_id}')
print()

# Назначаем студента в группу
cursor.execute(
    'UPDATE students SET group_id = %s WHERE id = %s',
    (group_id, student_id)
)

# Создаем предметы
cursor.execute(
    'INSERT INTO subjects (title) VALUES (%s)',
    ('Geography',)
)
subject_id_1 = cursor.lastrowid
print(f'Предмет Geography добавлен с ID: {subject_id_1}')

cursor.execute('INSERT INTO subjects (title) VALUES (%s)',
               ('World History',)
               )
subject_id_2 = cursor.lastrowid
print(f'Предмет World History добавлен с ID: {subject_id_2}')
print()

# Создаем уроки
cursor.execute(
    'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)',
    ('Geography lesson 1', subject_id_1)
)
lesson_id_1 = cursor.lastrowid
print(f'Урок Geography lesson 1 добавлен с ID: {lesson_id_1}')

cursor.execute(
    'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)',
    ('Geography lesson 2', subject_id_1)
)
lesson_id_2 = cursor.lastrowid
print(f'Урок Geography lesson 2 добавлен с ID: {lesson_id_2}')

cursor.execute(
    'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)',
    ("World History lesson 1", subject_id_2)
)
lesson_id_3 = cursor.lastrowid
print(f'Урок World History lesson 1 добавлен с ID: {lesson_id_3}')

cursor.execute(
    'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)',
    ("World History lesson 2", subject_id_2)
)
lesson_id_4 = cursor.lastrowid
print(f'Урок World History lesson 2 добавлен с ID: {lesson_id_4}')
print()

# Добавляем оценки
cursor.execute(
    'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)',
    (4, lesson_id_1, student_id)
)
cursor.execute(
    'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)',
    (3, lesson_id_2, student_id)
)
cursor.execute(
    'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)',
    (3, lesson_id_3, student_id)
)
cursor.execute(
    'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)',
    (5, lesson_id_4, student_id)
)

db.commit()

# Вывод данных
print('Вывод оценок студента')
cursor.execute('''
               SELECT value
               FROM marks
               WHERE student_id = %s
               ''',
               (student_id,)
               )
marks = cursor.fetchall()
for mark in marks:
    print(f"Оценка: {mark['value']}")
print()

print('Вывод книг студента')
cursor.execute('''
               SELECT title
               FROM books
               WHERE taken_by_student_id = %s
               ''',
               (student_id,)
               )
books = cursor.fetchall()
for row in books:
    print(f'Книга: {row["title"]}')
print()

print('Полная информация о студенте и всех запиясях в БД')
cursor.execute('''
               SELECT students.id          AS student_id,
                      students.name        AS student_name,
                      students.second_name AS student_second_name,
                      groups.title         AS group_title,
                      books.title          AS book_title,
                      marks.value          AS mark,
                      lessons.title        AS lesson_title,
                      subjects.title       AS subject_title
               FROM students
                        JOIN `groups` ON students.group_id = `groups`.id
                        JOIN books ON students.id = books.taken_by_student_id
                        JOIN marks ON students.id = marks.student_id
                        JOIN lessons ON marks.lesson_id = lessons.id
                        JOIN subjects ON lessons.subject_id = subjects.id
               WHERE students.id = %s
               ''',
               (student_id,)
               )
full_info = cursor.fetchall()
for row in full_info:
    print(row)

db.close()
