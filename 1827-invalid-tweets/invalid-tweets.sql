# Write your MySQL query statement below
select tweet_id from tweets
where character_length(content) > "15"
