from classes.task import Task
from storage.memory import MemoryManager
from utils.parser import Parser

memory = MemoryManager()

# 1. Simulate user input
user_input = "Remind me to Fix the CSS at high priority due tomorrow"

# 2. Parse the input into a dictionary
data = Parser.parse_command(user_input)

# 3. Create the object dynamically
new_task = Task(
    title=data['title'],
    priority=data['priority'],
    due_date=data['due_date']
)

# 4. Save to database
memory.add_task(new_task)

print(
    f"Added task: {new_task.title} (Priority: {new_task.priority}, Due: {new_task.due_date})")
