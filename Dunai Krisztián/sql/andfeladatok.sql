SELECT suppliername, country FROM Suppliers
where (country = 'USA' OR country = 'UK');

SELECT suppliername, city FROM Suppliers
where (city = 'Boston' OR city = 'New Orleans');

SELECT suppliername, country FROM Suppliers
where not (country = 'Japan' OR country = 'Canada');s

SELECT productname, price FROM Products
ORDER BY price ASC;

SELECT productname, price FROM Products
ORDER BY price DESC;

SELECT productname, unit FROM Products
ORDER BY productname ASC, unit desc;
