-- Example: Grouping sales data by product category and calculating total sales amount for each category
SELECT category, SUM(total_amount) AS total_sales
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY category;