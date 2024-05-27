--3. Window Functions
--Window functions perform calculations across a set of table rows that are somehow related to the current row.
--Example: Using ROW_NUMBER(), RANK(), and DENSE_RANK() to rank customers by total amount spent.

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
    cs.total_spent,
    ROW_NUMBER() OVER (ORDER BY cs.total_spent DESC) AS row_number,
    RANK() OVER (ORDER BY cs.total_spent DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY cs.total_spent DESC) AS dense_rank
FROM customers c
JOIN CustomerSales cs ON c.customer_id = cs.customer_id;

--Example: Using NTILE() to divide customers into quartiles based on total amount spent.
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
    cs.total_spent,
    NTILE(4) OVER (ORDER BY cs.total_spent DESC) AS quartile
FROM customers c
JOIN CustomerSales cs ON c.customer_id = cs.customer_id;


--Example: Using LEAD() and LAG() to compare a customer's spending with the next and previous customers.
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
    cs.total_spent,
    LEAD(cs.total_spent, 1) OVER (ORDER BY cs.total_spent DESC) AS next_total_spent,
    LAG(cs.total_spent, 1) OVER (ORDER BY cs.total_spent DESC) AS previous_total_spent
FROM customers c
JOIN CustomerSales cs ON c.customer_id = cs.customer_id;


--Example: Using window functions to calculate running totals and moving averages.
WITH MonthlySales AS (
    SELECT 
        DATE_FORMAT(sale_date, '%Y-%m') AS sale_month, 
        SUM(total_amount) AS monthly_sales
    FROM sales
    GROUP BY sale_month
    ORDER BY sale_month
)
SELECT 
    sale_month,
    monthly_sales,
    SUM(monthly_sales) OVER (ORDER BY sale_month) AS running_total,
    AVG(monthly_sales) OVER (ORDER BY sale_month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_average
FROM MonthlySales;
