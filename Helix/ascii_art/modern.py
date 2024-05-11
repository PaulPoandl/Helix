# modern.py




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
        "           --  ,ggg,        gg                                             \n"
        "           -- dP\"\"Y8b       88           ,dPYb,                          \n"
        "           -- Yb, `88       88           IP'`Yb                            \n"
        "           --  `\"  88       88           I8  8I  gg                       \n"
        "           --      88aaaaaaa88           I8  8'  \"\"                      \n"
        "           --      88\"\"\"\"\"\"\"88   ,ggg,   I8 dP   gg      ,gg,   ,gg \n"
        "           --      88       88  i8\" \"8i  I8dP    88     d8\"\"8b,dP\"    \n"
        "           --      88       88  I8, ,8I  I8P     88    dP   ,88\"          \n"
        "           --      88       Y8, `YbadP' ,d8b,_ _,88,_,dP  ,dP\"Y8,         \n"
        "           --      88       `Y8888P\"Y8888P'\"Y888P\"\"Y88\"  dP\"   \"Y8  \n"
        "           --                                                              \n"
        "           --                                                              \n"
        "           --                                                              \n"
        "                                                                           \n",
        "                                                    \n"
        "           .s    s.                                 \n"
        "                 SS. .s5SSSs.  .s        s.  .s5 s. \n"
        "           sS    S%S       SS.           SS.     SS.\n"
        "           SS    S%S sS    `:; sS        S%S ssS SSS\n"
        "           SSSs. S%S SSSs.     SS        S%S  SSSSS \n"
        "           SS    S%S SS        SS        S%S SSS SSS\n"
        "           SS    `:; SS        SS        `:; SSS `:;\n"
        "           SS    ;,. SS    ;,. SS    ;,. ;,. SSS ;,.\n"
        "           :;    ;:' `:;;;;;:' `:;;;;;:' ;:' `:; ;:'\n"
        "                                                    \n",
        
        "             _       _    _            _              _     _      _        \n"
        "            / /\    / /\ /\ \         _\ \           /\ \ /_/\    /\ \      \n"
        "           / / /   / / //  \ \       /\__ \          \ \ \\ \ \   \ \_\     \n"
        "          / /_/   / / // /\ \ \     / /_ \_\         /\ \_\\ \ \__/ / /     \n"
        "         / /\ \__/ / // / /\ \_\   / / /\/_/        / /\/_/ \ \__ \/_/      \n"
        "        / /\ \___\/ // /_/_ \/_/  / / /            / / /     \/_/\__/\      \n"
        "       / / /\/___/ // /____/\    / / /            / / /       _/\/__\ \     \n"
        "      / / /   / / // /\____\/   / / / ____       / / /       / _/_/\ \ \    \n"
        "     / / /   / / // / /______  / /_/_/ ___/\ ___/ / /__     / / /   \ \ \   \n"
        "    / / /   / / // / /_______\/_______/\__\//\__\/_/___\   / / /    /_/ /   \n"
        "    \/_/    \/_/ \/__________/\_______\/    \/_________/   \/_/     \_\/    \n"
        "                                                                            \n",
        
        "                                                                       \n"
        "                __   __     _____   __       __   __  __               \n"
        "               /\\_\\ /_/\\  /\\_____\\ /\\_\\     /\\_/\\ /\\  /\\    \n"
        "              ( ( (_) ) )( (_____/ ( ( (     \\/_/ \\ \\/ / /          \n"
        "               \\ \\___/ /  \\ \\__\\   \\ \\_\\     /\\_\\\\ \\  / /  \n"
        "               / / _ \\ \\  / /__/_  / / /__  / / // /  \\ \\          \n"
        "              ( (_( )_) )( (_____\\( (_____(( (_(/ / /\\ \\ \\         \n"
        "               \\/_/ \\_\\/  \\/_____/ \\/_____/ \\/_/\\/__\\/__/      \n"
        "                                                                       \n",
        
        "                                                \n"
        "           {__     {__           {__            \n"
        "           {__     {__           {__ {_         \n"
        "           {__     {__   {__     {__   {__   {__\n"
        "           {______ {__ {_   {__  {__{__  {_ {__ \n"
        "           {__     {__{_____ {__ {__{__   {_    \n"
        "           {__     {__{_         {__{__ {_  {__ \n"
        "           {__     {__  {____   {___{__{__   {__\n"
        "                                                \n",
        
        "                                                                           \n"
        "            --                      ,;                                     \n"
        "            --  .    .            f#i            i   t                     \n"
        "            --  Di   Dt         .E#t            LE   Ej                    \n"
        "            --  E#i  E#i       i#W,            L#E   E#, :KW,      L       \n"
        "            --  E#t  E#t      L#D.            G#W.   E#t  ,#W:   ,KG       \n"
        "            --  E#t  E#t    :K#Wfff;         D#K.    E#t   ;#W. jWi        \n"
        "            --  E########f. i##WLLLLt       E#K.     E#t    i#KED.         \n"
        "            --  E#j..K#j...  .E#L         .E#E.      E#t     L#W.          \n"
        "            --  E#t  E#t       f#E:      .K#E        E#t   .GKj#K.         \n"
        "            --  E#t  E#t        ,WW;    .K#D         E#t  iWf  i#K.        \n"
        "            --  f#t  f#t         .D#;  .W#G          E#t LK:    t#E        \n"
        "            --   ii   ii           tt :W##########Wt E#t i       tDj       \n"
        "            --                        :,,,,,,,,,,,,,.,;.                   \n"
        "                                                                           \n",
        
        "                                                                                    \n"
        "       --      ___           ___           ___                    __                \n"
        "       --     /  /\         /  /\         /  /\       ___        |  |\              \n"         
        "       --    /  /:/        /  /::\       /  /:/      /__/\       |  |:|             \n"
        "       --   /  /:/        /  /:/\:\     /  /:/       \__\:\      |  |:|             \n"
        "       --  /  /::\ ___   /  /::\ \:\   /  /:/        /  /::\     |__|:|__           \n"
        "       -- /__/:/\:\  /\ /__/:/\:\ \:\ /__/:/      __/  /:/\/ ____/__/::::\          \n"
        "       -- \__\/  \:\/:/ \  \:\ \:\_\/ \  \:\     /__/\/:/~~  \__\::::/~~~~          \n"
        "       --      \__\::/   \  \:\ \:\    \  \:\    \  \::/        |~~|:|              \n"
        "       --      /  /:/     \  \:\_\/     \  \:\    \  \:\        |  |:|              \n"
        "       --     /__/:/       \  \:\        \  \:\    \__\/        |__|:|              \n"
        "       --     \__\/         \__\/         \__\/                  \__\|              \n"
        "                                                                                    \n",
    ]
    random_color = random.choice(colors)
    random_art = random.choice(ascii_arts)
    colored_art = f"{random_color}{random_art}{Fore.RESET}"
    return colored_art