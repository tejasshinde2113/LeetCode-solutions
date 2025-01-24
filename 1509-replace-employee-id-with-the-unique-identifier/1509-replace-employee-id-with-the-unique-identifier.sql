/* Write your T-SQL query statement below */

select u.unique_id unique_id , e.name
from employees e 
left join employeeUNI u
on u.id = e.id