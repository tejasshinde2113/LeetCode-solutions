/* Write your T-SQL query statement below */

declare @c as int
set @c = (select count(distinct product_key) from product)

select distinct customer_id
from customer
where customer_id in (
    select customer_id
    from customer
    group by customer_id
    having count(distinct product_key) = @c
    )
