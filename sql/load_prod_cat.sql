TRUNCATE ProductCategories;

load data
INFILE '/var/lib/mysql-files/prod_categories.csv'
into table sqllab.ProductCategories
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(prodcat_id, category_name);