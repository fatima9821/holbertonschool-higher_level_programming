-- script that creates a table in the database
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	scrore INT
);
INERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
