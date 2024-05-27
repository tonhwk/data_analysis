-- Adding foreign key constraint to the "sales" table referencing the "customers" table
ALTER TABLE sales
    ADD CONSTRAINT fk_sales_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- Adding foreign key constraint to the "sales" table referencing the "products" table
ALTER TABLE sales
    ADD CONSTRAINT fk_sales_product_id FOREIGN KEY (product_id) REFERENCES products(product_id);