import subprocess
import sys


def test_add_user_command():
    
    result = subprocess.run(
        [sys.executable, "main.py", "add-user",
         "--name", "TestUser",
         "--email", "test@example.com"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "user added" in result.stdout.lower()


def test_list_users_command():

    result = subprocess.run(
        [sys.executable, "main.py", "list-users"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0