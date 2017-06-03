use mydb;

alter table people drop index DOB_index;

create index  first_name_index on people (first_name);