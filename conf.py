import os
from src import printcolors as pc

pc.printout("# - Remake By Erzox", pc.YELLOW)
pseudo=input("\nPseudo of victim: ")

os.system(f"python3 main.py {pseudo}")