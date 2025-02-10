# Airline Passenger Satisfaction Database Project

## Problem Statement
The objective of this project is to create and manage a comprehensive database for Airline Passenger Satisfaction. The database will store, retrieve, and analyze passenger feedback, flight details, satisfaction ratings, and other relevant data. This will facilitate the analysis of passenger satisfaction factors, help in making data-driven decisions, and support performance assessments for airlines.

## Entity-Relationship Diagram (ERD)
The ER diagram for the airline passenger satisfaction database consists of the following main entities:

- **Passengers:** Stores information about passengers, including demographic details such as age and customer type.
- **Flights:** Contains data about flight details such as flight ID, flight distance, type of travel, and class.
- **Satisfaction Ratings:** Includes the ratings provided by passengers for various aspects of the flight experience like seat comfort, inflight service, etc.
- **Delays:** Records data about delays in flights, including the delay time and the reasons for delays.
- **Overall Satisfaction:** Contains the overall satisfaction score for passengers based on their experience.

The relationships between these entities are clearly outlined in the ERD, with primary keys, foreign keys, and constraints like not-null conditions.

## SQL Execution Steps
To set up the database, follow these steps:

1. **Run the `create.sql` script** to create the tables and relationships for the airline passenger satisfaction database. This script defines the schema and structure of the database.
    
2. **Populate the database** by running the `load.sql` script. This script includes `INSERT` statements to insert data into each table.

3. Ensure that you have a supported Database Management System (DBMS) installed, such as PostgreSQL, and that you have the necessary permissions to create and modify the database.

## Query Execution Comments
Once the database is set up, you can perform queries to retrieve or modify the data as needed. Always back up your data before running operations that can alter or delete records.

For troubleshooting, check the documentation for SQL query guidelines or consult the database administrator.

For example queries, you can retrieve passenger satisfaction ratings by flight, analyze delays, or evaluate overall satisfaction across different passenger types and classes.

### Example Queries
- Retrieve all flights with their corresponding satisfaction ratings.
- Fetch passengers by their customer type (e.g., loyal vs. disloyal).
- Identify the average satisfaction ratings for each flight.

Refer to the documentation for further SQL query examples and guidance.
