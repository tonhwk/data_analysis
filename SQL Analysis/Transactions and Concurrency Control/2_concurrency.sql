-- Set the isolation level to Repeatable Read
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

START TRANSACTION;

-- Select product details
SELECT * FROM products WHERE product_id = 2;

-- Simulate a delay to allow concurrent transaction to occur
SLEEP(5);

-- Check product details again
SELECT * FROM products WHERE product_id = 2;

COMMIT;