# Day 3: OOP - Task Tracker

## What I Built

A command-line task tracker that lets you manage your to-do list. You can add tasks, mark them done, delete them, and filter by status. All tasks are saved to a JSON file so they stay between runs.

## Usage

```
python tasks.py add "Fix login bug"
python tasks.py add "Update database"
python tasks.py list
python tasks.py done 1
python tasks.py list --filter done
python tasks.py list --filter todo
python tasks.py delete 1
```

## Why Classes?

I could have written all the code as functions at the top level, but then I'd have to pass the tasks list to every function. With a class, the TaskManager keeps the task list and operates on it. The Task class represents a single task and knows how to convert itself to a dictionary for saving.

Classes are better because:
- The data (tasks) stays with the methods that use it
- I can reuse TaskManager in other programs without rewriting it
- The code is organized - Task stuff in Task, managing stuff in TaskManager
- Persistence and error handling are built in

This is how real programs are structured.