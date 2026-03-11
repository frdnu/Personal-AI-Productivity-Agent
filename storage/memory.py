import sqlite3


class MemoryManager:

    def __init__(self, db_path="data/tasks.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
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

        conn.commit()
        conn.close()

    def add_task(self, task):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks (title, description, priority, status, due_date, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            task.title,
            task.description,
            task.priority,
            task.status,
            str(task.due_date),
            str(task.created_at)
        ))

        conn.commit()
        conn.close()
