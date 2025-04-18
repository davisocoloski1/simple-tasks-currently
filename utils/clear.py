import os

class Clear:
    def __init__(self):
        # Clears terminal when executed
        os.system('cls' if os.name == 'nt' else 'clear')