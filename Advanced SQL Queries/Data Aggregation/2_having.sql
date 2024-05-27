-- Example: Finding product categories with total sales amount greater than $1000
SELECT category, SUM(total_amount) AS total_sales
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY category
HAVING total_sales > 1000;