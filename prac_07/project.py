import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def update(self, new_completion_percentage=None, new_priority=None):
        if new_completion_percentage is not None:
            self.completion_percentage = new_completion_percentage
        if new_priority is not None:
            self.priority = new_priority

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"





