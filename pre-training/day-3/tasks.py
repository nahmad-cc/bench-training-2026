import json
import os
from datetime import datetime
import sys

class Task:
    def __init__(self, id, title, status='todo', created_at=None):
        self.id = id
        self.title = title
        self.status = status
        if created_at:
            self.created_at = created_at
        else:
            self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'created_at': self.created_at
        }
    
    def mark_done(self):
        self.status = 'done'


class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for task_data in data:
                        task = Task(
                            task_data['id'],
                            task_data['title'],
                            task_data['status'],
                            task_data['created_at']
                        )
                        self.tasks.append(task)
            except json.JSONDecodeError:
                print("Error: tasks.json is corrupted. Starting fresh.")
                self.tasks = []
    
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, f, indent=2)
    
    def add_task(self, title):
        if not title:
            print("Error: task title cannot be empty")
            return
        
        next_id = 1
        if self.tasks:
            next_id = max(t.id for t in self.tasks) + 1
        
        task = Task(next_id, title)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {title} (ID: {next_id})")
    
    def complete_task(self, task_id):
        try:
            task_id = int(task_id)
        except ValueError:
            print(f"Error: {task_id} is not a valid ID")
            return
        
        for task in self.tasks:
            if task.id == task_id:
                task.mark_done()
                self.save_tasks()
                print(f"Task {task_id} marked as done")
                return
        
        print(f"Error: Task with ID {task_id} not found")
    
    def delete_task(self, task_id):
        try:
            task_id = int(task_id)
        except ValueError:
            print(f"Error: {task_id} is not a valid ID")
            return
        
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print(f"Task {task_id} deleted")
                return
        
        print(f"Error: Task with ID {task_id} not found")
    
    def list_tasks(self, filter_status=None):
        if not self.tasks:
            print("No tasks yet")
            return
        
        print("\nTasks:")
        print("-" * 60)
        
        for task in self.tasks:
            if filter_status and task.status != filter_status:
                continue
            
            status_marker = "✓" if task.status == 'done' else " "
            print(f"[{status_marker}] ID: {task.id} | {task.title} | {task.status} | {task.created_at}")
        
        print("-" * 60)


def main():
    manager = TaskManager()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tasks.py add 'Task title'")
        print("  python tasks.py done <id>")
        print("  python tasks.py delete <id>")
        print("  python tasks.py list")
        print("  python tasks.py list --filter done")
        print("  python tasks.py list --filter todo")
        return
    
    command = sys.argv[1]
    
    if command == 'add':
        if len(sys.argv) < 3:
            print("Error: please provide a task title")
            return
        title = ' '.join(sys.argv[2:])
        manager.add_task(title)
    
    elif command == 'done':
        if len(sys.argv) < 3:
            print("Error: please provide a task ID")
            return
        manager.complete_task(sys.argv[2])
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Error: please provide a task ID")
            return
        manager.delete_task(sys.argv[2])
    
    elif command == 'list':
        filter_status = None
        if len(sys.argv) > 2 and sys.argv[2] == '--filter':
            if len(sys.argv) > 3:
                filter_status = sys.argv[3]
        manager.list_tasks(filter_status)
    
    else:
        print(f"Error: unknown command '{command}'")


if __name__ == '__main__':
    main()
