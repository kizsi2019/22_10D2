SELECT SupplierName, Country FROM Suppliers WHERE Country = "UK" OR Country = "USA";
SELECT SupplierName, City FROM Suppliers WHERE Country = "USA" AND (City = "Boston" OR City = "New Orleans");
SELECT SupplierName, Country FROM Suppliers WHERE NOT Country = "Japan" AND NOT Country = "Canada";

SELECT ProductName, Price FROM Products ORDER BY Price ASC;
SELECT ProductName, Price FROM Products ORDER BY Price DESC;
SELECT ProductName, Unit FROM Products ORDER BY ProductName ASC, Unit DESC;