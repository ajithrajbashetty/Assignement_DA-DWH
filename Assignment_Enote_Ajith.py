import sqlite3

import pandas as pd

c=sqlite3.connect("ENOTE_assignment_DWH")

conn = sqlite3.connect("ENOTE_assignment_DWH")  

c = conn.cursor()

 

c.execute("CREATE TABLE Accounts_stg(id_account VARCHAR(100)   ,id_person VARCHAR(100),account_type VARCHAR(100));")

c.execute("CREATE TABLE Customer_stg (id_person INTEGER PRIMARY KEY  ,name VARCHAR (100)  , surname VARCHAR (100)  ,zip INTEGER,city VARCHAR (100),country  VARCHAR (100) ,email VARCHAR (100)  ,phone_number INTEGER,birth_date DATE);")

c.execute("CREATE TABLE Transactions_stg(id_transaction VARCHAR(100),id_account VARCHAR(100)  , transaction_type VARCHAR (100)  ,transaction_date DATE  ,transaction_amount VARCHAR(100));")

table1= pd.read_csv(r'C:\Users\AJITH_RAJ_BASHETTY\Desktop\Data_Analyst_assignment_enote\BI_assignment_person.csv',skip_blank_lines=True)

table1.to_sql('Customers_stg', conn, if_exists='append', index = False)  

table2 = pd.read_csv(r'C:\Users\AJITH_RAJ_BASHETTY\Desktop\Data_Analyst_assignment_enote\BI_assignment_account.csv',)

table2.to_sql('Accounts_stg', conn, if_exists='append', index = False) 

table3 = pd.read_csv (r'C:\Users\AJITH_RAJ_BASHETTY\Desktop\Data_Analyst_assignment_enote\BI_assignment_transaction.csv')

table3.to_sql('Transactions_stg', conn, if_exists='append', index = False)  

c.execute("CREATE TABLE Customer_main (id_person INTEGER PRIMARY KEY  ,name VARCHAR (100)  , surname VARCHAR (100)  ,zip INTEGER,city VARCHAR (100),country  VARCHAR (100)  ,email VARCHAR (100)  ,phone_number INTEGER,birth_date DATE  );")

c.execute("CREATE TABLE Accounts_main  ( id_account INTEGER PRIMARY KEY ,id_person INTEGER NOT NULL REFERENCES Customer(id_person),account_type VARCHAR(20) NOT NULL);")

c.execute("CREATE TABLE Transactions_main (id_transaction INTEGER NOT NULL ,id_account INTEGER NOT NULL REFERENCES Accounts(id_account), transaction_type VARCHAR (10)  NOT NULL,transaction_date DATE,transaction_amount DECIMAL(10,6) NOT NULL);")



c.executescript("""
insert into Customer_main   select * from Customers_stg;
insert into Accounts_main select * from Accounts_stg ;
insert into Transactions_main select * from Transactions_stg ;
""")
 




for i in c.execute("""select 
 AC.id_person,
 strftime('%m',T.transaction_date) ||'.'|| strftime('%Y',T.transaction_date) AS MONTH,
 sum(T.transaction_amount)     
 from Transactions_main  T   INNER JOIN    
 (select A.id_account,A.id_person from Accounts_main A INNER JOIN 
  Customer_main C on A.id_person= CAST(C.id_person AS INTEGER)
  WHERE A.id_person in (345,1234)) AC on cast(T.id_account as INTEGER) = AC.id_account  
  AND  T.transaction_date BETWEEN '2020-02-15' AND  '2020-06-07'  
 GROUP BY strftime('%m',T.transaction_date),AC.id_person
 order by AC.id_person DESC;
 """):
        print(i)

