from pathlib import Path

def read_file_to_string_win(file_path: Path) -> str:
    """
    Read File and Return as String
    
    Args:
        path (String): Path to file
    
    Returns:
        String: File as String
    """
    with file_path.open("r") as file:
        return file

def write_string_to_file_win(file_content: str, file_path: Path):
    """
    Opens or creates File and write given content in it
    
    Args:
        content (String): Content to be saved as file
        path (String): Path to File
    """
    with file_path.open('a') as file:
        file.write(file_content)
    
    