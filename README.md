# Database-Interaction-with-Text-Menus---Python---SQLITE3-
Python 2.7 interacting with a database using text menus instead of SQL statements. 



This was a an exercise to learn how to use SQLITE3 with Python, but then I ended up adding menus and menus and before you knew it, this was a cool little way to add/delete tables and records to a database!



Things to know:

1. I've included my 'smiplsons.db' file for you to play with. During extensive learning, I've made a lot of dumb stuff in there, including most of the data in a table named 'fart'...sorry. 

2. You need to put the database name in the connect function at the top of the code. It has the 'simpsons.db' file now. HOWEVER, I was surprised that when I used a different .db file, everything seemed to work! So if you have a .db file laying around, i'd be curious how well this interfaces with it. 

3. There is a table named 'sqlite_sequence' that cannot be deleted and I even made an exception handle. However, if you try to add/delete record from it, that's not handled. FYI. 

4. If you want to create a new .db file, just put the name of the desired file in the top. Python creates the .db file if it doesn't exist. 
