from task import Task
from storage.memory import MemoryManager

memory = MemoryManager()

task1 = Task(
    title="Study Operating Systems",
    description="Prepare for midterm",
    due_date="2026-03-20",
    priority="high"
)

task2 = Task(
    title="Go to gym",
    description="Leg day",
    priority="medium"
)

memory.add_task(task1)
memory.add_task(task2)

tasks = memory.get_tasks()

print("Tasks in database:")
for task in tasks:
    print(task)
