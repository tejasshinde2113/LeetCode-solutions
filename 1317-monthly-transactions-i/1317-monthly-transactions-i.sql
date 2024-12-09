/* Write your T-SQL query statement below */


select 
        concat(year(trans_date),'-',FORMAT(MONTH(trans_date), '00')) month    , 
        country, 
        count(id) as trans_count,
        isnull(count(case state when 'approved' then 1 end),0)  approved_count,
        isnull(sum(amount),0)  trans_total_amount,
        isnull(sum(case state when 'approved' then amount end),0)  approved_total_amount 

from transactions
group by country, month(trans_date),year(trans_date)