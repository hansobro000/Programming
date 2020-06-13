-- #1
-- Write a query that provides a current head count by each department with a subtotal. 
-- Hint: Use WITH ROLLUP keyword

select
	dp.dept_name,
    format(count(de.emp_no), 0) as 'Employees'
from dept_emp de
inner join departments dp
on de.dept_no = dp.dept_no
where year(to_date) = 9999
group by dept_name with rollup;

-- #2
-- Write a query that uses an inner join to return a table with all columns from salaries and employees

select *
from salaries s
inner join employees e
on s.emp_no = e.emp_no;

-- #3
-- Write a query that returns the complete salary history and demographic information for employee 
-- number = 10002

select *
from salaries s
inner join employees e
on s.emp_no = e.emp_no
where s.emp_no = 10002;

-- #4
-- Write a query that returns the following columns: emp_no, full name (first_name + last_name), 
-- and current salary for all employees

select
	e.emp_no,
    concat(first_name,' ',last_name) as 'Name',
    format(s.salary, 0) as 'Salary'
from employees e
inner join salaries s
on e.emp_no = s.emp_no
where year(to_date) = 9999;

-- #5
-- Revise the query in #3 to include a column for the employee’s job title

select
	e.emp_no,
    concat(first_name,' ',last_name) as 'Name',
    format(s.salary, 0) as 'Salary',
    t.title as 'Title'
from employees e
inner join salaries s
inner join titles t
on e.emp_no = s.emp_no
and e.emp_no = t.emp_no
where year(s.to_date) = 9999;

-- #6
-- What is the name of the department that Georgi Facello works in?

select
	concat(first_name,' ',last_name) as 'Name',
    dept_name as 'Department'
from employees e
inner join dept_emp d
inner join departments dp
on e.emp_no = d.emp_no
and d.dept_no = dp.dept_no
where e.emp_no = 10001;

-- #7
-- Who is Georgi Facello’s manager?

select
	concat(e.first_name,' ',e.last_name) as 'Name',
    concat(em.first_name,' ',em.last_name) as 'Manager'
from employees e
inner join dept_emp d
inner join dept_manager dm
inner join employees em
on e.emp_no = d.emp_no
and d.dept_no = dm.dept_no
and dm.emp_no = em.emp_no
where e.emp_no = 10001
and year(dm.to_date) = 9999;

