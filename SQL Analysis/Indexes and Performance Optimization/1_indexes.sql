-- Adding indexes to the customers table
CREATE INDEX idx_customers_last_name ON customers(last_name);

-- Adding indexes to the products table
CREATE INDEX idx_products_category ON products(category);

-- Adding composite index to the sales table for queries involving both customer_id and sale_date
CREATE INDEX idx_sales_customer_date ON sales(customer_id, sale_date);
