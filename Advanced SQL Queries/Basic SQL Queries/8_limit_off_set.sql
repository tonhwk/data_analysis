-- Retrieve the first 2 customers
SELECT * FROM customers LIMIT 2;

-- Retrieve the second set of 2 customers (for pagination)
SELECT * FROM customers LIMIT 2 OFFSET 2;
