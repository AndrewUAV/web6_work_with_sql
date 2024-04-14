--2.Знайти студента із найвищим середнім балом з певного предмета.

SELECT students.id, students.name, ROUND(AVG(grades.grade)) AS average_grade, subjects.name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.id = 2
GROUP BY students.id, students.name
ORDER BY average_grade DESC
LIMIT 1;