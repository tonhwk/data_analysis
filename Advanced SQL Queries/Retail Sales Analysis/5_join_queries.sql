SELECT s.sale_id, c.first_name, c.last_name, p.product_name, s.sale_date, s.quantity, s.total_amount
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id;
