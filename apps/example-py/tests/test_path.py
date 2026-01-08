import os

def test_print_os_path(monkeypatch):
    print("OS PATH:", os.environ.get("PATH"))