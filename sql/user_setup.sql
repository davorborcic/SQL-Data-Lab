CREATE USER sqllab IDENTIFIED BY 'secretpassword';
GRANT ALL PRIVILEGES ON *.* TO 'sqllab'@'%' WITH GRANT OPTION;
flush privileges;
create database sqllab;

