/* Write your T-SQL query statement below */

select isnull((select top 1 num
from Mynumbers
group by num
having count(num) = 1
order by num desc), null) as num 
