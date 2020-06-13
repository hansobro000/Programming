-- #1
create view NoCustomerAssigned as
select
e.employeeNumber,
e.firstName,
e.lastName,
e.jobTitle
from employees e
left join customers c
on e.employeeNumber = c.salesRepEmployeeNumber
where c.salesRepEmployeeNumber is null;

select *
from NoCustomerAssigned;

-- #2
select
e.employeeNumber,
e.firstName,
e.lastName,
e.jobTitle
from employees e
where not exists
(select
c.salesRepEmployeeNumber
from customers c
where e.employeeNumber = c.salesRepEmployeeNumber);

-- #3
create view PLineQuantity as
select
p.productLine,
format(sum(o.quantityOrdered), 0) as 'QuantityOrdered'
from orderdetails o
left join products p
on o.productCode = p.productCode
group by p.productLine;

select *
from PLineQuantity;

-- #4
select
p.productLine,
sum((select
sum(o.quantityOrdered)
from orderdetails o
where o.productCode = p.productCode)) as 'QuantityOrdered'
from products p
group by p.productLine;






