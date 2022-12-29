from task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        for i in range(len(self.tasks)):
            if task_name == self.tasks[i].name:
                self.tasks[i].completed = True
                self.completed_tasks.append(task_name)
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        a = len(self.completed_tasks)
        self.completed_tasks.clear()
        return f"Cleared {a} tasks."


    def view_section(self):
        result = [f'Section {self.name}:']
        separator = "\n"

        for el in self.tasks:
            result.append(Task.details(el))

        return f"{separator.join(result)}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 78/100
# 100/100 ot nishtoto shoto judge e adekvaten
