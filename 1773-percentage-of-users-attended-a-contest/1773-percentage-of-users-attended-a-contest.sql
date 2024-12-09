# Write your MySQL query statement below

select r.contest_id, round((count(r.contest_id)*1.0/allval)*100.0,2) percentage
from register r
join (select count(user_id) as allval 
        from users) as cnt
group by r.contest_id
order by percentage desc, r.contest_id