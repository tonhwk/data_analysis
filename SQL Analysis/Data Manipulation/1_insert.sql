-- Adding a new customer to the customers table
INSERT INTO customers (first_name, last_name, email, phone_number) 
VALUES ('Robert', 'Brown', 'robert.brown@example.com', '555-4321');

-- Adding a new product to the products table
INSERT INTO products (product_name, category, price) 
VALUES ('Headphones', 'Electronics', 150.00);

-- Adding a new sale to the sales table
INSERT INTO sales (customer_id, product_id, sale_date, quantity, total_amount) 
VALUES (1, 4, '2023-04-10', 2, 300.00);