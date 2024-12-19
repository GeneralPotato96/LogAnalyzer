#!/usr/bin/env python3
import sys
from pathlib import Path
from LogAnalyzer.input_controler import process_command_and_show_result, handle_commands
from LogAnalyzer.config.myconfigparser import read_properties, map_to_config, AppConfig

configuration = AppConfig

def config():
    properties_path = Path(__file__).parent / "LogAnalyzer" / "config" / "application.properties"
    properties = read_properties(properties_path)
    configuration = map_to_config(properties)
    print(config)

def main():
    while True:
        user_input = input("Bitte gib etwas ein ('-h' für Hilfe): ")
        handle_commands(user_input)
    
    

if __name__ == "__main__":
    config()
    main()
    
    