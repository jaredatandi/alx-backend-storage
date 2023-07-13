-- Use enums
CREATE table if not exists users (
id integer primary key auto_increment,
email varchar(255) not null unuique,
name varchar(255),
country enum('US', 'CO', 'TN') not null default 'US'
);
