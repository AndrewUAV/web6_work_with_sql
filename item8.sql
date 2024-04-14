--8.Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT teachers.name AS teacher, ROUND(AVG(grades.grade)) AS average_grade
FROM grades
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE teachers.id = 1