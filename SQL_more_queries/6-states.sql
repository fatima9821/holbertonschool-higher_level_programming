-- script that creates the databasehbn and the table states
CREATE DATABASES IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- in tha database hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO8INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
