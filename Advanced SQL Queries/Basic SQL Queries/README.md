# Basic SQL Querying 

## Project Overview 

This project demonstrates the use of SQL for basic querying and database management. The project includes scripts for creating a database, defining tables, inserting sample data, and performing various SQL queries. These queries cover essential SQL operations like selection, filtering, ordering, distinct values, pagination, joins, aggregations, and advanced data analysis. 

## File Descriptions 
### 1. Create Database 
```sql 
CREATE DATABASE retail_sales_analysis;
```
Creates a new database named retail_sales_analysis.


### 2. Create Tables
```sql
CREATE TABLE customers ( customer_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(100), phone_number VARCHAR(15) );



CREATE TABLE products ( product_id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(100), category VARCHAR(50), price DECIMAL(10, 2) );

 
CREATE TABLE sales ( sale_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, product_id INT, sale_date DATE, quantity INT, total_amount DECIMAL(10, 2), FOREIGN KEY (customer_id) REFERENCES customers (customer_id), FOREIGN KEY (product_id) REFERENCES products (product_id) );
 ```
 Creates the customers, products, and sales tables with appropriate fields and constraints.


### 3. Insert Sample Data
 ```sql
INSERT INTO customers (first_name, last_name, email, phone_number) VALUES ('John', 'Doe', 'john.doe@example.com', '555-1234'), ('Jane', 'Smith', 'jane.smith@example.com', '555-5678'), ('Alice', 'Johnson', 'alice.johnson@example.com', '555-8765'); 

INSERT INTO products (product_name, category, price) VALUES ('Laptop', 'Electronics', 1200.00), ('Smartphone', 'Electronics', 800.00), ('Tablet', 'Electronics', 400.00); 

INSERT INTO sales (customer_id, product_id, sale_date, quantity, total_amount) VALUES (1, 1, '2023-01-15', 1, 1200.00), (2, 2, '2023-02-20', 2, 1600.00), (3, 3, '2023-03-05', 1, 400.00);
 ```
Inserts sample data into the customers, products, and sales tables.


### 4. Select Statement
 ```sql
-- Retrieve all columns from the customers table 
SELECT * FROM customers;
```
Demonstrates a basic SELECT statement to retrieve all records from the customers table.


### 5. WHERE Clause
 ```sql
-- Retrieve customers with the last name 'Doe' 
SELECT * FROM customers WHERE last_name = 'Doe';
```
Filters records using the WHERE clause.


### 6. ORDER BY
```sql
-- Retrieve all products ordered by price in descending order 
SELECT * FROM products ORDER BY price DESC;
```
Sorts records using the ORDER BY clause.


### 7. DISTINCT
```sql
-- Retrieve distinct product categories 
SELECT DISTINCT category FROM products;
```
Retrieves distinct values from a column.


### 8. LIMIT and OFFSET
```sql
-- Retrieve the first 2 customers 
SELECT * FROM customers LIMIT 2; 
-- Retrieve the second set of 2 customers (for pagination) 
SELECT * FROM customers LIMIT 2 OFFSET 2;
```
Limits the number of records returned and uses offset for pagination.


### 9. JOIN Queries
```sql
SELECT s.sale_id, c.first_name, c.last_name, p.product_name, s.sale_date, s.quantity, s.total_amount FROM sales s JOIN customers c ON s.customer_id = c.customer_id JOIN products p ON s.product_id = p.product_id;
```
Joins multiple tables to retrieve combined data.


### 10. Aggregation Queries
```sql
SELECT c.first_name, c.last_name, SUM(s.total_amount) AS total_spent FROM sales s JOIN customers c ON s.customer_id = c.customer_id GROUP BY c.customer_id ORDER BY total_spent DESC;
```
Aggregates data using SUM and GROUP BY.


### 11. Advanced Queries
```sql
-- Find the top-selling product categories 
SELECT category, SUM(quantity) AS total_sold FROM sales s JOIN products p ON s.product_id = p.product_id GROUP BY category ORDER BY total_sold DESC; 
-- Calculate monthly sales totals 
SELECT DATE_FORMAT(sale_date, '%Y-%m') AS sale_month, SUM(total_amount) AS monthly_sales FROM sales GROUP BY sale_month ORDER BY sale_month;
```
Includes advanced queries for detailed data analysis.


### 12. Reporting Insights
```sql
-- Monthly sales per customer 
SELECT c.first_name, c.last_name, DATE_FORMAT(s.sale_date, '%Y-%m') AS sale_month, SUM(s.total_amount) AS monthly_total FROM sales s JOIN customers c ON s.customer_id = c.customer_id GROUP BY c.customer_id, sale_month ORDER BY c.customer_id, sale_month; 
-- Product performance analysis 
SELECT p.product_name, COUNT(s.sale_id) AS units_sold, SUM(s.total_amount) AS total_revenue FROM sales s JOIN products p ON s.product_id = p.product_id GROUP BY p.product_name ORDER BY total_revenue DESC;
```
Includes queries for generating reports and insights from the data.


How to Use
1. Install MySQL and MySQL Workbench.
2. Start your MySQL server.
3. Open MySQL Workbench and connect to your local MySQL server.
4. Execute the SQL scripts in the provided order.
By following these steps, you can recreate the database, populate it with sample data, and run various SQL queries to analyze and extract insights from the data.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or feedback, please contact Antonio Martinez at andresreg93@gmail.com.

