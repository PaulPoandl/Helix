# technical.py




# Import 
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()




# Getting Art
def get_random_ascii_art():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    ascii_arts = [
    
        "                                                                           \n"
        "         ░▄▀▄░▀█░░▄▀▄░▄▀▄░▀█░░▄▀▄░▄▀▄░▄▀▄░░░▄▀▄░▀█░░▄▀▄░▄▀▄░▄▀▄░▀█░░▄▀▄░▀█░\n"
        "         ░█/█░░█░░█/█░█/█░░█░░█/█░█/█░█/█░░░█/█░░█░░█/█░█/█░█/█░░█░░█/█░░█░\n"
        "         ░░▀░░▀▀▀░░▀░░░▀░░▀▀▀░░▀░░░▀░░░▀░░░░░▀░░▀▀▀░░▀░░░▀░░░▀░░▀▀▀░░▀░░▀▀▀\n"
        "         ░▄▀▄░▀█░░▄▀▄░▄▀▄░▀█░░▀█░░▄▀▄░▄▀▄░░░▄▀▄░▀█░░▄▀▄░▄▀▄░▀█░░▄▀▄░▄▀▄░▀█░\n"
        "         ░█/█░░█░░█/█░█/█░░█░░░█░░█/█░█/█░░░█/█░░█░░█/█░█/█░░█░░█/█░█/█░░█░\n"
        "         ░░▀░░▀▀▀░░▀░░░▀░░▀▀▀░▀▀▀░░▀░░░▀░░░░░▀░░▀▀▀░░▀░░░▀░░▀▀▀░░▀░░░▀░░▀▀▀\n"
        "         ░▄▀▄░▀█░░▄▀▄░▀█░░▀█░░▄▀▄░▄▀▄░▄▀▄                                  \n"
        "         ░█/█░░█░░█/█░░█░░░█░░█/█░█/█░█/█                                  \n"
        "         ░░▀░░▀▀▀░░▀░░▀▀▀░▀▀▀░░▀░░░▀░░░▀░                                  \n"
        "                                                                           \n",
        
        "        ______  ______  ______  ______  ______  ______  ______ \n"
        "       | |__| || |__| || |__| || |__| || |__| || |__| || |__| |\n"
        "       |  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  |\n"
        "       |______||______||______||______||______||______||______|\n"
        "       ______                                          ______ \n"
        "       | |__| |                                        | |__| |\n"
        "       |  ()  |      ____  ____              _  _      |  ()  |\n"
        "       |______|     |_  _||    | ____  ____ | \/ |     |______|\n"
        "        ______       _||_ ||_| ||  __||____| >  <       ______ \n"
        "       | |__| |     |____||_||_||_|         |_/\_|     | |__| |\n"
        "       |  ()  |                                        |  ()  |\n"
        "       |______|                                        |______|\n"
        "        ______  ______  ______  ______  ______  ______  ______ \n"
        "       | |__| || |__| || |__| || |__| || |__| || |__| || |__| |\n"
        "       |  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  |\n"
        "       |______||______||______||______||______||______||______|\n"
        "                                                               \n",
        
        "                    __ __         __                  ____     ______     \n"
        "                   /\ \\ \      /'_ `\               /'___\   /\  ___\    \n"
        "                   \ \ \\ \    /\ \L\ \             /\ \__/   \ \ \__/    \n"
        "                    \ \ \\ \_  \/_> _ <_            \ \  _``\  \ \___``\  \n"
        "                     \ \__ ,__\  /\ \L\ \            \ \ \L\ \  \/\ \L\ \ \n"
        "                      \/_/\_\_/  \ \____/             \ \____/   \ \____/ \n"
        "                         \/_/     \/___/               \/___/     \/___/  \n"
        "          ____     ____                   ____       __                   \n"
        "         /'___\   /\  _`\                /'___\    /'_ `\                 \n"
        "        /\ \__/   \ \ \/\_\             /\ \__/   /\ \L\ \                \n"
        "        \ \  _``\  \ \ \/_/_            \ \  _``\ \ \___, \               \n"
        "         \ \ \L\ \  \ \ \L\ \            \ \ \L\ \ \/__,/\ \              \n"
        "          \ \____/   \ \____/             \ \____/      \ \_\             \n"
        "           \/___/     \/___/               \/___/        \/_/             \n"
        "         ________    __                                                   \n"
        "        /\_____  \ /'_ `\                                                 \n"
        "        \/___//'/'/\ \L\ \                                                \n"
        "            /' /' \/_> _ <_                                               \n"
        "          /' /'     /\ \L\ \                                              \n"
        "         /\_/       \ \____/                                              \n"
        "         \//         \/___/                                               \n"
        "                                                                          \n",
        
        "                                                                          \n"
        "                        : '                                               \n"
        "                        .-. .-..---..-.   .-..-..-.                       \n"
        "                        | |=| || |- | |__ | | >  <                        \n" 
        "                        `-' `-'`---'`----'`-''-'`-`                       \n"
        "                        '                                                 \n"
        "                                                                          \n",
        
        "                                                                          \n"
        "                         -- 72 101 108 105 120                            \n"
        "                                                                          \n",
        
        "                                                                          \n"
        "    --  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄     \n"
        "    -- ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌     ▐░▌    \n"
        "    -- ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌           ▀▀▀▀█░█▀▀▀▀  ▐░▌   ▐░▌     \n"
        "    -- ▐░▌       ▐░▌▐░▌          ▐░▌               ▐░▌       ▐░▌ ▐░▌      \n"
        "    -- ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌               ▐░▌        ▐░▐░▌       \n"
        "    -- ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌               ▐░▌         ▐░▌        \n"
        "    -- ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌               ▐░▌        ▐░▌░▌       \n"
        "    -- ▐░▌       ▐░▌▐░▌          ▐░▌               ▐░▌       ▐░▌ ▐░▌      \n"
        "    -- ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄  ▐░▌   ▐░▌     \n"
        "    -- ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌    \n"
        "    --  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀     \n"
        "                                                                          \n",
        
        "                                                                          \n"
        "                                                                          \n"     
        "         --  █████   █████          ████   ███                            \n"
        "         -- ░░███   ░░███          ░░███  ░░░                             \n"
        "         --  ░███    ░███   ██████  ░███  ████  █████ █████               \n"
        "         --  ░███████████  ███░░███ ░███ ░░███ ░░███ ░░███                \n"
        "         --  ░███░░░░░███ ░███████  ░███  ░███  ░░░█████░                 \n"
        "         --  ░███    ░███ ░███░░░   ░███  ░███   ███░░░███                \n"
        "         --  █████   █████░░██████  █████ █████ █████ █████               \n"
        "         -- ░░░░░   ░░░░░  ░░░░░░  ░░░░░ ░░░░░ ░░░░░ ░░░░░                \n"     
        "                                                                          \n"
        "                                                                          \n",
        
    ]
    random_color = random.choice(colors)
    random_art = random.choice(ascii_arts)
    colored_art = f"{random_color}{random_art}{Fore.RESET}"
    return colored_art