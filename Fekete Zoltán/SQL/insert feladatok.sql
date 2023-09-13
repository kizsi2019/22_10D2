INSERT INTO Categories (CategoryName, Description)
VALUES ('Seafood', 'Squid, Salmon')

INSERT INTO Categories (CategoryName)
VALUES ('Produce')

SELECT * FROM Categories WHERE Description IS NULL;