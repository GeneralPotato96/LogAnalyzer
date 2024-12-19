
'''
This module awaits and process user input
'''
from analyzeTools.filter_content import get_lines_containing_keywords
from pathlib import Path
from utils.read_and_write_file import read_file_to_string_win

def show_help():
    helpfile_path = Path(__file__).parent / "config" / "helpfile"
    with open(helpfile_path, "r") as file:
        file_content = file.read()
        print(file_content)


def process_command_and_show_result(file_path: Path, command: str, *args):
    '''
    Process user Commands and shows direct output
    
    Args:
        file_path (Path): Path to File that should be processed
        command (str): user command
        args
    '''
    if not command_is_valid(command):
        print("Bitte geben sie einen gültigen Befehl ein. (-h für Hilfe)")
    if command == 'lc':
        content = read_file_to_string_win(file_path)
        print(get_lines_containing_keywords(content, args))
        
        
    
def command_is_valid(command: str) -> bool:
    '''checks if command is valid'''
    
    command_list = ["lc", "lb", "cb"]
    if any(command_list in command for comm in command_list):
        return True
    else:
        return False
    
    
def handle_commands(*args):
    '''
    Decides on first base witch args are given and chooses correct pathway
    '''
    
    #TODO: decide if switch cases are the better option
    
    if len(args) < 1:
        print("ERROR Bitte übergeben wir sie mindestsn ein Komando")
    elif args[0] == '-h':
        show_help()
    elif args[0] == '-q':
        exit(0)
    elif args[0] == '-l' and len(args) >= 4:
        process_command_and_show_result(args[1:])
        
    
    
    