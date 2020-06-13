-- #1
select
	concat(e.firstName, e.lastName) as 'Employee Name',
    concat('$', format(sum(od.quantityOrdered*od.priceEach)*0.05, 2)) as SalesCommission
from employees e
inner join customers c
on e.employeeNumber = c.salesRepEmployeeNumber
inner join orders o
on c.customerNumber = o.customerNumber
inner join orderdetails od
on o.orderNumber = od.orderNumber
group by e.employeeNumber
order by SalesCommission desc;

-- #2
create view OrderAmount as
select
	o.customerNumber,
    od.orderNumber,
    sum(od.quantityOrdered * od.priceEach) as 'Amount'
from orderdetails od
left join orders o
on od.orderNumber = o.orderNumber
group by o.customerNumber
order by o.customerNumber;

create view PaymentAmount as
select
	p.customerNumber,
    c.customerName,
    sum(p.amount) as 'Amount'
from payments p
left join customers c
on p.customerNumber = c.customerNumber
group by p.customerNumber;

select
	o.customerNumber,
    p.customerName,
    concat('$', format(sum(o.Amount - p.Amount), 2)) as 'AmountDue'
from OrderAmount o
left join PaymentAmount p
on o.customerNumber = p.customerNumber
group by o.customerNumber;

-- #3
create table NeverPurchased (
	ProductCode		varchar(15) not null,
    ProductName		varchar(70),
    ProductLine 	varchar(50),
    BuyPrice		decimal(10,2)
);

insert into NeverPurchased
	(ProductCode, ProductName, ProductLine, BuyPrice)
select 
p.ProductCode,
p.ProductName,
p.ProductLine,
p.BuyPrice
from products p
where not exists
(select null
from orderdetails od
where od.productCode = p.productCode);

select *
from NeverPurchased;

set SQL_SAFE_UPDATES = 0;
update NeverPurchased
	set buyPrice = buyPrice*0.9;
set SQL_SAFE_UPDATES = 1;




