/* Write your T-SQL query statement below */



    

select a.name 
from employee a
inner join (
    select aa.managerid, count(aa.managerid) cnt
    from employee aa
    where aa.managerid is not null
    group by aa.managerid
) as b
on a.id = b.managerid
where b.cnt >=5