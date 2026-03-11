from datetime import datetime, date


class Task:
    VALID_PRIORITIES = {"low", "medium", "high"}
    VALID_STATUSES = {"pending", "done"}

    def __init__(
            self,
            title: str,
            description: str = "",
            due_date: str | date | None = None,
            priority="medium"
    ):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty!")
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(
                f"Priority must be one of {self.VALID_PRIORITIES}!")

        self.title = title.strip()
        self.description = description.strip()
        self.priority = priority
        self.status = "pending"
        self.created_at = datetime.now()
        self.due_date = self._parse_due_date(due_date)

    def _parse_due_date(self, due_date: str | None) -> date | None:
        if due_date is None:
            return None

        try:
            return datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Due date should be in YYYY-MM-DD format")

    def mark_done(self):
        self.status = "done"

    def is_overDue(self) -> bool:
        if self.due_date is None:
            return False
        elif self.due_date < date.today() and self.status == "pending":
            return True

    def __repr__(self):
        return (
            f"Task(title={self.title!r}, priority={self.priority!r}, "
            f"status={self.status!r}, due_date={self.due_date})"
        )

    def __str__(self):
        due = self.due_date if self.due_date else "No due date"
        return f"[{self.status.upper()}] {self.title} | Priority: {self.priority} | Due: {due}"
