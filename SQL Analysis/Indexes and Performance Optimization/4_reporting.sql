--Monthly Sales Analysis with Indexing:
CREATE INDEX idx_sales_date ON sales(sale_date);

SELECT DATE_FORMAT(s.sale_date, '%Y-%m') AS sale_month, SUM(s.total_amount) AS monthly_sales 
FROM sales s 
GROUP BY sale_month 
ORDER BY sale_month;

--Top Selling Products Analysis:
SELECT p.product_name, COUNT(s.sale_id) AS units_sold, SUM(s.total_amount) AS total_revenue 
FROM sales s 
JOIN products p ON s.product_id = p.product_id 
GROUP BY p.product_name 
ORDER BY total_revenue DESC 
LIMIT 5;
