#1
-- Write a query that provides a current head count by each department with a subtotal. 
-- Hint: Use WITH ROLLUP keyword.

select 
dept_no as Department,
format(count(emp_no), 0) as 'Number of Employees'
from dept_emp
group by dept_no with rollup;

-- #2
-- Write a query that uses an inner join to return a table with all columns from
-- salaries and employees

select *
from salaries
inner join employees
on salaries.emp_no = employees.emp_no;

-- #3
-- Write a query that returns the complete salary history and demographic information 
-- for employee number = 10002