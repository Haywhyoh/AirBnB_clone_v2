-- create database called hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- CREATE A USES IF NOT EXIST
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test_dev'@'localhost';
FLUSH PRIVILEGES;
-- grant select privileges to hbnb_test_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test_dev'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;