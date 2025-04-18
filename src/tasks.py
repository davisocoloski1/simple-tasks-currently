import psycopg2
from dotenv import load_dotenv
import os

load_dotenv() #Parse a .env file and then load all the variables found as environment variables.

class TaskManager:
    def __init__(self):
        """When the class is called it connect to the database"""
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        
        self.cur = self.conn.cursor()

    def close(self):
        """When executed, ends the connection with the database"""
        self.cur.close()
        self.conn.close()

    def get_time(self):
        """Returns the system time in hours:minutes:seconds"""
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")

    def add_task(self, task, status):
        """ Insert the values given by user in the method parameters into the table.

            Should insert 3 values, but there's only 2 parameters. 
            This is because the 3rd value is given by the method get_time(), 
            which return the system time. """

        self.cur.execute("INSERT INTO simple_tasks (to_do, status, entry_time) VALUES (%s, %s, %s)", (task, status, self.get_time()))
        
        self.conn.commit()

    def list_tasks(self):
        """Access all items from the table and returns it"""

        self.cur.execute("SELECT * FROM simple_tasks ORDER BY id")
        return self.cur.fetchall()
        
    def change_task_status(self, task_id, status):
        """
            self.cur.execute("SELECT status FROM simple_tasks WHERE ID = %s", (task_id,))
            stat = self.cur.fetchone()
            This command access the column status with the id given by user

            If the status do not exist, returns 'Task not found' else, access it.
            If the status given by the user is the same as in the table, returns 'Same status'
            If the status given by user is not 'Active', 'Inactive' or 'Completed', returns 'Invalid status'

            self.cur.execute("UPDATE simple_tasks SET status = %s WHERE id = %s", (status, task_id))
            self.conn.commit()
            This command access the current status and change it for the status given by the user

            Returns 'Status updated successfully'
        """

        self.cur.execute("SELECT status FROM simple_tasks WHERE ID = %s", (task_id,))
        stat = self.cur.fetchone()

        if not stat:
            return "Task not found."
        
        current_status = stat[0]

        if current_status == status:
            return "Same status."
        
        if status not in ['Active'.lower(), 'Inactive'.lower(), 'Completed'.lower()]:
            return "Invalid status."
        
        self.cur.execute("UPDATE simple_tasks SET status = %s WHERE id = %s", (status, task_id))
        self.conn.commit()
        return "Status updated successfully"
    
    def task_exists(self, task_id):
        """
            Search, in the table, the id given by the user
            This method is a confirmation that the id/tasks exists
        """

        self.cur.execute("SELECT 1 FROM simple_tasks WHERE id = %s", (task_id,))
        return self.cur.fetchone() is not None
            
    def delete_task(self, task_id):
        """
            Deletes the task from the table, using the id given by user
        """

        self.cur.execute("DELETE FROM simple_tasks WHERE id = %s", (task_id,))
        self.conn.commit()

    def reset(self):
        """
            This method resets the table ids if it is empty.
        """

        self.cur.execute("SELECT COUNT(*) FROM simple_tasks")
        count = self.cur.fetchone()[0]

        if count == 0:
            self.cur.execute("ALTER SEQUENCE simple_tasks_id_seq RESTART WITH 1")
            self.conn.commit()
        else: pass