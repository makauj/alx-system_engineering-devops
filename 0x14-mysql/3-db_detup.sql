-- Create a populated database tyrell_corp
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    department VARCHAR(100),
    salary INT
);

INSERT INTO nexus6 (first_name, last_name, department, salary) VALUES
('Rick', 'Deckard', 'Blade Runner', 100000),
('Roy', 'Batty', 'Blade Runner', 120000),
('Pris', 'Stratton', 'Blade Runner', 90000),
('Rachael', 'Tyrell', 'Management', 150000),
('Eldon', 'Tyrell', 'Management', 200000),
('J.F.', 'Sebastian', 'Engineering', 80000),
('Hannibal', 'Chew', 'Engineering', 75000),
('Dave', 'Holden', 'Blade Runner', 110000),
('Gaff', 'Gaff', 'Blade Runner', 95000),
('Harry', 'Bryant', 'Management', 130000),
('Leon', 'Kowalski', 'Engineering', 85000),
('Zhora', 'Salome', 'Engineering', 90000),
('Pris', 'Stratton', 'Engineering', 95000),
('Rachael', 'Tyrell', 'Engineering', 100000),
('Rick', 'Deckard', 'Engineering', 105000),
('Roy', 'Batty', 'Engineering', 110000),
('Dave', 'Holden', 'Engineering', 115000),
('Gaff', 'Gaff', 'Engineering', 120000),
('Harry', 'Bryant', 'Engineering', 125000),
('Leon', 'Kowalski', 'Engineering', 130000),
('Zhora', 'Salome', 'Engineering', 135000),
('Pris', 'Stratton', 'Engineering', 140000),
('Rachael', 'Tyrell', 'Engineering', 145000),
('Rick', 'Deckard', 'Engineering', 150000),
('Roy', 'Batty', 'Engineering', 155000),
('Dave', 'Holden', 'Engineering', 160000),
('Gaff', 'Gaff', 'Engineering', 165000),
('Harry', 'Bryant', 'Engineering', 170000),
('Leon', 'Kowalski', 'Engineering', 175000),
('Zhora', 'Salome', 'Engineering', 180000),
('Pris', 'Stratton', 'Engineering', 185000),
('Rachael', 'Tyrell', 'Engineering', 180000),

USE mysql;
GRANT SELECT ON tyrell_corp.employees TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
