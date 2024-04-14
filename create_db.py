import random
import sqlite3
from faker import Faker

FILE_DB = 'university.db'
GROUPS = ['group A', 'group B', 'group C']
SUBJECTS = ["Mathematics", "History", "Literature", "Biology", "Physics", "Geography", "Chemistry", "Languages"]
TEACHERS = ["John Smith", "Mary Johnson", "Peter Ivanov", "Anna Koval", "Michael Petrov"]

fake = Faker()


def create_tables(file_db):
    try:
        with sqlite3.connect(file_db) as conn:
            cursor = conn.cursor()

            # students
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS students(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(255),
                            group_id TINYINT,
                             FOREIGN KEY (group_id) REFERENCES groups(id)
                        )
                    ''')

            # groups
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS groups (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(255)
                        )
                    ''')

            # teachers
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS teachers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(255)
                        )
                    ''')

            # subjects
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS subjects (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(255),
                            teacher_id TINYINT,
                            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                        )
                    ''')

            # progress of students
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS grades (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            student_id TINYINT,
                            student_name VARCHAR(255),
                            subject_id TINYINT,
                            grade TINYINT,
                            date_received DATE,
                            FOREIGN KEY (student_id) REFERENCES students(id),
                            FOREIGN KEY (subject_id) REFERENCES subjects(id)
                        )
                    ''')
            # add all data of db
            add_groups(GROUPS, cursor)
            add_teachers(TEACHERS, cursor)
            add_subjects(SUBJECTS, TEACHERS, cursor)
            students = add_students(cursor)
            add_grades(students, cursor)

    except sqlite3.Error as e:
        print(f'Error: {e}')


def add_groups(groups: list, cursor):
    for group in groups:
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (group,))


def add_teachers(teachers: list, cursor):
    for teacher in teachers:
        cursor.execute('INSERT INTO teachers (name) VALUES (?)', (teacher,))


def add_subjects(subjects: list, teachers: list, cursor):
    for subject in subjects:
        teacher_id = random.randint(1, len(teachers))  # Випадковим чином обираємо ідентифікатор вчителя
        cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, teacher_id))


def add_students(cursor):
    students = list()

    for _ in range(50):
        name = fake.name()
        group_id = random.randint(1,3)
        students.append((name, group_id))
    cursor.executemany('INSERT INTO students (name, group_id) VALUES (?, ?)', students)
    return students


def add_grades(students: list, cursor):
    grades = list()
    for student_id in range(1, 50 + 1):
        for subject_id in range(1, 8):
            student_name = students[student_id - 1][0]
            grade = random.randint(60, 100)
            date_received = fake.date_between(start_date="-1y", end_date="today")
            grades.append((student_id, student_name, subject_id, grade, date_received))
    cursor.executemany(
                'INSERT INTO grades (student_id, student_name, subject_id, grade, date_received) VALUES (?, ?, ?, ?, ?)',
                grades)


if __name__ == "__main__":
    create_tables(FILE_DB)