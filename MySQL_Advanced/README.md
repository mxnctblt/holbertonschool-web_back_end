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

### Task 2. Best band ever!

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:

- Import this table dump: metal_bands.sql.zip
- Column names must be: origin and nb_fans
- Your script can be executed on any database

### Task 3. Old school band

Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

Requirements:

- Import this table dump: metal_bands.sql.zip
- Column names must be: band_name and lifespan (in years)
- You should use attributes formed and split for computing the lifespan
- Your script can be executed on any database

### Task 4. Buy buy buy

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table items can be negative.

Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

### Task 5. Email validation to sent

Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

### Task 6. Add bonus

Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:

- Procedure AddBonus is taking 3 inputs (in this order):
  - user_id, a users.id value (you can assume user_id is linked to an existing users)
  - project_name, a new or already exists projects - if no projects.name found in the table, you should create it
  - score, the score value for the correction

Context: Write code in SQL is a nice level up!

### Task 7. Average score

Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

Requirements:

- Procedure ComputeAverageScoreForUser is taking 1 input:
  - user_id, a users.id value (you can assume user_id is linked to an existing users)
