--2. Common Table Expressions (CTEs)
--CTEs are used for improving the readability and reusability of complex queries. They can be particularly useful for breaking down complicated queries into simpler parts.
--Example: Calculate the total sales for each customer and use it in a subsequent query.
WITH CustomerSales AS (
    SELECT 
        customer_id, 
        SUM(total_amount) AS total_spent
    FROM sales
    GROUP BY customer_id
)
SELECT 
    c.first_name, 
    c.last_name, 
    cs.total_spent
FROM customers c
JOIN CustomerSales cs ON c.customer_id = cs.customer_id
ORDER BY cs.total_spent DESC;
