select
substring('Home of the Hawks.',13,3);

select
upper(concat(last_name, ', ', first_name)) as 'Full Name'
from employees;

select
concat(first_name, ' ', last_name) as 'Name',
timestampdiff(year, birth_date, now()) as 'Age'
from employees;

select
timestampdiff(day, '2019-01-01', now()) as 'Days passed since January 1';

select
emp_no,
format(salary/173.33, 0) as MonthlySalary
from salaries
order by MonthlySalary desc;