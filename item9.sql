--9.Знайти список курсів, які відвідує студент.
SELECT students.name AS student_name, subjects.name AS subject
FROM subjects
JOIN students
JOIN grades ON subjects.id = subject_id AND students.id = student_id
WHERE students.id = 17