-- #1

create table people (
	StudentID		integer auto_increment primary key,
    LastName		varchar(30) not null,
    FirstName		varchar(30),
    MiddleInitial	char(1),
    DateOfBirth		date not null
);

insert into people
	(LastName, FirstName, MiddleInitial, DateOfBirth)
Values
	('Reed', 'Mary', 'L', '2000-05-02'),
    ('Stephens', 'Joanne', 'M', '1988-01-17'),
    ('Dawkins', 'Stephen', 'J', '1980-02-25'),
    ('Fitch', 'Louis', 'B', '2005-03-16'),
    ('Smith', 'Jason', 'R', '1974-02-01'),
    ('Downing', 'Leslie', 'Q', '1994-12-15'),
    ('Jones', 'Marie', 'S', '2001-04-04');

select *
from people;

-- #2
update people
	set LastName = 'Riley'
where StudentID = 2;

select *
from people;

-- #3
set sql_safe_updates = 0;
update people
	set FirstName = 'Steven'
where DateOfBirth = '1980-02-25';
set sql_safe_updates = 1;

select *
from people;

-- #4
update people
	set MiddleInitial = 'Z',
		DateOfBirth = '1984-02-01'
where StudentID = 5;

select *
from people;

-- #5
delete from people
where StudentID = 6;

select *
from people;

-- #6
set sql_safe_updates = 0;
delete from people
where DateOfBirth > '2000-01-01';
set sql_sage_updates = 1;

select *
from people;


	

