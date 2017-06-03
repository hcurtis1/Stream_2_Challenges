use mydb;

drop table if exists people;

create table people (
	id integer auto_increment,
    first_name varchar(50) not null,
    surname varchar(50) not null,
    DOB date not null,
    primary key (id)
);