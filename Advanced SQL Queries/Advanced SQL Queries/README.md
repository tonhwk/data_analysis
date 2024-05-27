# Advanced SQL Querying Project

## Project Overview
This project demonstrates advanced SQL querying techniques, including the use of subqueries, Common Table Expressions (CTEs), and window functions. These advanced queries enable complex data analysis and provide deeper insights from the dataset. The project builds on a retail sales analysis scenario, enhancing the basic SQL operations with more sophisticated data manipulation and reporting capabilities.

## File Descriptions

### 1. Subqueries
**File:** `1_subqueries.sql`

**Description:** This file includes examples of subqueries, which are used to perform operations that require multiple steps, such as filtering results based on aggregated values.

**Example Query:**
```sql
-- Retrieve customers who have made purchases above the average sale amount.
SELECT * 
FROM customers 
WHERE customer_id IN (
    SELECT customer_id 
    FROM sales 
    GROUP BY customer_id 
    HAVING SUM(total_amount) > (SELECT AVG(total_amount) FROM sales)
);
```
### 2. Common Table Expressions (CTEs)
**File:**  `2_ctes.sql`

**Description:** This file includes examples of CTEs, which improve the readability and reusability of complex queries by breaking them down into simpler parts.

**Example Query:**

```sql
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
```

### 3. Window Functions
**File:** `3_window_functions.sql`

**Description:** This file includes examples of window functions, which perform calculations across a set of table rows related to the current row, such as ranking, partitioning, and calculating running totals.

**Example Queries:**

Using ROW_NUMBER(), RANK(), and DENSE_RANK()

```sql
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
Using NTILE()
```
```sql
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
Using LEAD() and LAG()
```

```sql
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
```
Calculating Running Totals and Moving Averages

```sql
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
```

### How to Use
Set up the Database: Create and populate the database using the provided SQL scripts in the basic querying section.
Run the Advanced Queries: Use the advanced SQL scripts provided in this project to perform complex data analysis.
### Conclusion
This project showcases the power and flexibility of advanced SQL querying techniques. By using subqueries, CTEs, and window functions, you can perform sophisticated data analysis and gain deeper insights from your datasets. These skills are essential for any data analyst looking to leverage SQL for advanced data manipulation and reporting.


