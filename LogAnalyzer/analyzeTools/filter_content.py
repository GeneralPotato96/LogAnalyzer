'''
This module contains functions to filter the given textfiles
'''

def get_lines_containing_keywords(content: str, keywords: list) -> list:
    '''
    Finds all Lines containing multipla keywords
    
    Args:
        content (str): Text that will be searched for keywords
        keywords (str)
    Returns:
        result (list): List of Lines containing Keywords
    '''
    lines = content.splitlines()
    tmp_lines = []
    
    for line in lines:
        if keywords[0] in line:
            tmp_lines.append(line)
    
    tmp_text = '\n'.join(tmp_lines)

    print(f"TMP_LINES: {tmp_lines}")
        
    if len(tmp_lines) == 0 or len(keywords) == 1:
        #recursion anchor
        return tmp_lines
    else: 
        return get_lines_containing_keywords(
            tmp_text, keywords[1:len(keywords)])
        
def get_content_between_keywords(content: str, start_keyword: str, end_keyword : str) -> str:
    '''
    Returns Content between two given Keywords
    
    Args:
        contetn (str)
        keywords (list)
    Returns:
        str
    '''
     
    result = ""
    write_str_bool = False
    
    for word in content.split(' '):
        write_str_bool = True if word == start_keyword else write_str_bool 
        result = result + word + " " if write_str_bool else result
        write_str_bool = False if word == end_keyword else write_str_bool
    
    return result.strip()
            
def get_lines_bewtween_strings(conten: str, start_string: str, end_string: str) -> list:
    '''
    Returns Lines Between two given string inclusive the lines containing the Strings
    
    Args:
        content (str)
        start_string (str)
        end_string (str)
    Returns:
        result (list): list containing matching lines
    '''

    result = []
    write_str_bool = False
    
    for line in conten.splitlines():
        write_str_bool = True if start_string in line else write_str_bool
        result.append(line) if write_str_bool else result
        write_str_bool = False if end_string in line else write_str_bool
        
    return result