-- Example: Adding a new column "salary" to the "employees" table
ALTER TABLE employees
    ADD salary DECIMAL(10, 2);

-- Example: Dropping the column "hire_date" from the "employees" table
ALTER TABLE employees
    DROP COLUMN hire_date;
