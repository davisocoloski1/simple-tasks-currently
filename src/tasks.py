import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class TaskManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def get_time(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")

    def add_task(self, task, status):
        self.cur.execute("INSERT INTO simple_tasks (to_do, status, entry_time) VALUES (%s, %s, %s)", (task, status, self.get_time()))
        
        self.conn.commit()

    def list_tasks(self):
        self.cur.execute("SELECT * FROM simple_tasks ORDER BY id")
        return self.cur.fetchall()
        
    def change_task_status(self, task_id, status):
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
        return f"Status updated successfully"
    
    def task_exists(self, task_id):
        self.cur.execute("SELECT 1 FROM simple_tasks WHERE id = %s", (task_id,))
        return self.cur.fetchone() is not None
            
    def delete_task(self, task_id):
        self.cur.execute("DELETE FROM simple_tasks WHERE id = %s", (task_id,))
        self.conn.commit()

    def reset(self):
        self.cur.execute("SELECT COUNT(*) FROM simple_tasks")
        count = self.cur.fetchone()[0]

        if count == 0:
            self.cur.execute("ALTER SEQUENCE simple_tasks_id_seq RESTART WITH 1")
            self.conn.commit()
        else: pass