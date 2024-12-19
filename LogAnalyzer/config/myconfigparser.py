#import configparser
from pathlib import Path

from .appconfig import AppConfig

def read_properties(file_path: Path) -> dict:
    """
    Reads a properties file and returns a dict
     
    Args:
        file_path (Path)
        
    Returns:
        app_config (dict): Application Configuration as dict
    """
    #config = configparser.ConfigParser()
    #TODO: change to configparser (add sections in properties)
    
    config_dict = {}
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config_dict[key.strip()] = value.strip()
                
    return config_dict

def map_to_config(properties: dict) -> AppConfig:
    """
    Maps properties dictionary to the AppConfig dataclass.
    
    Args:
        properties (dict)

    Returns: AppConfig (Custom config Data-Class)

    """
    return AppConfig(
        operating_sys=properties["app.operating_sys"],
        log_file_type=properties["app.log_file_type"]
    )