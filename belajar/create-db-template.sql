CREATE DATABASE IF NOT EXISTS test_db;

USE test_db;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL    
);

INSERT INTO users (username, password) VALUES ("admin", "1234");


CREATE TABLE pasien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    umur INT NOT NULL,
    penyakit VARCHAR(50) NOT NULL,
    dokter VARCHAR(50) NOT NULL
);
