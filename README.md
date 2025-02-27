## Database Connection Project with Python

## Description
This project allows you to establish a connection to a database using Python.
Depending on which database manager you want to use, clone the corresponding folder, 
install the necessary dependencies for your engine and then import the PoolCursor class to start interacting with the database.
Each one consists of two files that handle the connection and the interaction with the database.
You only have to make the methods and SQL queries to be executed.

## Requirements
- Python 3.x
- Library `mysql-connector-python` or `psycopg2` (depending on the database manager used)

## Installation
1. Clone this repository:
2. Install the necessary dependencies:


## Usage
1. Configure the database credentials in the corresponding file.
2. Run the connection script:


## Project Structure
```
/
|--db_connection
|----db_mysql
|------ connection_my.py # Main file to establish the connection to the database
|------ pool_cursor_my.py # File that manages connections from a connection pool
|----db_postgres
|------ connection_pg.py # Main file for establishing connection to database
|------ pool_cursor_pg.py # File that handles connections from a connection pool
|-- README.md # This file
```

## Author
Jose A. Perezlindo

## License
This project is licensed under the [MIT] license.
