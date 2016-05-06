# Write your MySQL query statement below
select W1.Id from Weather W1 inner join Weather W2 on
To_Days(W1.Date) = To_Days(W2.Date) + 1 and W1.Temperature > W2.Temperature;

# Other solutions found in the discussion panel.
SELECT wt1.Id FROM Weather wt1, Weather wt2 WHERE wt1.Temperature > wt2.Temperature AND TO_DAYS(wt1.DATE)-TO_DAYS(wt2.DATE)=1;

select B.Id from Weather A,Weather B where A.Temperature < B.Temperature and datediff(B.Date,A.date)=1
