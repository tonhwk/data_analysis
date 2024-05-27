# Advanced SQL Querying Project

## Project Overview
This repository contains SQL queries demonstrating data aggregation and grouping techniques for performing basic data analysis tasks. These queries are designed to showcase skills in SQL for data analytics purposes, particularly focusing on aggregation functions, grouping data, and applying filters on grouped data.

## File Descriptions

### 1. GROUP BY
**File:** `1_group_by.sql`

**Example Query:**
```sql
-- Example: Grouping sales data by product category and calculating total sales amount for each category
SELECT category, SUM(total_amount) AS total_sales
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY category;
```
### 2. HAVING
**File:**  `2_having.sql`

**Example Query:**

```sql
SELECT category, SUM(total_amount) AS total_sales
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY category
HAVING total_sales > 1000;
```

### 3. Window Functions
**File:** `3_aggregate_functions.sql`

**Example Queries:**
Using Using SUM(), AVG(), MAX(), MIN(), COUNT().

```sql
-- Average Sale Amount
SELECT AVG(total_amount) AS average_sale_amount
FROM sales;

-- Maximum and Minimum Sale Amounts
SELECT MAX(total_amount) AS max_sale_amount, MIN(total_amount) AS min_sale_amount
FROM sales;

-- Counting Sales for Each Product
SELECT product_name, COUNT(*) AS sales_count
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY product_name;
```

### How to Use
To run these SQL queries, ensure that you have access to a SQL database containing the necessary tables (sales and products) with appropriate data. Simply copy and paste the queries into your SQL database management tool or client, and execute them to obtain the desired results.

### License
This repository is licensed under the MIT License.




