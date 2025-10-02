CREATE TABLE Employees
(
    Id INT PRIMARY KEY,
    Name VARCHAR(255),
    Position VARCHAR(255),
    Department VARCHAR(255) DEFAULT NULL,
    Salary DECIMAL(10, 2)
);

INSERT INTO Employees (Id, Name, Position, Department, Salary)
VALUES
    (1, 'Maxim', 'Manager', 'Marketing', 100000.00),
    (2, 'Ivan', 'Manager', 'Sales', 85000.00),
    (3, 'Olga', 'HR Specialist', 'HR', 65000.00),
    (4, 'Anna', 'Designer', 'Marketing', 75000.00),
    (5, 'Sergey', 'Developer', 'IT', 120000.00);

-- Вывод всех сотрудников
SELECT * FROM Employees;

-- ✅ TODO 3: Измените должность одного из сотрудников на более высокую
UPDATE Employees
SET Position = 'Senior Manager'
WHERE id = 2;

-- ✅ TODO 4: Добавьте новое поле "HireDate" (DATE) в таблицу "Employees"

ALTER TABLE Employees
ADD COLUMN HireDate DATE DEFAULT NULL;

-- ✅ TODO 5: Добавьте дату приема на работу для всех сотрудников
UPDATE Employees
SET HireDate = CASE
    WHEN Name = 'Maxim' THEN '2020-05-15'
    WHEN Name = 'Ivan' THEN '2021-03-10'
    WHEN Name = 'Olga' THEN '2022-11-22'
    WHEN Name = 'Anna' THEN '2023-02-18'
    WHEN Name = 'Sergey' THEN '2021-08-30'
END
WHERE HireDate IS NULL;


-- ✅ TODO 6: Найдите всех сотрудников с должностью "Manager"
SELECT * FROM Employees
WHERE Position = 'Manager';

-- ✅ TODO 7: Найдите всех сотрудников с зарплатой больше 5000
SELECT * FROM Employees
WHERE Salary >= 5000.00;

-- ✅ TODO 8: Найдите всех сотрудников, которые работают в отделе "Sales"
SELECT * FROM Employees
WHERE LOWER(Department) = 'sales';

-- ✅ TODO 9: Найдите среднюю зарплату всех сотрудников
SELECT
    AVG(Salary) AS AvgSalary,
    MIN(Salary) AS MinSalary,
    MAX(Salary) AS MaxSalary
FROM Employees;


-- ✅ TODO 10: Удалите таблицу "Employees"
DROP TABLE Employees

-- 🎯 *Задание с повышенным уровнем сложности:*
-- Реализуйте задачи 6–9 в виде ХРАНИМЫХ ФУНКЦИЙ или ПРОЦЕДУР.

-- Подсказка:
-- CREATE FUNCTION или CREATE PROCEDURE
-- BEGIN ... END

-- Пример вызова:
-- CALL имя_процедуры();

-- 📝 Напишите здесь свои CREATE FUNCTION / PROCEDURE

-- ✅ TODO 6: Найдите всех сотрудников с должностью "Manager"
CREATE PROCEDURE GetManagers()
BEGIN
    SELECT * FROM Employees
    WHERE Position LIKE '%Manager%';
END

CALL GetManagers();

-- ✅ TODO 7: Найдите всех сотрудников с зарплатой больше 5000
CREATE PROCEDURE GetHighSalary()
BEGIN
    SELECT * FROM Employees
    WHERE Salary >= 50000.00;
END

CALL GetHighSalary();

-- ✅ TODO 8: Найдите всех сотрудников, которые работают в отделе "Sales"
CREATE PROCEDURE GetSales()
BEGIN
    SELECT * FROM Employees
    WHERE LOWER(Department) = 'sales';
END

CALL GetSales();


-- ✅ TODO 9: Найдите среднюю зарплату всех сотрудников
CREATE PROCEDURE GetSalaryStats()
BEGIN
    SELECT
    AVG(Salary) AS AvgSalary,
    MIN(Salary) AS MinSalary,
    MAX(Salary) AS MaxSalary
FROM Employees;
END

CALL GetSalaryStats();


✅ Удалить процедуры в конце (чтобы не «засорять» БД):

DROP PROCEDURE IF EXISTS GetManagers;
DROP PROCEDURE IF EXISTS GetHighSalary;
DROP PROCEDURE IF EXISTS GetSales;
DROP PROCEDURE IF EXISTS GetSalaryStats;
