import sqlite3
import sys

class Database_Engine():
    '''
        Class is responsible for initialising a database, configuring (Settings), and closing

        Params:
            -> db_path = path to database (.db) file - String
            -> debug_mode = "True" (Virtual) / "False" (Live) - String
    '''

    # Placeholders for connection + cursor variables
    conn = None
    c = None

    def __init__(self, db_path=None, debug_mode=True):

        try:
            self.conn = self.connect(db_path=db_path, debug_mode=debug_mode)
            self.c = self.conn.cursor()
        except:
            print(f"Incorrect datapase path specified: {db_path}")
            sys.exit(0)

    def connect(self, db_path, debug_mode):
        '''Connects to database. Actual or virtual depending on debug value'''

        if debug_mode:
            conn = sqlite3.connect(':memory:')  # Stores the db in memory so always fresh and always resets after use
        else:
            conn =  sqlite3.connect(db_path)

        self.configure_connection(conn)

        return conn

    def configure_connection(self, conn):
        '''Method for configuring the connection (Add new settings here)'''

        # Enables foreign key settings
        conn.execute('pragma foreign_keys=ON')

    def close_connection(self):
        ''' Closes the connection to the active database '''

        self.conn.close()
