# Left join example
select P.FirstName, P.LastName, A.City, A.State
    from Person P
left join (
    select City, State, PersonId from Address
) A on P.PersonId = A.PersonId