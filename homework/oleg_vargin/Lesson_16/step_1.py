import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(base_dir)))
csv_path = os.path.join(
    root_dir, 'homework', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv'
)

missing_row = []

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        name = row['name'].strip()
        second_name = row['second_name'].strip()
        group_title = row['group_title'].strip()
        book_title = row['book_title'].strip()
        subject_title = row['subject_title'].strip()
        lesson_title = row['lesson_title'].strip()
        mark_value = row['mark_value'].strip()
        query = """
                SELECT *
                FROM students AS s
                         JOIN marks AS m ON s.id = m.student_id
                         JOIN `groups` AS g ON s.group_id = g.id
                         JOIN lessons AS l ON m.lesson_id = l.id
                         JOIN subjects AS subj ON l.subject_id = subj.id
                WHERE s.name = %s
                  AND s.second_name = %s
                  AND g.title = %s
                  AND subj.title = %s
                  AND l.title = %s
                  AND m.value = %s
                """
        cursor.execute(query,
                       (name, second_name, group_title, subject_title, lesson_title, mark_value)
                       )
        result = cursor.fetchone()

        query_book = """
                     SELECT b.id
                     FROM books AS b
                              JOIN students AS s ON b.taken_by_student_id = s.id
                     WHERE s.name = %s
                       AND s.second_name = %s
                       AND b.title = %s
                     """
        cursor.execute(query_book,
                       (name, second_name, book_title)
                       )
        book_result = cursor.fetchone()

        if not result or not book_result:
            missing_row.append(row)

if missing_row:
    for row in missing_row:
        print('Отсутствует в базе данных', row)
else:
    print('Все записи из CSV присутствуют в базе.')

cursor.close()
db.close()
