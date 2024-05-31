START TRANSACTION;

-- Insert a new sale
INSERT INTO sales (customer_id, product_id, sale_date, quantity, total_amount) 
VALUES (1, 2, '2024-05-30', 1, 800.00);

-- Update the product quantity (assuming there's a field for stock, which we haven't defined yet)
UPDATE products 
SET stock = stock - 1 
WHERE product_id = 2;

COMMIT;
