-- Example: Calculating the average sale amount
SELECT AVG(total_amount) AS average_sale_amount
FROM sales;

-- Example: Finding the maximum and minimum sale amounts
SELECT MAX(total_amount) AS max_sale_amount, MIN(total_amount) AS min_sale_amount
FROM sales;

-- Example: Counting the number of sales for each product
SELECT product_name, COUNT(*) AS sales_count
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY product_name;