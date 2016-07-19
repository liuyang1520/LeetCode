# Write your MySQL query statement below
select
    T.Name as Department,
    S.Name as Employee,
    S.Salary
from 
    (select 
        E1.Name,
        Salary,
        E1.DepartmentId
    from Employee E1 
    inner join (
        select DepartmentId, max(Salary) as maxSalary from Employee group by DepartmentId
    ) E2
    where E1.DepartmentId = E2.DepartmentId and E1.Salary = E2.maxSalary) S
inner join (
    select Id, Name from Department 
) T
where S.DepartmentId = T.Id