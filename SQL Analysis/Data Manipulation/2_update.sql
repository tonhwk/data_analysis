-- Updating the email of a customer
UPDATE customers 
SET email = 'john.d.new@example.com' 
WHERE customer_id = 1;


-- Updating the price of a product
UPDATE products 
SET price = 750.00 
WHERE product_id = 2;

-- Updating the quantity and total_amount of a sale
UPDATE sales 
SET quantity = 3, total_amount = 2400.00 
WHERE sale_id = 2;