flogo
BE Module 13 Lesson 2: Assignment

1 question left!
BE Module 13 Lesson 2: Assignment
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

Implementing Pagination in the Factory Management System
Objective: The objective of this assignment is to enhance the factory management system by implementing pagination for retrieving orders and products efficiently using Flask.

Problem Statement: You are tasked with extending the factory management system to support pagination for retrieving orders and products. Pagination allows for fetching large datasets in smaller, manageable chunks, improving system performance and user experience.

Task 1: Implement Pagination for Orders

Modify the existing endpoint /orders to support pagination by adding query parameters for page and per_page.
Implement pagination logic in the backend to retrieve orders in batches based on the provided parameters.
Task 2: Implement Pagination for Products

Update the /products endpoint to incorporate pagination functionality similar to the orders endpoint.
Adjust the backend logic to fetch products in paginated form based on the specified parameters.
Task 3: Test Pagination Endpoints

Test the pagination endpoints /orders and /products using various combinations of page and per_page parameters.
Verify that the endpoints return the expected results and handle edge cases such as out-of-range page numbers gracefully.
Expected Outcomes:

Upon completing this assignment, students should achieve the following outcomes:

Implementation of pagination functionality for retrieving orders and products, improving system performance and user experience.
Integration of pagination logic into the existing factory management system, ensuring seamless interaction with large datasets.
Successful testing of pagination endpoints to validate correct functionality and handle edge cases effectively.

Advanced Querying in Factory Management System with SQLAlchemy
Objective: The objective of this assignment is to practice performing complex queries using SQLAlchemy in a factory management system. This includes utilizing Group By, Having, Joins, and Subqueries to extract meaningful insights and data from the database.

Problem Statement: You are tasked with implementing advanced querying operations in the factory management system to analyze employee performance, track production efficiency, and gain insights into customer behavior. This involves executing queries that involve grouping, filtering, joining multiple tables, and using subqueries to extract relevant information from the database.

Task 1: Analyze Employee Performance

Write a query to calculate the total quantity of products each employee has produced.
Group the results by employee name.
Use the Group By clause to group the data and the Sum function to calculate the total quantity.
Task 2: Identify Top Selling Products

Write a query to find the top-selling products based on the total quantity ordered.
Group the results by product name.
Use the Group By clause to group the data, the Sum function to calculate the total quantity ordered for each product, and the Order By clause to sort the results in descending order of quantity.
Task 3: Determine Customer Lifetime Value

Write a query to calculate the total value of orders placed by each customer.
Group the results by customer name.
Use the Group By clause to group the data and the Sum function to calculate the total order value.
Filter out customers with a total order value less than a certain threshold using the Having clause.
Task 4: Evaluate Production Efficiency

Write a query to calculate the total quantity produced for each product on a specific date.
Join the Production and Product tables on the product_id column.
Use a subquery to filter the production records for the specified date.
Group the results by product name.
Expected Outcomes:

Upon completing this assignment, students should achieve the following outcomes:

Proficiency in writing complex queries using SQLAlchemy to analyze various aspects of the factory management system.
Ability to utilize Group By, Having, Joins, and Subqueries to extract meaningful insights and data from the database.
Understanding of how to perform advanced querying operations to evaluate employee performance, track production efficiency, identify top-selling products, and determine customer lifetime value.
