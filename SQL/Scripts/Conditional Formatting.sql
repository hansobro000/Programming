select *
from salaries
where salary > 40000
and salary < 60000
order by
salary desc, 
from_date;
-- desc or asc applies to the column right before it, not all previous

select
emp_no,
to_date,
salary
from salaries
where (year(to_date) = 2000
or year(to_date) = 2001)
and salary < 40000;

select *
from salaries
where emp_no = 10001;
-- only georgie fiscello

select *
from salaries
where not emp_no = 10001;
-- everyone except georgie fiscello

select *
from salaries
where salary between 40000 and 60000;
-- is between to quickly set high and low parameters

select
emp_no,
to_date,
salary
from salaries
where year(to_date);
-- need to finish

select *
from departments;

select
case dept_no
when 'd001' then 'Marketing'
when 'd002' then 'Finance'
when 'd003' then 'Human Resources'
else 'Other'
end as 'Department Description',
dept_no as 'Department Number'
from departments;
-- Case Statement

select *
from employees
where year(birth_date) >
case
	when Gender = 'M' then 1960
    end;
    
select *
from employees
where gender = 'M'
and year(birth_date) > 1960;
-- This does the same thing as above without using a complicated
-- case statement

select *,
		timestampdiff(year, hire_date, now()) as Tenure
from employees
where 1=case
	when timestampdiff(year, hire_date, now()) = 20 then 1
    else 0
end;
-- sets any row that tenure is 20 equal to 1 and anyting else equal to 0
-- and then returns the rows that include 1's

select *,
		timestampdiff(year, hire_date, now()) as Tenure
from employees
where timestampdiff(year, hire_date, now()) = 20;
-- Another easier way to do the above



