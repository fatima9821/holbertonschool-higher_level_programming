-- script that create the database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- script that create the table
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT  UNIQUE NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);

