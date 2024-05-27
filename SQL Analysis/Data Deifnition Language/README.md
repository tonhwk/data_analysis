# Data Definition Language (DDL) 

## Project Overview
This repository contains SQL queries demonstrating essential Data Definition Language (DDL) techniques. These queries showcase skills in SQL for defining and modifying database structures, including creating and altering tables, adding and dropping columns, and implementing constraints.


## File Descriptions

### 1. CREATE TABLE
**File:** `1_create_table.sql`

**Example Query:**
This file contains queries for creating tables in the database.

```sql
-- Example: Creating a new table called "employees"
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    hire_date DATE
);

```
### 2.  ALTER TABLE
**File:**  `2_alter_table.sql`

**Example Query:**
This file contains queries for altering existing tables in the database.

```sql
-- Example: Adding a new column "salary" to the "employees" table
ALTER TABLE employees
    ADD salary DECIMAL(10, 2);

-- Example: Dropping the column "hire_date" from the "employees" table
ALTER TABLE employees
    DROP COLUMN hire_date;

```

### 3. DROP TABLE
**File:** `3_drop_table.sql`

**Example Queries:**
This file contains queries for dropping tables from the database.
```sql
-- Example: Dropping the "employees" table
DROP TABLE employees;

```


### 3. Constraints
**File:** `4_constraints.sql`

**Example Queries:**
This file contains queries for implementing constraints such as primary keys, foreign keys, unique constraints, and check constraints.
```sql
-- Adding foreign key constraint to the "sales" table referencing the "customers" table
ALTER TABLE sales
    ADD CONSTRAINT fk_sales_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- Adding foreign key constraint to the "sales" table referencing the "products" table
ALTER TABLE sales
    ADD CONSTRAINT fk_sales_product_id FOREIGN KEY (product_id) REFERENCES products(product_id);

```

### How to Use
To execute these SQL queries, ensure that you have access to a SQL database containing the necessary tables. Copy and paste the queries into your SQL database management tool or client, and execute them to perform the desired Data Definition Language (DDL) operations.

### License
This repository is licensed under the MIT License.




