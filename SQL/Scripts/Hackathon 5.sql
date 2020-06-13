-- # 1
select
	orderNumber,
    format(sum(quantityOrdered*priceEach), 2) as 'Amount'
from orderdetails
group by orderNumber;

-- # 2
create view OrderTotalsVIEW as
select
	orderNumber,
    format(sum(quantityOrdered*priceEach), 2) as 'Amount'
from orderdetails
group by orderNumber;

select *
from OrderTotalsVIEW;

-- # 3
select
    c.customerName,
    d.orderNumber,
    format(sum(d.quantityOrdered*d.priceEach), 2) as 'Amount'
from customers c
left join orders o
on c.customerNumber = o.customerNumber
left join orderdetails d
on o.orderNumber = d.orderNumber
where c.customerNumber = 131
group by d.orderNumber;










