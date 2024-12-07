/* Write your T-SQL query statement below */


select e.name, b.bonus
from employee e
left join bonus b
on e.empId = b.empid
where bonus < 1000 or bonus is null