-- Monthly sales per customer
SELECT 
    c.first_name, 
    c.last_name, 
    DATE_FORMAT(s.sale_date, '%Y-%m') AS sale_month, 
    SUM(s.total_amount) AS monthly_total 
FROM sales s 
JOIN customers c ON s.customer_id = c.customer_id 
GROUP BY c.customer_id, sale_month 
ORDER BY c.customer_id, sale_month;

-- Product performance analysis
SELECT 
    p.product_name, 
    COUNT(s.sale_id) AS units_sold, 
    SUM(s.total_amount) AS total_revenue 
FROM sales s 
JOIN products p ON s.product_id = p.product_id 
GROUP BY p.product_name 
ORDER BY total_revenue DESC;
