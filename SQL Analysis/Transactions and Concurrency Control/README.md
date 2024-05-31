# Transactions and Concurrency Control

## Project Overview
This repository contains SQL queries demonstrating essential techniques for managing transactions and implementing concurrency control in a database system. It includes examples of transaction management, setting isolation levels, and handling concurrency issues.


## File Descriptions

### 1. Transactions
**File:** `1_transactions.sql`

**Example Query:**
Managing transactions for maintaining data integrity.


```sql
START TRANSACTION;

-- Insert a new sale
INSERT INTO sales (customer_id, product_id, sale_date, quantity, total_amount) 
VALUES (1, 2, '2024-05-30', 1, 800.00);

-- Update the product quantity (assuming there's a field for stock, which we haven't defined yet)
UPDATE products 
SET stock = stock - 1 
WHERE product_id = 2;

COMMIT;
```

### 2. Concurrency
**File:**  `2_concurrency.sql`

**Example Query:**
Setting isolation levels to control the visibility of data changes during transactions.

```sql
-- Set the isolation level to Repeatable Read
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

START TRANSACTION;

-- Select product details
SELECT * FROM products WHERE product_id = 2;

-- Simulate a delay to allow concurrent transaction to occur
SLEEP(5);

-- Check product details again
SELECT * FROM products WHERE product_id = 2;

COMMIT;

```

### 3. Concurrent Transaction
**File:** `3_concurrent_transactions.sql`

**Example Queries:**
Implementing concurrency control mechanisms to prevent data inconsistency during concurrent transactions.

```sql
-- Transaction 1
START TRANSACTION;

-- Check stock availability
SELECT stock FROM products WHERE product_id = 2 FOR UPDATE;

-- Simulate processing time
SLEEP(5);

-- Update stock if available
UPDATE products 
SET stock = stock - 1 
WHERE product_id = 2 AND stock > 0;

-- Commit transaction
COMMIT;

-- Transaction 2 (similar steps)
START TRANSACTION;

-- Check stock availability
SELECT stock FROM products WHERE product_id = 2 FOR UPDATE;

-- Simulate processing time
SLEEP(5);

-- Update stock if available
UPDATE products 
SET stock = stock - 1 
WHERE product_id = 2 AND stock > 0;

-- Commit transaction
COMMIT;


```


### How to Use
To run these SQL queries, ensure that you have access to a SQL database containing the necessary tables (sales and products) with appropriate data. Simply copy and paste the queries into your SQL database management tool or client, and execute them to perform transaction management, set isolation levels, and implement concurrency control.

### License
This repository is licensed under the MIT License - see the LICENSE file for details.

### Contact
For any questions or feedback, please contact Antonio Martinez at andresreg93@gmail.com.





