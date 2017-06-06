use mydb;

drop table if exists orders;

drop table if exists profiles;

drop table if exists people;

create table people (
	id integer auto_increment,
    first_name varchar(50) not null,
    surname varchar(50) not null,
    DOB date,
    primary key (id)
);

create table orders (
	id integer auto_increment,
    amount decimal(18, 2),
    person_id integer,
    created_at datetime default current_timestamp,
    primary key (id),
    foreign key (person_id) references people(id),
    check (amount>0)
);

create table profiles (
	id integer auto_increment,
    person_id int,
    address text,
    updated_at datetime default current_timestamp,
    primary key (id),
    foreign key (person_id) references people(id)
);

insert into mydb.people (
	first_name,
    surname,
    DOB
) values 
	('Barry', 'Scott', str_to_date('1/01/2012', '%d/%m/%Y')),
    ('Fred', 'Damas', str_to_date('03/06/1956', '%d/%m/%Y')),
    ('Benedict', 'Philmore', str_to_date('04/09/1974', '%d/%m/%Y')),
    ('Will', 'Cockbag', str_to_date('25/07/1999', '%d/%m/%Y')),
    ('Stacey', 'Bell', str_to_date('31/03/1945', '%d/%m/%Y'));

insert into mydb.profiles (
	person_id,
    address
) values (
	2,
    '142
    big dicklane
    swingingdicksland
    NK4 7UR'
);

insert into mydb.orders (
	person_id,
    amount
) values 
	(1, 142.36),
    (2, 2256.89),
    (3, 42.12),
    (4, 779.99),
    (5, 589.20);
    
update mydb.orders
set amount = amount * 2
where person_id = 3