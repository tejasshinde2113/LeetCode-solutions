/* Write your T-SQL query statement below */


select *
from cinema
where description not in ('boring') and id%2 != 0
order by rating desc