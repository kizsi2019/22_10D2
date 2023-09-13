Select SupplierName, Country from Suppliers
where (country = 'USA' or country = 'UK');

Select SupplierName, City from Suppliers
where (city = 'Boston' or city = 'New Orleans');


Select SupplierName, Country from Suppliers
where not (Country = 'Japan' or Country = 'Canada');

Select ProductName, Price from Products
order by price ASC;


Select ProductName, Price from Products
order by price DESC;

Select ProductName, unit from Products
order by productname ASC, unit DESC
