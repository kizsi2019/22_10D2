SELECT SupplierName, Country FROM Suppliers WHERE Country = 'USA' OR Country = 'UK';
SELECT SupplierName, City FROM Suppliers WHERE City = 'Boston' OR City = 'New Orleans';
SELECT SupplierName, Country FROM Suppliers WHERE NOT Country = 'Japan' AND NOT Country = 'Canada';

SELECT ProductName, Price FROM Products ORDER BY Price;
SELECT ProductName, Price FROM Products ORDER BY Price DESC;
SELECT ProductName, Unit FROM Products ORDER BY ProductName ASC, Unit DESC;