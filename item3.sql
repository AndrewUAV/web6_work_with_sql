--3.Знайти середній бал у групах з певного предмета.
SELECT groups.name AS group_name, subjects.name, ROUND(AVG(grades.grade)) AS average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.id = 5
GROUP BY group_name