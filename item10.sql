--10.Список курсів, які певному студенту читає певний викладач.
SELECT students.name AS student_name, subjects.name AS subject, teachers.name AS teacher
FROM subjects
JOIN students
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN grades ON students.id = student_id AND subjects.id = subject_id
WHERE students.id = 49 AND teachers.id = 2