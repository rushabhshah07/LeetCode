# Write your MySQL query statement below
select e.name from employee e
join (
    select managerid from employee e
    where managerid is not null
    group by managerid
    having count(managerid) >= 5
) m on e.id = m.managerid