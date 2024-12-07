/* Write your T-SQL query statement below */



select st.student_id, st.student_name, ss.subject_name , count(su.student_id) attended_exams
from students st
cross join subjects ss
left join examinations su
on st.student_id = su.student_id and su.subject_name = ss.subject_name
group by st.student_id, st.student_name, ss.subject_name