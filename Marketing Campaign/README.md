# Data Exploration:

* Loading the dataset. 
* Take a look at the first few rows of the dataset to understand its structure and column names.
* Check for missing values in each column and handle them appropriately (e.g., by imputation or removal). The reason why the second code snippet gave you the correct columns while specifying sep='\t' (tab) and index_col='ID' (setting the 'ID' column as the index) is likely because the CSV file uses a tab character (\t) as the delimiter instead of a comma (,), and the first code snippet did not specify any delimiter.

There are two columns that are not mentioned in dataset decription: Z_CostCount and Z_Revenue. Because there are only 1 values in these columns, I will delete the columns.



