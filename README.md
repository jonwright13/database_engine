# database_engine

A Python class object that contains some helpful methods for initialising an sql database, whether it be virtual or live

## Requirements

This only requires sqlite3

## How To Use

First, initialise the class: `DB = Database_Engine(database_path, debug_mode)`
* Where database_path is the relative path to the database including the database name with extension (String)
* And debug_mode is True / False (Boolean), which refers to creating the database in a live file or as a virtual database -> True for virtual and False for live
The class object will create the connection and the cursor object, which are stored as class attributes, before configuring the connection (This can be modified as needed)

The database engine can be used freely from here.

Lastly, use the `DB.close_connection()` method to close the connection.
