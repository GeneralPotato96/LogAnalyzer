from dataclasses import dataclass

@dataclass
class AppConfig:
    """Contains Config Inforations"""
    operating_sys: str
    log_file_type: str