# Write your MySQL query statement below
select * from Cinema
where (Id % 2) != 0 and description != 'boring'
order by rating DESC; 