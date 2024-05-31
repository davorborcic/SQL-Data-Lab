# Sqllab
Environment and the set of utilities for querying, analyzing and cleaning the data
The details abut this project are available in [Build SQL Data Platform](https://medium.com/p/b87426c58ae3) on Medium.  


By installing and using this solution you are acknowledging that you have read and agreed with [licensing terms](LICENSE). If you do not agree, you are forbidden to use this code.   

## Installation Instructions
1. Install Docker and verify it works
2. Load and start MySQL Docker container, create sqllab user and sqllab database (see the article)
3. Create 4 tables in the customer sales model
4. Create .env file from env_template.env in the same directory as code files and replace placeholders with proper credentials and values for MySQL database
4. Execute faker_test.py to create test data, or use Mockaroo to create data sets and then load them
5. Connect via Jupyter or other tools to connect with Pandas, or directly as SQL

## Directories
 

| Directory       | Description                                       | 
|-----------------|:--------------------------------------------------|
| sql             | SQL scripts (table creation, user creation, etc.) |
| data            | data files                                        |

| File                     | Description                                              |
|--------------------------|----------------------------------------------------------|
| .env_template            | template for .env file creation (used for dotenv module) |
| requirements.txt         | Libraries required for the solution                      | 
| initialize_containers.sh | Load and start MySQL Docker container                    |
| retrieval_demo.py        | Showcase data retrieval options (pandas vs. native SQL)  |
| faker_demo.py            | Generate mock data and load into the database            |
| mock_demo.py             | Using inherited class to simulate product categories     |
| test_faker_test.py       | Unit test file                                           | 
| build_tables.sql         | Build 4 tables in customer sales data model              |
| user_setup.sql           | Create a sqllab database user and the database           |
| load_prod_cat.sql        | Load product categories                                  |
| README.md                | This file                                                |
| LICENSE                  | License file                                             |


### Prerequisites
- Installed Python (virtual environment) and required modules (see requirements.txt file) 

The code has been developed on MacOS. It can be ported easily to other Linux, or Windows. 


