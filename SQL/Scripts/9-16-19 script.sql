select 
dept_no,
count(emp_no)
from dept_manager
group by dept_no;

select 
	case dept_no
	when 'd001' then 'Marketing'
	when 'd002' then 'Finance'
	else 'Other'
	end as 'Department',
	count(emp_no) as 'Number of Managers'
from dept_manager
group by 
	case dept_no
	when 'd001' then 'Marketing'
	when 'd002' then 'Finance'
	else 'Other'
	end
    order by dept_no;
    
select 
	year(hire_date) as HireYear,
    count(emp_no) as NumberOfEmployees
from employees
group by year (hire_date) with rollup;