-- Transaction 1
START TRANSACTION;

-- Check stock availability
SELECT stock FROM products WHERE product_id = 2 FOR UPDATE;

-- Simulate processing time
SLEEP(5);

-- Update stock if available
UPDATE products 
SET stock = stock - 1 
WHERE product_id = 2 AND stock > 0;

-- Commit transaction
COMMIT;

-- Transaction 2 (similar steps)
START TRANSACTION;

-- Check stock availability
SELECT stock FROM products WHERE product_id = 2 FOR UPDATE;

-- Simulate processing time
SLEEP(5);

-- Update stock if available
UPDATE products 
SET stock = stock - 1 
WHERE product_id = 2 AND stock > 0;

-- Commit transaction
COMMIT;
