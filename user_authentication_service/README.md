# User authentication service

## Learning Objectives

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Tasks

### Task 0. User model

In this task you will create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy).

The model will have the following attributes:

- id, the integer primary key
- email, a non-nullable string
- hashed_password, a non-nullable string
- session_id, a nullable string
- reset_token, a nullable string
