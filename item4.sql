-- 4.Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT ROUND(AVG(grades.grade)) AS average_grade
FROM grades