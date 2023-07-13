-- A script to create a table users
CREATE table if not exists users (
id integer primary key auto_increment,
email varchar(255) not null unique,
name varchar(255)
);
