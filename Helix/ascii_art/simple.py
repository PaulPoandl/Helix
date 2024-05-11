# simple.py




# Import 
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()




# Getting Art
def get_random_ascii_art():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    ascii_arts = [
    
        "                                              \n"
        "           d8b              d8b   d8,         \n"
        "           ?88              88P  `8P          \n"
        "            88b            d88                \n"
        "            888888b  d8888b888    88b?88,  88P\n"
        "            88P `?8bd8b_,dP?88    88P `?8bd8P'\n"
        "           d88   88P88b     88b  d88  d8P?8b, \n"
        "          d88'   88b`?888P'  88bd88' d8P' `?8b\n"
        "                                              \n",
        
        "                                                              \n"
        "           echo    ,; .-. .-.  ,---.   ,-.     ,-. .-.   .-.; \n"
        "           echo    ,; | | | |  | .-'   | |     |(|  ) \_/ /;  \n"
        "           echo    ,; | `-' |  | `-.   | |     (_) (_)   /;   \n"
        "           echo    ,; | .-. |  | .-'   | |     | |   / _ \;   \n"
        "           echo    ,; | | |)|  |  `--. | `--.  | |  / / ) \;  \n"
        "           echo    ,; /(  (_)  /( __.' |( __.' `-' `-' (_)-'; \n"
        "           echo    ,; (__)     (__)     (_)                  ;\n"
        "                                                              \n",
        
        "                                                   \n"
        "       -- .##..##..######..##......######..##..##. \n"
        "       -- .##..##..##......##........##.....####.. \n"
        "       -- .######..####....##........##......##... \n"
        "       -- .##..##..##......##........##.....####.. \n"
        "       -- .##..##..######..######..######..##..##. \n"
        "       -- ........................................ \n"
        "                                                   \n",
        
        "                                                \n"
        "       -- _|    _|            _|  _|            \n"
        "       -- _|    _|    _|_|    _|      _|    _|  \n"
        "       -- _|_|_|_|  _|_|_|_|  _|  _|    _|_|    \n"
        "       -- _|    _|  _|        _|  _|  _|    _|  \n"
        "       -- _|    _|    _|_|_|  _|  _|  _|    _|  \n"
        "                                                \n",
        
        "                                        \n"
        "           --  _     _       _  _       \n"
        "           -- (_)   (_)     | |(_)      \n"
        "           --  _______ _____| | _ _   _ \n"
        "           -- |  ___  | ___ | || ( \ / )\n"
        "           -- | |   | | ____| || |) X ( \n"
        "           -- |_|   |_|_____)\_)_(_/ \_)\n"
        "                                        \n",
        
        "                                                               \n"
        "           -- 88        88              88  88                 \n"
        "           -- 88        88              88  ""                 \n"
        "           -- 88        88              88                     \n"
        "           -- 88aaaaaaaa88   ,adPPYba,  88  88  8b,     ,d8    \n"
        "           -- 8'''''''''8   888         88  88  88`Y8, ,8P'    \n"
        "           -- 88        88  8PP'''''''  88  88     )888(       \n"
        "           -- 88        88  'a   ,aa    88  88   ,d8" "8b,     \n"
        "           -- 88        88   `'bd88'    88  88  8P'     `Y8    \n"
        "                                                               \n",
        
        "                                                    \n"
        "           -- ____    ____        ___               \n"
        "           -- `MM'    `MM'        `MM 68b           \n"
        "           --  MM      MM          MM Y89           \n"
        "           --  MM      MM   ____   MM ___ ____   ___\n"
        "           --  MM      MM  6MMMMb  MM `MM `MM(   )P'\n"
        "           --  MMMMMMMMMM 6M'  `Mb MM  MM  `MM` ,P  \n"
        "           --  MM      MM MM    MM MM  MM   `MM,P   \n"
        "           --  MM      MM MMMMMMMM MM  MM    `MM.   \n"
        "           --  MM      MM MM       MM  MM    d`MM.  \n"
        "           --  MM      MM YM    d9 MM  MM   d' `MM. \n"
        "           -- _MM_    _MM_ YMMMM9 _MM__MM__d_  _)MM_\n"
        "                                                    \n",      
    ]
    random_color = random.choice(colors)
    random_art = random.choice(ascii_arts)
    colored_art = f"{random_color}{random_art}{Fore.RESET}"
    return colored_art
