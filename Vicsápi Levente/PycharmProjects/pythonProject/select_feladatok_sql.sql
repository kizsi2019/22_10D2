SELECT * FROM Customers;
SELECT * FROM Categories;
SELECT CategoryName FROM Categories;
SELECT ProductName, Price FROM Products;
SELECT ProductName, Price FROM Products WHERE price < 20;
SELECT ProductName, Price FROM Products WHERE price BETWEEN 20 and 30;
SELECT ProductName, Price FROM Products WHERE price <> 10;
SELECT ProductName, Unit, Price FROM Products WHERE ProductName LIKE "t%";
SELECT ProductName, Unit, Price FROM Products WHERE ProductName LIKE "Louisiana%";

