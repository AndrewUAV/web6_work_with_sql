--7.Знайти оцінки студентів у окремій групі з певного предмета.
SELECT students.name AS student_name, groups.name, subjects.name AS subject, grades.grade
FROM students
JOIN groups ON students.group_id = groups.id
JOIN subjects ON grades.subject_id = subjects.id
JOIN grades ON students.id = grades.student_id
WHERE groups.id = 3
AND subjects.id = 2