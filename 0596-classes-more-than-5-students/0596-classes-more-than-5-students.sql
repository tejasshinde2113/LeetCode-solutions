# Write your MySQL query statement below

select class
from (
select class, count(student) cnt
from courses
group by class
) as a
where cnt >4