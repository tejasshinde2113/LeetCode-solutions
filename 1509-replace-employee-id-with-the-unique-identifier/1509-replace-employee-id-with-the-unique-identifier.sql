/* Write your T-SQL query statement below */

select isnull(u.unique_id,null) unique_id , e.name
from employees e 
left join employeeUNI u
on u.id = e.id