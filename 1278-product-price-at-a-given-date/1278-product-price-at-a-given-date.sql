/* Write your T-SQL query statement below */



select b.product_id, isnull(a.new_price, 10) price
from (select distinct product_id from products) as b
left join 
(select product_id, new_price, rank() over (partition by product_id order by change_date desc) s
from products
where change_date <= '2019-08-16'

) as a
on a.product_id = b.product_id and a.s =1
