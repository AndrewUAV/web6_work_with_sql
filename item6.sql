--6.Знайти список студентів у певній групі.
SELECT students.id AS id, students.name AS students_name, groups.name AS groupe
FROM students
JOIN groups ON students.group_id = groups.id
WHERE group_id = 2