# SQL Indexing and Performance Optimization

## Project Overview
This repository contains SQL queries demonstrating essential techniques for improving database performance through indexing, understanding query execution plans using `EXPLAIN`, and various performance tuning strategies. Additionally, it includes example queries for generating insightful reports.

## File Descriptions

### 1. Indexes
**File:** `1_indexes.sql`

**Example Query:**
Creating indexes to optimize query performance.


```sql
-- Adding an index to the customers table
CREATE INDEX idx_customers_last_name ON customers(last_name);

-- Adding an index to the products table
CREATE INDEX idx_products_category ON products(category);

-- Adding a composite index to the sales table for queries involving both customer_id and sale_date
CREATE INDEX idx_sales_customer_date ON sales(customer_id, sale_date);
```
### 2. EXPLAIN
**File:**  `2_explain.sql`

**Example Query:**
Using EXPLAIN to analyze query execution plans.


```sql
EXPLAIN SELECT s.sale_id, c.first_name, c.last_name, p.product_name, s.sale_date, s.quantity, s.total_amount 
FROM sales s 
JOIN customers c ON s.customer_id = c.customer_id 
JOIN products p ON s.product_id = p.product_id;
```

### 3. Performance Tuning
**File:** `3_performance_tuning.sql`

**Example Queries:**
Optimizing queries for better performance.

```sql
--Before Optimization
SELECT s.sale_id, c.first_name, c.last_name, p.product_name, s.sale_date, s.quantity, s.total_amount 
FROM sales s 
JOIN customers c ON s.customer_id = c.customer_id 
JOIN products p ON s.product_id = p.product_id;

--After Optimization (with selected columns and indexed fields):
SELECT s.sale_id, c.first_name, c.last_name, p.product_name, s.sale_date, s.quantity, s.total_amount 
FROM sales s 
JOIN customers c ON s.customer_id = c.customer_id 
JOIN products p ON s.product_id = p.product_id 
WHERE c.last_name = 'Doe' AND s.sale_date >= '2023-01-01';

```


### 4. Reporting
**File:** `4_reporting.sql`

**Example Queries:**
Generating insightful reports using optimized queries.

```sql
-- Monthly Sales Analysis with Indexing:
CREATE INDEX idx_sales_date ON sales(sale_date);

SELECT DATE_FORMAT(s.sale_date, '%Y-%m') AS sale_month, SUM(s.total_amount) AS monthly_sales 
FROM sales s 
GROUP BY sale_month 
ORDER BY sale_month;

-- Top Selling Products Analysis:
SELECT p.product_name, COUNT(s.sale_id) AS units_sold, SUM(s.total_amount) AS total_revenue 
FROM sales s 
JOIN products p ON s.product_id = p.product_id 
GROUP BY p.product_name 
ORDER BY total_revenue DESC 
LIMIT 5;


```

### How to Use
To run these SQL queries, ensure that you have access to a SQL database containing the necessary tables (customers, products, and sales) with appropriate data. Simply copy and paste the queries into your SQL database management tool or client, and execute them to perform the desired indexing, analysis, and performance optimization operations.

### License
This repository is licensed under the MIT License - see the LICENSE file for details.

### Contact
For any questions or feedback, please contact Antonio Martinez at andresreg93@gmail.com.





