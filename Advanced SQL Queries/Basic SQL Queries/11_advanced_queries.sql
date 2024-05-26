-- Find the top-selling product categories
SELECT 
    category, 
    SUM(quantity) AS total_sold 
FROM sales s 
JOIN products p ON s.product_id = p.product_id 
GROUP BY category 
ORDER BY total_sold DESC;

-- Calculate monthly sales totals
SELECT 
    DATE_FORMAT(sale_date, '%Y-%m') AS sale_month, 
    SUM(total_amount) AS monthly_sales 
FROM sales 
GROUP BY sale_month 
ORDER BY sale_month;