/* Write your T-SQL query statement below */

select distinct num ConsecutiveNums
from (
    select l1.num
    from logs l1
    inner join logs l2 on l2.id -1 = l1.id
    inner join logs l3 on l3.id - 1 = l2.id
    where l1.num = l2.num and l2.num = l3.num
) as s