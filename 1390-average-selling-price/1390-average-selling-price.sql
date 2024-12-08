/* Write your T-SQL query statement below */

-- select p.product_id--, isnull(u.units,0) units, isnull(cast(u.units*p.price as float),0) as val
-- from prices p
-- left join unitssold u
-- on u.product_id = p.product_id and  u.purchase_date between p.start_date and p.end_date

select p.product_id, isnull(round(sum(val)/sum(units),2),0) average_price
from 
prices p
left join (
select p.product_id, u.units, isnull(cast(u.units*p.price as float),0) as val
from prices p
left join unitssold u
on u.product_id = p.product_id
where u.purchase_date between p.start_date and p.end_date
) as a
on p.product_id = a.product_id
group by p.product_id