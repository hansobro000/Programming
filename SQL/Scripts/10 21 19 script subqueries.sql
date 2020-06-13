-- Subqueries

select
	od.orderNumber,
    sum(od.quantityOrdered*od.priceEach) as 'TotalAmount'
from orderdetails od
group by od.orderNumber;

select
	format(avg(ordertotals.totalAmount), 2)
from (select
	od.orderNumber,
    sum(od.quantityOrdered*od.priceEach) as 'TotalAmount'
from orderdetails od
group by od.orderNumber) as ordertotals;
-- this basically creates a virtual table to then perform calculations on.


-- Subquery as a where statement
select
distinct o.customerNumber
from orders o
where year(o.orderDate) = 2003
order by o.customerNumber;

select
c.customerNumber,
c.customerName
from customers c
where c.customerNumber in(
select
distinct o.customerNumber
from orders o
where year(o.orderDate) = 2003
order by o.customerNumber);

-- Subquery as a column

select
customerName,
(select
count(orders.orderNumber)
from orders
where orders.customerNumber = customers.customerNumber) as 'NumberOfOrders'
from customers;
-- This is a correlated subquery. This means it will not run on its own.

