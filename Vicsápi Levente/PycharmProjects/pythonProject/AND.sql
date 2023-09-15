SELECT SupplierName FROM Suppliers WHERE country = 'USA' or country = 'UK';
SELECT SupplierName FROM  Suppliers WHERE city = 'Boston' or city = 'New Orleans';
SELECT SupplierName FROM  Suppliers WHERE not country = 'Canada' and not country ='Japan';
SELECT SupplierName FROM  Suppliers WHERE not country = 'Canada' and not country ='Japan';

SELECT ProductName, Price FROM Products order by Price ASC;
SELECT ProductName, Price FROM Products order by Price DESC;
SELECT ProductName, Unit FROM Products order by ProductName asc, Unit desc;
