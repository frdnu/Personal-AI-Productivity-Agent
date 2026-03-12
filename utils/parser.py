import re
from datetime import datetime, timedelta


class Parser:
    @staticmethod
    def parse_command(command: str):

        title_match = re.search(r"(?i)remind me to (.*?)(?: at |$)", command)

        priority_match = re.search(
            r"(high|medium|low) priority", command, re.IGNORECASE)

        due_date = Parser.extract_due_date(command)

        return {
            "title": title_match.group(1) if title_match else "Unknown Task",
            "priority": priority_match.group(1) if priority_match else "medium",
            "due_date": due_date
        }

    @staticmethod
    def extract_due_date(command: str):
        match = re.search(r"due (today|tomorrow)", command, re.IGNORECASE)

        if match:
            keyword = match.group(1).lower()
            if keyword == "tomorrow":
                date = datetime.now() + timedelta(days=1)
                return date.strftime("%Y-%m-%d")

        return None
