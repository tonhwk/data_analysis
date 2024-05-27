-- Adding a new customer or updating an existing one
INSERT INTO customers (customer_id, first_name, last_name, email, phone_number) 
VALUES (1, 'John', 'Doe', 'john.d.new@example.com', '555-1234') 
ON DUPLICATE KEY UPDATE 
first_name = VALUES(first_name), 
last_name = VALUES(last_name), 
email = VALUES(email), 
phone_number = VALUES(phone_number);

-- Adding a new product or updating an existing one
INSERT INTO products (product_id, product_name, category, price) 
VALUES (3, 'Tablet', 'Electronics', 350.00) 
ON DUPLICATE KEY UPDATE 
product_name = VALUES(product_name), 
category = VALUES(category), 
price = VALUES(price);