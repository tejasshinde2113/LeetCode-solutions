/* Write your T-SQL query statement below */

-- select avg(immediate_percentage) immediate_percentage
-- from (
-- select round(1.0*100*count(case when d.order_date = d.customer_pref_delivery_date then 1 end)/(count(d.customer_id)) ,2) immediate_percentage 
-- from delivery d
-- inner join (
--     select * , rank() over (partition by customer_id order by order_date) as val
--     from delivery) as k
--     on k.customer_id = d.customer_id
-- where val = 1
-- group by d.customer_id
-- ) as s


WITH cte AS (
    SELECT
        customer_id,
        order_date,
        RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS r,
        customer_pref_delivery_date
    FROM
        Delivery
)
SELECT
    ROUND(
        CAST(100*COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END) AS decimal) /
        CAST(COUNT(customer_id) AS decimal),
    2) AS immediate_percentage
FROM
    cte
WHERE r = 1;



