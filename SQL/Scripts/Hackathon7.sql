-- #1

delimiter $$
create procedure customerOrders (cusOrd int)
begin
select *
from orders
where customerNumber = cusOrd;
end$$
delimiter ;

-- #2

call customerOrders (131);

-- #3
delimiter $$
create procedure CanceledOrder (CancOrd int)
begin
select *
from orderdetails od
where od.orderNumber = CancOrd;
end$$
delimiter ;

call CanceledOrder (10248);

select
	orderNumber,
    sum(quantityOrdered*priceEach) as 'Amount'
from orderdetails
where orderNumber = 10248



