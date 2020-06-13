-- #1

select
c.customerName,
o.orderNumber
from orders o
left join customers c
on o.customerNumber = c.customerNumber
where shippedDate is null;

-- # 2

select
p.productCode,
p.productName,
p.productDescription
from products p
left join orderdetails o
on p.productCode = o.productCode
where o.productCode is null;

-- # 3

select
concat(e.firstName,' ',e.lastName) as 'No Customer Assigned'
from employees e
left join customers c
on e.employeeNumber = c.salesRepEmployeeNumber
where c.salesRepEmployeeNumber is null;

-- # 4

select
c.customerName,
count(o.customerNumber) as 'Number of Orders'
from customers c
left join orders o
on c.customerNumber = o.customerNumber
group by c.customerNumber;
