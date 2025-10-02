-- 📘 TeachMeSkills: Домашнее задание по SQL
-- Тема: Создание таблиц, связи и JOIN
--

-- 📋 Задача 1: Создание и заполнение таблиц

-- TODO: Создайте таблицу authors с полями id, first_name, last_name
--       (используйте PRIMARY KEY для поля id)
CREATE TABLE Authors(
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

-- TODO: Создайте таблицу books с полями id, title, author_id, publication_year
--       (PRIMARY KEY — id, FOREIGN KEY — author_id, ссылается на authors)
CREATE TABLE Books(
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    publication_year INT,
    FOREIGN KEY (author_id) REFERENCES Authors(id) ON DELETE CASCADE
);

-- TODO: Создайте таблицу sales с полями id, book_id, quantity
--       (PRIMARY KEY — id, FOREIGN KEY — book_id, ссылается на books)
CREATE TABLE Sales(
    id INT PRIMARY KEY,
    book_id INT,
    quantity INT DEFAULT 0 NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Books(id) ON DELETE CASCADE
);

-- Вставить данные:

-- TODO: Добавьте нескольких авторов в таблицу authors
--       (INSERT INTO authors ...)
INSERT INTO Authors (id, first_name, last_name)
VALUES
    (1, 'Лев', 'Толстой'),
    (2, 'Федор', 'Достоевский'),
    (3, 'Антон', 'Чехов'),
    (4, 'Николай', 'Гоголь'),
	(5, 'Максим', 'Свирилин');

-- TODO: Добавьте несколько книг в таблицу books, указывая авторов из authors
INSERT INTO Books (id, title, author_id, publication_year)
VALUES
    (1, 'Война и мир', 1, 1869),
    (2, 'Преступление и наказание', 2, 1866),
    (3, 'Вишнёвый сад', 3, 1904),
    (4, 'Мёртвые души', 4, 1842),
	(5, '[нет книги]', 5, 2025);    -- Для демонстрации автора без нормальной книги


-- TODO: Добавьте записи о продажах книг в таблицу sales
INSERT INTO Sales (id, book_id, quantity)
VALUES
	(1, 1, 0),
	(2, 2, 25),
	(3, 3, 16),
	(4, 4, 20);

-- 📋 Задача 2: Использование JOIN

-- TODO: Используйте INNER JOIN для получения списка всех книг и их авторов.
SELECT Authors.first_name, Authors.last_name, Books.title
FROM Authors
INNER JOIN Books ON Authors.id = Books.author_id;
-- TODO: Используйте LEFT JOIN для получения списка всех авторов и их книг 
--		(включая авторов, у которых нет книг).
SELECT Authors.first_name, Authors.last_name, Books.title
FROM Authors
LEFT JOIN Books ON Authors.id = Books.author_id;

-- TODO: Используйте RIGHT JOIN, чтобы получить список всех книг и их авторов
--       (включая книги без автора)
SELECT Authors.first_name, Authors.last_name, Books.title
FROM Authors
RIGHT JOIN Books ON Authors.id = Books.author_id;

-- 📋 Задача 3: Множественные JOIN

-- TODO: Используйте INNER JOIN, чтобы связать authors, books и sales и получить
--       список всех книг, их авторов и продаж
SELECT Authors.first_name, Authors.last_name, Books.title, Sales.quantity
FROM Books
INNER JOIN Authors ON Books.author_id = Authors.id
INNER JOIN Sales ON Books.id = Sales.book_id;

-- TODO: Используйте LEFT JOIN, чтобы связать authors, books и sales и получить
--       список всех авторов, их книг и продаж (включая авторов без книг и книги без продаж)
SELECT Authors.first_name, Authors.last_name, Books.title, Sales.quantity
FROM Authors
LEFT JOIN Books ON Authors.id = Books.author_id
LEFT JOIN Sales ON Books.id = Sales.book_id;

-- Пример агрегатной функции:
-- SELECT author_id, SUM(quantity) FROM sales
-- JOIN books ON sales.book_id = books.id
-- GROUP BY author_id;
--
-- 💡 Вопросы для самоконтроля:
-- 1. Чем отличается INNER JOIN от LEFT JOIN?
-- 2. Почему внешний ключ важен для целостности данных?
-- 3. Для чего нужен GROUP BY?

-- 📋 Задача 4: Агрегация данных с использованием JOIN

-- TODO: Используйте INNER JOIN и агрегатные функции, чтобы определить общее
--       количество проданных книг каждого автора
SELECT 
    Authors.first_name, 
    Authors.last_name, 
    Books.title, 
    COALESCE(SUM(Sales.quantity), 0) AS total_sales
FROM Authors
INNER JOIN Books ON Authors.id = Books.author_id
INNER JOIN Sales ON Books.id = Sales.book_id
GROUP BY 
    Authors.id, 
    Authors.first_name, 
    Authors.last_name,
    Books.title
ORDER BY 
    total_sales DESC;

-- TODO: Используйте LEFT JOIN и агрегатные функции, чтобы определить общее
--       количество проданных книг каждого автора, включая авторов без продаж
SELECT 
    Authors.first_name, 
    Authors.last_name, 
    Books.title, 
    COALESCE(SUM(Sales.quantity), 0) AS total_sales
FROM Authors
LEFT JOIN Books ON Authors.id = Books.author_id
LEFT JOIN Sales ON Books.id = Sales.book_id
GROUP BY 
    Authors.id, 
    Authors.first_name, 
    Authors.last_name,
    Books.title
ORDER BY 
    total_sales DESC;

-- 📋	Задача 5: Подзапросы и JOIN
-- TODO: Найдите автора с наибольшим количеством проданных книг, используя подзапросы и JOIN
SELECT 
    Authors.first_name, 
    Authors.last_name,
    author_sales.total_sales
FROM (
    SELECT 
        Authors.id,
        Authors.first_name,
        Authors.last_name,
        SUM(COALESCE(Sales.quantity, 0)) AS total_sales
    FROM Authors
    LEFT JOIN Books ON Authors.id = Books.author_id
    LEFT JOIN Sales ON Books.id = Sales.book_id
    GROUP BY 
        Authors.id, 
        Authors.first_name, 
        Authors.last_name
) AS author_sales
ORDER BY 
    author_sales.total_sales DESC
FETCH FIRST 1 ROWS WITH TIES;

-- TODO: Найдите книги, которые были проданы в количестве, превышающем среднее количество продаж всех книг,
-- 		используя подзапросы и JOIN
SELECT 
    Books.title,
    Sales.quantity
FROM Books
INNER JOIN Sales ON Books.id = Sales.book_id
WHERE Sales.quantity > (
	SELECT AVG(quantity)
	FROM Sales
	WHERE quantity IS NOT NULL
)
ORDER BY 
    Sales.quantity DESC;


-- 🚀 Удачи! Не бойтесь пробовать разные JOIN и GROUP BY, чтобы лучше понять, как они работают!