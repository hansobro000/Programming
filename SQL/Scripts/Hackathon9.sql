-- #1
create schema hackathon9db;

use hackathon9db;

-- #2
create table Persons (
	PersonID int,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    constraint PKPerson primary key (PersonID,LastName)
);

describe Persons;

-- #3
insert into Persons (PersonID, LastName, FirstName, Age)
values
	(1, 'Hanson', 'Ola', 30),
	(2, 'Svendson', 'Tove', 23),
    (3, 'Petterson', 'Kari', 20);
    
select *
from Persons;

-- #4
create table Orders (
	OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    primary key (OrderID),
    foreign key (PersonID) references Persons(PersonID)
);

describe Orders;

-- #5
insert into Orders (OrderID, OrderNumber, PersonID)
values
		(1, 77895, 3),
        (2, 44678, 3),
        (3, 22456, 2),
        (4, 24562, 1);
        
select *
from Orders;

-- #6
select *
from Persons p
left join Orders o
on p.PersonID = o.PersonID;