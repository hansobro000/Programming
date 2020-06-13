select *
from customers c
left join orders o
on c.customerNumber = o.customerNumber;

select *
from customers c
inner join orders o
on c.customerNumber = o.customerNumber;
-- This is the difference between left join and inner join. inner join is everything thrown at you at once
-- Anything that matches will get returned. left join will tie the data from the second table with the data
-- in the first table in the order that the first table occurs in.

select *
from orders o
left join customers c
on o.customerNumber = c.customerNumber;

select *
from customers c
left join orders o
on c.customerNumber = o.customerNumber
where o.customerNumber is not null;
-- only the customers that placed orders

select *
from customers c
left join orders o
on c.customerNumber = o.customerNumber
where o.customerNumber is null;
-- only the customers that didn't place orders

select *
from customers c
right join orders o
on c.customerNumber = o.customerNumber;

select *
from orders o
left join customers c
on o.customerNumber = c.customerNumber;
-- these two statements return the same results, just in different orders

