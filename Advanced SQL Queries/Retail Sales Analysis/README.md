# Advanced SQL Analysis Project

## Overview

This project demonstrates advanced SQL analysis techniques and showcases proficiency in SQL for data analysis. It includes a collection of SQL scripts for analyzing various datasets, extracting insights, and generating reports. The queries cover a wide range of topics, from basic data retrieval to complex joins, aggregations, and reporting.


## Scripts

### 1. `1_basic_queries.sql`
Contains basic SQL queries for retrieving data from single tables.

### 2. `2_join_queries.sql`
Includes SQL queries that join multiple tables to extract combined information.

### 3. `3_aggregation_queries.sql`
Contains SQL queries for aggregating data and calculating summary statistics.

### 4. `4_advanced_queries.sql`
Demonstrates advanced SQL queries for complex data analysis tasks.

### 5. `5_reporting_insights.sql`
Includes SQL queries for generating insightful reports and visualizations from the data.

## Usage

1. **Database Setup**: Ensure you have a SQL database set up to run the queries.
2. **Script Execution**: Open each SQL script in your SQL editor (e.g., MySQL Workbench) and execute them in order.
3. **Analysis**: Use the results of the queries to analyze the dataset and derive insights.

## Example Queries

### Basic Query
```sql
SELECT * FROM customers;
```

### Join Query
```sql
SELECT s.sale_id, c.first_name, c.last_name, p.product_name, s.sale_date, s.quantity, s.total_amount
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id;
```

### Aggregation Query
```sql
SELECT c.first_name, c.last_name, SUM(s.total_amount) AS total_spent
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC;
```

### Advanced Query
```sql
-- Find top-selling product categories
SELECT category, SUM(quantity) AS total_sold
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY category
ORDER BY total_sold DESC;

-- Calculate monthly sales totals
SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month, SUM(total_amount) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;
```

### Reporting Query
```sql
-- Monthly sales per customer
SELECT c.first_name, c.last_name, DATE_FORMAT(s.sale_date, '%Y-%m') AS month, SUM(s.total_amount) AS monthly_spent
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_id, month
ORDER BY c.customer_id, month;

-- Product performance analysis
SELECT p.product_name, COUNT(s.sale_id) AS times_sold, SUM(s.total_amount) AS total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_revenue DESC;

```
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or feedback, please contact Antonio Martinez at andresreg93@gmail.com.
