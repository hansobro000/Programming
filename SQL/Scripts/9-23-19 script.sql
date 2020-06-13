select *
from dept_manager
inner join employees
on dept_manager.emp_no = employees.emp_no;

select *
from dept_manager d
inner join employees e
on d.emp_no = e.emp_no;

select *
from employees
where emp_no = 110022
or emp_no = 110039;

select *
from employees e
inner join dept_manager d
on e.emp_no = d.emp_no;

select
	d.emp_no,
    e.first_name,
    e.last_name,
    e.gender,
    dp.dept_name
from dept_manager d
inner join employees e
on d.emp_no = e.emp_no
inner join departments dp
on dp.dept_no = d.dept_no;

select
	d.emp_no,
    e.first_name,
    e.last_name,
    e.gender,
    dp.dept_name
from dept_manager d
inner join employees e
inner join departments dp
on d.emp_no = e.emp_no
and dp.dept_no = d.dept_no;
