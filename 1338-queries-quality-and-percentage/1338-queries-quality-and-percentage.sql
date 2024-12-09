/* Write your T-SQL query statement below */

WITH cte AS (
    SELECT 
        q1.query_name, 
        ROUND((ISNULL(a.less, 0) * 1.0 / COUNT(q1.rating)) * 100, 2) AS poor_query_percentage
    FROM queries q1
    LEFT JOIN (
        SELECT 
            q2.query_name, 
            COUNT(rating) AS less
        FROM queries q2
        WHERE rating < 3
        GROUP BY q2.query_name
    ) AS a
    ON a.query_name = q1.query_name
    GROUP BY q1.query_name, a.less
),
cte2 as (
    select query_name , round(avg(rating*1.0/position),2) quality
    from queries
    group by query_name
)
select cte.query_name, cte2.quality, cte.poor_query_percentage 
from cte2
inner join cte
on cte.query_name = cte2.query_name
