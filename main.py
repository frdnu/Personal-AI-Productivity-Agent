from classes.task import Task
from storage.memory import MemoryManager
from utils.parser import Parser

memory = MemoryManager()

user_input = "Remind me to Fix the CSS at high priority due tomorrow"

data = Parser.parse_command(user_input)

new_task = Task(
    title=data['title'],
    priority=data['priority'],
    due_date=data['due_date']
)

memory.add_task(new_task)

print(
    f"Added task: {new_task.title} (Priority: {new_task.priority}, Due: {new_task.due_date})")
