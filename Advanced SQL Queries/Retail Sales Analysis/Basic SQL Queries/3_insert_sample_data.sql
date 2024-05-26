INSERT INTO customers (first_name, last_name, email, phone_number) VALUES
('John', 'Doe', 'john.doe@example.com', '555-1234'),
('Jane', 'Smith', 'jane.smith@example.com', '555-5678'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-8765');

INSERT INTO products (product_name, category, price) VALUES
('Laptop', 'Electronics', 1200.00),
('Smartphone', 'Electronics', 800.00),
('Tablet', 'Electronics', 400.00);

INSERT INTO sales (customer_id, product_id, sale_date, quantity, total_amount) VALUES
(1, 1, '2023-01-15', 1, 1200.00),
(2, 2, '2023-02-20', 2, 1600.00),
(3, 3, '2023-03-05', 1, 400.00);
