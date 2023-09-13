SELECT * FROM Categories;

SELECT CategoryName FROM Categories;

SELECT CategoryName AND Description FROM Categories;

SELECT Unit, Price, ProductName FROM [Products]

SELECT ProductName, Price FROM Products WHERE Price < 20;

SELECT ProductName, Price FROM Products WHERE Price between 20 and 30;

SELECT ProductName, Price FROM Products WHERE Price > 20;

SELECT ProductName, Price FROM Products WHERE ProductName like 't%';

SELECT DISTINCT Country FROM Suppliers;