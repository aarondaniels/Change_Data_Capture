# Change Data Capture
Change Data Capture (CDC) allows users to insert, update, and delete records in a database. It also notifies users that a change has occured. 

This exercise uses CDC to
- Manage change propogation in various database formats, including RDBMS, Document, Key-value, and distributed-decentralized databases. 
- This will be automated via shell comands, custom scripts, containers, database initilizing, and creating an event loop

Ultimately, this is an exercise in how CDC works and some of the mechanics. There are formal CDC tools that are better suited for scalable applications. For this repo, I focus on doing CDC by hand in order to build a greater understanding of the mechanics and fundamentals. 


## The instruction will progress as follows: 
1. A walk through on how to incorporate shell commands in a python script followed by adapting these scripts for automating the creation and deletion of containers within terminal. 
2. Database initilation - many DBs, such as Redis and Mongo, do not require the DB to be initilized. However, Cassandra and MySQL do. [This](https://github.com/aarondaniels/Change_Data_Capture/blob/main/Automate/create.py) code details how databases are initilized in containers. 
3. database changes - this exercise uses a (script)[timer.py] to simulate periodic changes. Additional instruction on time loops is captured [here](Time_loops.md)
4. Finally, the full CDC application will be developed using MySQL, MongoDB, Redis, and Cassandra
    - Mongo and Redis require less set up and configuration, as detailed [here](https://github.com/aarondaniels/Change_Data_Capture/blob/main/CDC/mongodb.py) and [here](https://github.com/aarondaniels/Change_Data_Capture/blob/main/CDC/redisdb.py), respectively.
    - Create files for the scheduler, containers, and the db's

## How to execute the CDC app? 
1. ***Create and initialize databse***: From the terminal, navigate to the file location of [the CDC app](https://github.com/aarondaniels/Change_Data_Capture/tree/main/CDC) and execute `python3 containers.py -create` (in order to create the containers. In case of deleting the containers, a similar command is executed, `python3 containers.py -delete`). Finally, initialize the MySQL and Cassandra database' by executing `python3 containers.py -init`
2. Run the scheduler by executing `python3 scheduler.py` to initate main loop to populate MySQL. Those DB changes will be detected and pushed into MongoDB, Redis, and Cassandra DB's. Confirmations should be displayed in the console. 



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
| ***1*** | ***10-31-2021*** |
| 2 | 05-07-2021 |
| 3 | 10-24-2021 |
| ***4*** | ***11-02-2021*** |

The advantage of this approach is that it provides an accurate view of the changed data using simple queries. The disadvantage of this approach pertains mainly to memory. The demand for data storage increases because you need three copies of the data sources that are being used in this technique: the original data, the previous snapshot, and the current snapshot.