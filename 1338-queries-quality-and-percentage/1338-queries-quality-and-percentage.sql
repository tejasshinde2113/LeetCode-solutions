/* Write your T-SQL query statement below */


select query_name,

round(avg(rating*1.0/position),2) quality ,

round(100*1.0*count(case when rating < 3 then 1 end)/count(rating),2) poor_query_percentage 

from queries
group by query_name