# MySQL advanced

## Learning Objectives

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Tasks

### Task 0. We are all unique!

Write a SQL script that creates a table users following these requirements:

- With these attributes:
  - id, integer, never null, auto increment and primary key
  - email, string (255 characters), never null and unique
  - name, string (255 characters)
- If the table already exists, your script should not fail
- Your script can be executed on any database

Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application

### Task 1. In and not out

Write a SQL script that creates a table users following these requirements:

- With these attributes:
  - id, integer, never null, auto increment and primary key
  - email, string (255 characters), never null and unique
  - name, string (255 characters)
  - country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
- If the table already exists, your script should not fail
- Your script can be executed on any database
