-- # 1
select
officeCode,
city,
state,
country
from offices;

-- # 2
select
e.employeeNumber,
concat(e.firstName,' ',e.lastName) as 'Name'
from offices o
left join employees e
on o.officeCode = e.officeCode
where o.officeCode = 1;

-- #3
select
o.orderNumber,
o.orderDate
from orders o
left join customers c
on o.customerNumber = c.customerNumber
where c.customerNumber = 114;

-- #4
select
p.checkNumber,
p.paymentDate,
format(p.amount, 2) as 'Amount'
from customers c
left join payments p
on c.customerNumber = p.customerNumber
where c.customerNumber = 114
order by paymentDate;

-- #5
select
	c.customerName,
	o.orderDate,
    format(sum(od.quantityOrdered*od.priceEach), 0) as 'Amount'
from customers c
left join orders o
on c.customerNumber = o.customerNumber
left join orderdetails od
on o.orderNumber = od.orderNumber
where c.customerNumber = 114
and o.orderDate = '2004-11-24'
group by o.orderDate;