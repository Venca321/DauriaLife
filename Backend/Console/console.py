
"""
Admin console module
"""

def process(user_input:str):
    """
    Process user input and return response
    """
    user_input = user_input.lower()
    if user_input == "help":
        text = """
        help - show this message
        run <python code> - run python code
        """
        return text
    
    if user_input.startswith("run"):
        return eval(user_input.replace("run ", ""))

    return None