-- script that creates the database and the table 
CREATE DATABASES IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- create the citis table
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
