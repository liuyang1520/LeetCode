# Note the problem ask you to delete rows in table!! Not the following statement
# select min(id), Email from Person group by id
# Write your MySQL query statement below
delete P1 from Person P1 inner join Person P2 where P1.Id > P2.Id and P1.Email = P2.Email