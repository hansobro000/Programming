-- #1
-- Write a query that retrieves the employee number (emp_no) and associated salary for the 
-- currently highest paid individual in the company

select
emp_no as 'Employee Number',
format(salary, 0) as 'Highest Salary'
from salaries
where to_date = '9999-01-01'
order by salary desc
limit 1;

-- #2
-- Write a query that retrieves the employee number (emp_no) and associated salary for the 
-- currently lowest paid individual in the company.

select
emp_no as 'Employee Number',
format(salary, 0) as 'Lowest Salary'
from salaries
order by salary
limit 1;

-- #3
-- Write a query that shows the current number of employees (i.e. “head count”) in each department. 
-- The only columns that should be in the output table are department number and the total number 
-- of employees. Hint: Use the dept_emp table. 

select
dept_no,
count(emp_no)
from dept_emp
where to_date = '9999-01-01'
group by 
	dept_no;
    
-- #4
-- How many employees currently earn $100,000 or more? 

select
format(count(emp_no), 0) as 'Employees over $100,000'
from salaries
where salary >= '100000'
and to_date = '9999-01-01';

-- #5
-- How many male and female employees are there? The only columns that should be in the output table 
-- are gender and the number of employees. 

select
gender,
format(count(emp_no), 0) as 'Number of employees'
from employees
group by gender;

-- Extra Credit

select
	case dept_no
    when 'd009' then 'Customer Service'
    when 'd004' then 'Production'
    when 'd007' then 'Sales'
    else 'Other'
    end as 'Department',
    format(count(emp_no), 0) as 'Number of Employees'
from dept_emp
group by
	case dept_no
    when 'd009' then 'Customer Service'
    when 'd004' then 'Production'
    when 'd007' then 'Sales'
    else 'Other'
    end;