# Data Manipulation

## Project Overview
This repository contains SQL queries demonstrating essential data manipulation techniques. These queries showcase skills in SQL for database management, focusing on inserting new records, updating existing records, deleting records, and performing upsert (merge) operations.


## File Descriptions

### 1. INSERT
**File:** `1_insert.sql`

**Example Query:**
Adding new records to the customers, products, and sales tables.

```sql
-- Adding a new customer to the customers table
INSERT INTO customers (first_name, last_name, email, phone_number) 
VALUES ('Robert', 'Brown', 'robert.brown@example.com', '555-4321');

-- Adding a new product to the products table
INSERT INTO products (product_name, category, price) 
VALUES ('Headphones', 'Electronics', 150.00);

-- Adding a new sale to the sales table
INSERT INTO sales (customer_id, product_id, sale_date, quantity, total_amount) 
VALUES (1, 4, '2023-04-10', 2, 300.00);
```
### 2. UPDATE
**File:**  `2_update.sql`

**Example Query:**
Modifying existing records in the customers, products, and sales tables.


```sql
-- Updating the email of a customer
UPDATE customers 
SET email = 'john.d.new@example.com' 
WHERE customer_id = 1;

-- Updating the price of a product
UPDATE products 
SET price = 750.00 
WHERE product_id = 2;

-- Updating the quantity and total_amount of a sale
UPDATE sales 
SET quantity = 3, total_amount = 2400.00 
WHERE sale_id = 2;
```

### 3. DELETE
**File:** `3_delete.sql`

**Example Queries:**
Removing records from the customers, products, and sales tables.

```sql
-- Deleting a customer from the customers table
DELETE FROM customers 
WHERE customer_id = 3;

-- Deleting a product from the products table
DELETE FROM products 
WHERE product_id = 3;

-- Deleting a sale from the sales table
DELETE FROM sales 
WHERE sale_id = 1;
```


### 3. UPSERT (MERGE)
**File:** `4_upsert.sql`

**Example Queries:**
Combining insert and update operations using the INSERT ... ON DUPLICATE KEY UPDATE syntax.


```sql
-- Adding a new customer or updating an existing one
INSERT INTO customers (customer_id, first_name, last_name, email, phone_number) 
VALUES (1, 'John', 'Doe', 'john.d.new@example.com', '555-1234') 
ON DUPLICATE KEY UPDATE 
first_name = VALUES(first_name), 
last_name = VALUES(last_name), 
email = VALUES(email), 
phone_number = VALUES(phone_number);

-- Adding a new product or updating an existing one
INSERT INTO products (product_id, product_name, category, price) 
VALUES (3, 'Tablet', 'Electronics', 350.00) 
ON DUPLICATE KEY UPDATE 
product_name = VALUES(product_name), 
category = VALUES(category), 
price = VALUES(price);
```

### How to Use
To run these SQL queries, ensure that you have access to a SQL database containing the necessary tables (customers, products, and sales) with appropriate data. Simply copy and paste the queries into your SQL database management tool or client, and execute them to perform the desired data manipulation operations.

### License
This repository is licensed under the MIT License.




