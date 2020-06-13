-- #1
select
orderNumber,
(select
sum(od.quantityOrdered*od.priceEach)
from orderdetails od
where od.orderNumber = o.orderNumber) as 'Amount'
from orders o
having amount > 50000
order by amount desc;

-- or class example

select
orderNumber
from orders
where (select
sum(o.quantityOrdered * o.priceEach)
from orderdetails o
where o.orderNumber = orders.orderNumber) > 50000;

-- #2
select
c.customerName,
orderNumber,
(select
sum(od.quantityOrdered*od.priceEach)
from orderdetails od
where od.orderNumber = o.orderNumber) as 'Amount'
from orders o
left join customers c
on o.customerNumber = c.customerNumber
having amount > 50000
order by amount desc;

-- #3
select
c.customerName
from customers c
where not exists
(select
o.customerNumber
from orders o
where c.customerNumber = o.customerNumber);




