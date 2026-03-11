import sqlite3
from classes.task import Task


class MemoryManager:
    def __init__(self, db_path="data/tasks.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    priority TEXT,
                    status TEXT,
                    due_date TEXT,
                    created_at TEXT
                )
            """)

    def add_task(self, task: Task):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO tasks (title, description, priority, status, due_date, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                task.title,
                task.description,
                task.priority,
                task.status,
                str(task.due_date) if task.due_date else None,
                task.created_at.strftime("%Y-%m-%d %H:%M:%S")
            ))

    def get_tasks(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT title, description, due_date, priority, status FROM tasks")
            rows = cursor.fetchall()

            task_objects = []
            for row in rows:
                t = Task(
                    title=row[0],
                    description=row[1],
                    due_date=row[2],
                    priority=row[3]
                )
                t.status = row[4]
                task_objects.append(t)

            return task_objects

    def reset_database(self):
        """Temp function that Wipes all tasks from the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM tasks")
        print("🧹 Database has been reset!")
