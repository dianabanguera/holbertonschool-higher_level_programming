-- script that creates a table called first_table in the current database in your MySQL server.
-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, your script should not fail
-- SELECT or SHOW statements are not allowed.

CREATE table If not exists first_table (id INT, name VARCHAR(256));