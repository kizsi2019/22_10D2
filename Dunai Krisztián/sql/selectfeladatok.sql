select * from Customers;
select categoryname from categories;
select categoryname and description from categories;
select unit, price, productname from products;
select productname, price from products where price < 20;
select productname, price from products where price between 20 and 30;
select productname, price from products where price > 20;
select productname, price from products where productname like 't%';
select distinct country from suppliers;