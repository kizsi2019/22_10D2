SELECT * FROM Category;

SELECT CategoryName FROM Category;

SELECT ProductName, Unit, Price FROM Products;

SELECT ProductName, Unit, Price FROM Products WHERE Price <20;

SELECT ProductName, Unit, Price FROM Products WHERE Price BETWEEN 20 AND 30;

SELECT ProductName, Unit, Price FROM Products WHERE Price <>10;

SELECT * FROM Products WHERE ProductName LIKE 'T%';

SELECT * FROM Products WHERE ProductName LIKE 'Louisiana%';