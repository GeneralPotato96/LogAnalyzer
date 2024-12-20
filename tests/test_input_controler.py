import io

from pathlib import Path
from contextlib import redirect_stdout

from LogAnalyzer.input_controler import command_is_valid, process_command_and_show_result


def test_command_is_valid_true():
    assert command_is_valid("lb") == True

def test_command_is_valid_false():
    assert command_is_valid("Kuchen") == False


def test_process_command_and_show_result():
    test_log_path = Path(__file__).parent / "test_resources" / "test.log"
    #print(f"TEST-PATH: {test_log_path}")
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        process_command_and_show_result(test_log_path, "lc", "UserService", "DatabaseQuery")
    output = buffer.getvalue().strip()
    assert output == [
        "2024-12-19 10:00:05 INFO  UserService - Fetching user with ID: 12345",
        "2024-12-19 10:00:07 DEBUG DatabaseQuery - Executing query: SELECT * FROM users WHERE id = 12345"
    ]