#  Project Tracker CLI Tool
  ## Overview
        This is an entry-level command-line project management application developed in Python.

        The tool enables administrators to perform the following actions:

        -Create user accounts

        -Assign projects to specific users

        -Create and add tasks to projects

        -Update task statuses (mark as complete)

        -Manage persistent data storage via JSON files

    This project serves as a practical demonstration of object-oriented programming (OOP) principles, command-line interface design, file input/output operations, and automated testing.

  ## Technologies Used
    -Python 3.10+

    -argparse (for CLI argument handling)

    -json (for data persistence)

    -rich (for aesthetic and formatted CLI output)

    -pytest (for unit testing)

    -Git & GitHub (for version control)

 ## Project Structure

    python-project-management-cli/
│
    ├── main.py
    ├── models/
    ├── utils/
    ├── data/
    ├── tests/
    ├── venv/


---

---

## Setup Instructions

### 1. Clone the repository
    ```bash
    git clone https://github.com/YOUR_USERNAME/python-project-management-cli.git

    cd python-project-management-cli
    ```

### 2. Create virtual environment
    ```bash
    python -m venv venv source venv/Scripts/activate
    ```

### 3. Install dependencies
    ```bash
pip install -r requirements.txt
```

---

## Running the Application

### Add a user
    ```bash
    python main.py add-user --name "Alex" --email "alex@gmail.com
 ```

### List users
    ```bash
    python main.py list-users
    ```

### Add a project
    ```bash
python main.py add-project --user "Alex" --title "CLI Tool" --description "Build tool" --due_date "2026-03-01"
    ```

### Add a task
    ```bash
    python main.py add-task --project "CLI Tool" --title "Write code" --assigned_to "Alex"
    ```

### Mark task complete
    ```bash
    python main.py complete-task --title "Write code"
    ```

---

## Testing
    ```bash
    Run tests using:
    python -m pytest
```

---

## Features Implemented

    - Object-oriented design (User → Project → Task)
    - One-to-many relationships
    - Command-line interface using argparse
    - JSON file persistence
    - External package usage (rich)
    - Unit testing using pytest

---

## Known Limitations

    - Data validation is minimal
    - No authentication system
    - JSON loading assumes correct format

---

## Author

    Luis Maleya






