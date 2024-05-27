-- Subquery to find the average total amount spent
SELECT * 
FROM customers 
WHERE customer_id IN (
    SELECT customer_id 
    FROM sales 
    GROUP BY customer_id 
    HAVING SUM(total_amount) > (SELECT AVG(total_amount) FROM sales)
);
