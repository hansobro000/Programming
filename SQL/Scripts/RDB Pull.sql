-- Join whole DB
select *
from offices off
left join employees emp
on off.officeCode = emp.officeCode
left join customers cus
on emp.employeeNumber = cus.salesRepEmployeeNumber
left join payments pay
on cus.customerNumber = pay.customerNumber
left join orders ord
on pay.customerNumber = ord.customerNumber
left join orderdetails ordd
on ord.orderNumber = ordd.orderNumber
left join products pro
on ordd.productCode = pro.productCode
left join productlines prl
on pro.productLine = prl.productLine;