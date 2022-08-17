# Change Data Capture
Change Data Capture (CDC) allows users to insert, update, and delete records in a database. It also notifies users that a change has occured. 

This exercise uses CDC to
- Manage change propogation in various database formats, including RDBMS, Document, Key-value, and distributed-decentralized databases. 
- This will be automated via shell comands, custom scripts, containers, database initilizing, and creating an event loop

## We'll walk through the lesson accordingly: 
1. A walk through on how to incorporate shell commands in a python script followed by adapting these scripts for automating the creation and deletion of containers within terminal. 
2. Database initilation - many DBs, such as redis and mongo, do not require the DB to be initilized. However, Cassandra and MySQL do. 
3. database changes - this exercise uses a (script)[timer.py] to simulate periodic changes



# What Is Change Data Capture (CDC)?

CDC refers to all of the techniques used to identify and capture changes needed in a database. This process is fundamental as data often changes at a high speed, and this may cause your database to change or grow. Therefore, being able to address these changes in an effective way is important to ensure that your code, application, and software work in an efficient way.

By using CDC, organizations are able to identify and integrate the changes in a database more quickly and with fewer resources. In other words, CDC reduces both the time required to analyze data and the cost of resources.

# Change Data Capture Methods

Naturally, there are a few different methods by which CDC can be implemented depending on your application requirements. This mini-lesson provides an overview of the two most common methods along with their advantages and disadvantages.

## Audit Columns

Audit columns are one of the most common CDC techniques. This method is implemented by adding a column called Last_changed to your dataset to create your own change data capture solution at the application level. This technique will only affect the rows in your dataset that were changed after the last change occurred.

This technique can be implemented with the following steps. Suppose that your original database has a column titled `Created_time`. To implement CDC using the audit columns technique, you would complete the following steps:

1. Add a column titled Changed_time to your original table.
2. Get the maximum value of both the target tables’ Created_time and Changed_time columns.
3. Select all the rows from the original table with a Created_Time greater than the final table’s maximum Created_Time.
4. Select all rows from the original table that have an Updated_Time greater than the final table’s maximum Updated_Time, but less than its maximum Created_Time.
5. Insert new rows from the third step or modify existing rows from the fourth step in the final table.

The advantage of this method is that it’s easy to implement using simple queries. The main disadvantage is that it’s easy to make errors that can cause inconsistencies in your data by using this technique.

## Table Deltas

Table deltas are one of the easiest techniques to implement CDC.

Suppose you have the following table:

| Customer_ID | Last_Purchase |

|------------|-------------| 
| 1 | 03-13-2021 |
| 2 | 05-07-2021 |
| 3 | 10-24-2021 |

Then suppose that the customer with an ID equal to 1 makes a new purchase on 10-31-2021 and that a new customer, with an ID equal to 4, makes their first purchase on 11-02-2021.

Using table deltas, the new table will be:

| Customer_ID | Last_Purchase |
|-----------|------------|
| 1 | 10-31-2021 |
| 2 | 05-07-2021 |
| 3 | 10-24-2021 |
| 4 | 11-02-2021 |

The advantage of this approach is that it provides an accurate view of the changed data using simple queries. The disadvantage of this approach pertains mainly to memory. The demand for data storage increases because you need three copies of the data sources that are being used in this technique: the original data, the previous snapshot, and the current snapshot.