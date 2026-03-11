from task import Task

task1 = Task(
    title="Study Operating Systems",
    description="Prepare for midterm",
    due_date="2026-03-01",
    priority="high",
)

task2 = Task("Clean desk")

print(task1)
print(task2)

task1.mark_done()
print(task1)

print("Is task1 overdue?", task1.is_overDue())
