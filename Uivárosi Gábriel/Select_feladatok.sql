SELECT * From Categories;

SELECT CategoryName AND Description From Categories;

SELECT 	ProductName, Unit, Price FROM Products Where Price < 20;

SELECT 	ProductName, Unit, Price FROM Products Where Price Between 20 and 30;

SELECT 	ProductName, Unit, Price FROM Products Where Price <> 10; 

SELECT 	ProductName, Unit, Price FROM Products Where ProductName like "t%";

SELECT 	ProductName FROM Products Where ProductName like "Louisiana%";

SELECT * FROM Customers
	where not 	Country = 'Germany';
    
SELECT * FROM Customers
ORder By Country;

SELECT * FROM Customers
	ORder By Country Desc;

SELECT * FROM Customers
	ORder By Country Desc, 	ContactName asc;

SELECT 	SupplierName, Country FROM Suppliers Where Country = 'USA' OR Country = 'UK';

SELECT 	SupplierName, City, Country FROM Suppliers Where City = 'New Orleans' OR City = 'Boston';

SELECT 	ProductName, Price  FROM Products ORder by price asc;

SELECT 	ProductName, Price  FROM Products ORder by price DESC;

SELECT 	ProductName, unit  FROM Products ORder by 
ProductName asc, Unit Desc;

insert into  Categories	(CategoryName, Description);
values ('Botka', 'VERY HORNY')