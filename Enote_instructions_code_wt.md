**Instructions:**

1) Pip install the requirements.txt( $ pip install -r requirements.txt)
2) Run the .py file using "python Assignment_Enote_Ajith.py"

**Code walk through:**

The samples files are pushed to Sqlite database using Python.

For connecting to Sqlite database and pushing data to the same, I have imported sqlite3 library and pandas library both.Using the **connect** function in Sqlite3 library, established  a connection between Python and database.Using the cursor object and its execute method executed SQL commands to create the tables on the database.

Using Pandas.read_csv(), read the csv files and loaded into the staging tables which are created in the earlier step. This staging tables are created for future purposes and performing any required transformations on the data.In the next step I have created the main tables and pushed the inserted the data from the staging tables to main tables.

The last statement is the actual step to get the required result.



