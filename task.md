# FastAPI with GraphQL and PostgreSQL Assessment

## In the Repo:
A FastAPI application has been initialized with standard boilerplate code for postgresSQL connection using SQLAlchemy and a GraphQL endpoint `/graphql` using Strawberry has been created.

## Pre-Requisites:
- Postgres Server (running locally)
- Python 3.10

## Tasks:
1. Add a PostgreSQL database and create a simple table named "users" with the fields: id (integer), name (string), email (string), and date_registered (date).
2. Add code to define the SQLAlchemy User Model 
3. Add the following operations to the endpoint:
   - Query all users
   - Query a user by their ID
   - Mutation to add a new user

### Implement the following functionalities:
- All user data returned from queries should be in lowercase.
- The `date_registered` field should return the number of days since the user was registered.

### Write tests for your GraphQL endpoint using a tool such as pytest. Make sure to test the following:
- Adding a new user
- Querying a user by their ID
- Querying all users

## Deliverables:
- A repository on Github containing the FastAPI application.
- A README file explaining how to run the application and tests.
- The code for the FastAPI application, the GraphQL endpoint, the PostgreSQL integration, and the tests.

## Evaluation Criteria:
- Correct implementation of the FastAPI application and the ability to integrate with PostgreSQL.
- Correct implementation of GraphQL queries and mutations.
- Proper testing of the GraphQL endpoint.
- Code readability, structure, and commenting.
