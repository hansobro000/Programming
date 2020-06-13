select *
from employees;

select
	concat(e.lastname,' ',e.firstname) as 'Employee',
    e.jobTitle,
    concat(m.lastname,' ',m.firstname) as 'Manager',
    m.jobTitle
from employees e
inner join employees m
on m.employeeNumber = e.reportsTo;

create view empNameVIEW as
select
employeeNumber,
concat(lastname,', ',firstname) as 'FullName'
from employees
order by employeeNumber;
-- create a view for someone to see but not actually have data

show tables;
-- see all the tables in database (virtual and real)

select *
from empNameVIEW;
-- see the view
-- only have to give someone this line of code to see the table

drop view if exists empName;
-- get rid of views you have already made

