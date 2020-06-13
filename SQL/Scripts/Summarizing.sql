select
	distinct title
from titles;

select
	format(sum(salary), 2) as 'Total Wages Paid'
from salaries
where emp_no = 10001;

select
	format(avg(salary), 0) as 'Average Wage Paid'
from salaries
where emp_no = 10001;

select
	round(avg(salary), 0) as 'Average Wage Paid'
from salaries
where emp_no = 10001;
-- same thing as format but no comma formatting

select
	floor(avg(salary)) as 'Average Wage Paid'
from salaries
where emp_no = 10001;
-- floor() function rounds down

select
max(salary),
min(salary)
from salaries;
-- min/max funtions

select
	count(*) as 'Total Female Employees'
from employees
where gender = 'F';

select
	count(distinct title)
from titles;
-- number of distinct titles

select
	emp_no,
    format(avg(salary), 2) as AvgSalary
from salaries
group by emp_no
having avg(salary) >= 140000;
-- 'Where' statement does not work with 'group by' statement. 
-- Need to use 'having' statement to add clauses

-- SQL General Format:
--	Select
--	From
--	Where
--	Group By
--	Having
--	Order By

