/* Write your T-SQL query statement below */




with cte1 as
(select user_id, cast(count(user_id) as float) c1
from confirmations
group by user_id), cte2 as 
(select user_id, cast(isnull(count(user_id),0)as float) c2
from confirmations
where action = 'confirmed'
group by user_id) 
select s.user_id, isnull(x.val,0) confirmation_rate
from signups s
left join (
    select s.user_id, round(isnull((b.c2)/a.c1,0),2) val, b.c2,a.c1
    from  signups s
    left join cte1 a
    on s.user_id = a.user_id
    inner join cte2 b
    on a.user_id = b.user_id
) as x
on x.user_id = s.user_id