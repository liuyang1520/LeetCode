# Note that "as Customers" is necessary, or will get error!!!
# not in
select Name as Customers from Customers where Customers.Id not in (select CustomerId from Orders);
# not exists
select Name as Customers from Customers where not exists (select CustomerId from Orders where Customers.Id = Orders.CustomerId);
# left join should also work