# Write your MySQL query statement below

select activity_date day, count(distinct user_id) active_users
from activity
where activity_date between date_sub('2019-07-28', INTERVAL 30 DAY) and '2019-07-27'
group by activity_date