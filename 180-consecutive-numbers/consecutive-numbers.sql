# Write your MySQL query statement below
select l1.num as ConsecutiveNums from logs l1
join logs l2 on l2.id = l1.id - 1
join logs l3 on l3.id = l1.id - 2
where l1.num = l2.num and l1.num = l3.num
group by l1.num
