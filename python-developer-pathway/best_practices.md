# 🛡️ Professional Python Best Practices

Writing Python code that works is only the first step. Professional Python developers write code that is clean, readable, testable, and maintainable. This guide outlines the core standards.

---

## 1. Code Style (PEP 8)
Python has an official style guide called **PEP 8**. Follow these key rules:
* **Indentation:** Use **4 spaces** per indentation level. Never use tabs.
* **Line Length:** Limit all lines to a maximum of **79 characters** (or 88 characters if using modern formatters like Black).
* **Naming Conventions:**
  - **Variables & Functions:** `snake_case` (e.g., `calculate_total_price`)
  - **Classes:** `PascalCase` (e.g., `UserManager`)
  - **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)
  - **Private Variables:** Leading underscore (e.g., `_database_connection`)
* **Imports:** 
  - Imports should be on separate lines:
    ```python
    # Correct
    import os
    import sys
    ```
  - Order imports: 1) Standard library, 2) Related third-party imports, 3) Local application imports. Leave a blank line between each group.

---

## 2. Environment & Package Management
Always isolate your project dependencies using a **virtual environment**. This prevents package version conflicts.

### Setting up a Virtual Environment (`venv`):
```bash
# Create a virtual environment named 'env'
python -m venv env

# Activate it:
# On Windows (PowerShell):
.\env\Scripts\Activate.ps1
# On macOS/Linux:
source env/bin/activate
```

### Managing Packages:
Install packages using `pip` and save them to a `requirements.txt` file so others can reproduce your environment:
```bash
# Install a package
pip install requests

# Save dependencies to requirements.txt
pip freeze > requirements.txt

# Install dependencies in a new environment
pip install -r requirements.txt
```

---

## 3. Formatting & Linting Tools
Use automated tools to enforce code quality and styling:
* **Black:** The uncompromising code formatter. It automatically formats files to follow style standards.
  ```bash
  pip install black
  black my_script.py
  ```
* **Flake8:** A linter that checks for syntax errors, style violations, and programming mistakes.
  ```bash
  pip install flake8
  flake8 my_script.py
  ```
* **Mypy:** A static type checker that utilizes type hints to find bugs before running the code.
  ```bash
  pip install mypy
  mypy my_script.py
  ```

---

## 4. Writing Unit Tests
Testing ensures your code behaves as expected and doesn't break when you make changes. Use **pytest** or the built-in **unittest** library.

Example using `pytest`:
* Code to test (`math_ops.py`):
  ```python
  def add(a: float, b: float) -> float:
      return a + b
  ```
* Test file (`test_math_ops.py`):
  ```python
  from math_ops import add

  def test_add():
      assert add(2, 3) == 5
      assert add(-1, 1) == 0
  ```
* Run the tests:
  ```bash
  pytest
  ```

---

## 5. Writing Pythonic Code
* **Use list/dict comprehensions** instead of simple loops where readable:
  ```python
  # Pythonic
  squares = [x**2 for x in range(10)]
  ```
* **Use context managers** for file operations (ensures files are closed properly):
  ```python
  # Pythonic
  with open("file.txt", "r") as f:
      content = f.read()
  ```
* **Use f-strings** for string formatting:
  ```python
  name = "Alice"
  print(f"Hello, {name}!")
  ```
