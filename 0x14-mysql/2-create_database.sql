-- Creates a user with a replication client privilege
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'password';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
