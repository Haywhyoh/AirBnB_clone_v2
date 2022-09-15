-- create database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a new user if not exists
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privilege
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant SELECT privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;