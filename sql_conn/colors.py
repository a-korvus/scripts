"""Some colors for the python output."""

import colorama
from colorama import Fore, Back

blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
red_error = Back.LIGHTRED_EX
color_back_end = Back.RESET

colorama.init(autoreset=True)
