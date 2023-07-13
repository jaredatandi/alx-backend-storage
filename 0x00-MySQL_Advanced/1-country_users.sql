--  creates a table users
CREATE table if not exists users (
id INT NOT NULL AUTO_INCREMENT,
email varchar(255) not null unuique,
name varchar(255),
country ENUM('US', 'CO', 'TN') not null default 'US',
PRIMARY KEY (id)
);
