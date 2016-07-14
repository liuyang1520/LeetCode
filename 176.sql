# Find second highest value of a column if exists, or return null
select max(Salary) as SecondHighestSalary from Employee where Salary < (select max(Salary) from Employee)