# Project 1: CLI Task Manager Guide

This project is a Command Line Interface (CLI) Task Manager that uses a JSON file to persist tasks. 
It covers:
- Object-Oriented Programming (OOP)
- File handling with JSON
- Argument parsing (`argparse`)
- Unit testing with `unittest`

## Directory Structure:
- `task_manager.py` - Core application logic and CLI entrypoint.
- `test_task_manager.py` - Automated test suite.

## Running the Application:

To see the available commands and help:
```bash
python task_manager.py --help
```

### Examples:
1. **Add a task:**
   ```bash
   python task_manager.py add "Learn Python Decorators"
   ```
2. **List all tasks:**
   ```bash
   python task_manager.py list
   ```
3. **Complete a task (by ID):**
   ```bash
   python task_manager.py complete 1
   ```
4. **Delete a task:**
   ```bash
   python task_manager.py delete 1
   ```

## Running the Tests:
To verify that the implementation works correctly:
```bash
python -m unittest test_task_manager.py
```
