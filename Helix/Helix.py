# Internet Check
import requests
import sys
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
def check_internet():
    try:
        requests.get('https://www.google.com/', timeout=3)
        return True
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False
if check_internet():
    pass
else:
    print("")
    print(f"{Colors.YELLOW}Warning: Please check your Internet-connection.{Colors.END}") 
    print(f"{Colors.YELLOW}Warning: The program cannot run properly without Internet.{Colors.END}")
    print(f"{Colors.RED}Helix: {Colors.END}{Colors.BLUE}Hey! I will keep your spot warm until you are connected.")
    print("")
    sys.exit(1)




# Main Program
# Import
import time
import datetime
import subprocess
import os
import requests
import json
import webbrowser
import pyttsx3
import pyjokes
import keyboard
from pynput import keyboard
import re
import pywhatkit
import wikipedia
from fuzzywuzzy import fuzz, process
import random
import wolframalpha
from wolframalpha import Client
import warnings
from bs4 import GuessedAtParserWarning
from textblob import TextBlob
import socket
import threading
#import spacy
import openai
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




# Warnings Filter
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)




# Google Calendar API setup
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'




# API Keys and Location and Status and Name
def read_api_key(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_api_key(api_key):
    client = wolframalpha.Client(api_key)
    try:
        res = client.query("2+2")
        if res and 'pod' in res:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error testing API Key: {e}\n")
        return False
def change_api_key(new_key, file_path):
    if test_api_key(new_key):
        try:
            with open(file_path, 'w') as file:
                file.write(new_key)
            print(f"{Colors.YELLOW}API Key updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating API Key: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid API Key. Please enter a valid key.{Colors.END}\n")
api_key_file = 'Memory/app_id-WolframAlpha.txt'
WOLFRAMALPHA_APP_ID = read_api_key(api_key_file)
def read_api_key2(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_api_key2(api_key):
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            model="davinci-002", 
            prompt="This is a test", 
            max_tokens=5
        )
        return True if response else False
    except Exception as e:
        print(f"Error testing OpenAI API Key: {e}\n")
        return False
def change_api_key2(new_key, file_path):
    if test_api_key2(new_key):
        try:
            with open(file_path, 'w') as file:
                file.write(new_key)
            print(f"{Colors.YELLOW}API Key updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating API Key: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid API Key. Please enter a valid key.{Colors.END}\n")
api_key_file2 = 'Memory/api_key_OpenAI.txt'
openai.api_key = read_api_key2(api_key_file2)
openai_api_key = openai.api_key 
def save_location(location, file_path):
    with open(file_path, 'w') as file:
        file.write(location)
def read_location(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_location(location, app_id):
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(f"weather in {location}")
        if hasattr(res, 'pods'):
            for pod in res.pods:
                if "weather" in pod.title.lower():
                    return True 
            print(f"No weather information found in the response for {location}")
            return False
        else:
            print(f"Unexpected response format: {res}")
            return False
    except Exception as e:
        print(f"{Colors.YELLOW}Exception occurred: {e}{Colors.END}\n")
        return False
def change_location(new_location, file_path, app_id):
    if test_location(new_location, app_id):
        try:
            with open(file_path, 'w') as file:
                file.write(new_location)
            print(f"{Colors.YELLOW}Location updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating location: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid location. Please enter a valid location.{Colors.END}\n")
location_file = 'Memory/user_location.txt'
user_location = read_location(location_file)
def read_name(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def change_name(new_name, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(new_name)
        print(f"{Colors.YELLOW}Name saved successfully.{Colors.END}\n")
    except Exception as e:
           print(f"{Colors.YELLOW}Error saving name: {e}{Colors.END}\n")
name_file = 'Memory/user_name.txt'
user_name = read_name(name_file)
def read_status_wolfram(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_status_wolfram(status):
    if status == "activate" or status == "deactivate":
        return True
    else:
        return False
def change_status_wolfram(new_status, file_path):
    if test_status_wolfram(new_status):
        try:
            with open(file_path, 'w') as file:
                file.write(new_status)
            print(f"{Colors.YELLOW}Status updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating status: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid status. Please enter a valid status.{Colors.END}\n")
status_wolfram_file = 'Memory/wolfram_status.txt'
status_wolfram = read_status_wolfram(status_wolfram_file)
def read_status_openai(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_status_openai(status):
    if status == "activate" or status == "deactivate":
        return True
    else:
        return False
def change_status_openai(new_status, file_path):
    if test_status_openai(new_status):
        try:
            with open(file_path, 'w') as file:
                file.write(new_status)
            print(f"{Colors.YELLOW}Status updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating status: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid status. Please enter a valid status.{Colors.END}\n")
status_openai_file = 'Memory/openai_status.txt'
status_openai = read_status_openai(status_openai_file)
def read_status_events(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_status_events(status):
    if status == "activate" or status == "deactivate":
        return True
    else:
        return False
def change_status_events(new_status, file_path):
    if test_status_events(new_status):
        try:
            with open(file_path, 'w') as file:
                file.write(new_status)
            print(f"{Colors.YELLOW}Status updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating status: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid status. Please enter a valid status.{Colors.END}\n")
status_events_file = 'Memory/events_status.txt'
status_events = read_status_events(status_events_file)
def read_status_location(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_status_location(status):
    if status == "activate" or status == "deactivate":
        return True
    else:
        return False
def change_status_location(new_status, file_path):
    if test_status_location(new_status):
        try:
            with open(file_path, 'w') as file:
                file.write(new_status)
            print(f"{Colors.YELLOW}Status updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating status: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid status. Please enter a valid status.{Colors.END}\n")
status_location_file = 'Memory/location_status.txt'
status_location = read_status_location(status_location_file)
def read_status_ServerSocket(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_status_ServerSocket(status):
    if status == "activate" or status == "deactivate":
        return True
    else:
        return False
def change_status_ServerSocket(new_status, file_path):
    if test_status_ServerSocket(new_status):
        try:
            with open(file_path, 'w') as file:
                file.write(new_status)
            print(f"{Colors.YELLOW}Status updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating status: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid status. Please enter a valid status.{Colors.END}\n")
status_ServerSocket_file = 'Memory/serversocket_status.txt'
status_ServerSocket = read_status_ServerSocket(status_ServerSocket_file)




# Greeting
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    elif 18 <= current_hour < 22:
        return "Good evening"
    else:
        return "Good night"
def get_random_ascii_art():
    colors = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]
    ascii_arts = [
        f"{Colors.RED}"
        "                                            \n"
        "           ·································\n"
        "           :                               :\n"
        "           :                               :\n"
        "           :                               :\n"
        "           :  .-. .-..---..-.   .-..-..-.  :\n"
        "           :  | |=| || |- | |__ | | >  <   :\n"
        "           :  `-' `-'`---'`----'`-''-'`-`  :\n"
        "           :                               :\n"
        "           :                               :\n"
        "           :                               :\n"
        "           ·································\n"
        "                                            \n"
        f"{Colors.END}",
        f"{Colors.GREEN}"
        "                                                       \n"
        "           ############################################\n"
        "           #     `;   .'           .;                 #\n"
        "           #    _ `; ; (          .;'   .-..;.    _   #\n"
        "           #   (  ;' ;  ) .-.    .;     `-'   `.,' '  #\n"
        "           #    `.;__;.'.;.-'   ::     ;'     ,'`.    #\n"
        "           # .  .:'  `:. `:::'_;;_.-_.;:._. -'    `._.#\n"
        "           #(_.'       `:                             #\n"
        "           ############################################\n"
        "                                                       \n"
        f"{Colors.END}",
        f"{Colors.YELLOW}"
        "                                                \n"
        "           {__     {__           {__            \n"
        "           {__     {__           {__ {_         \n"
        "           {__     {__   {__     {__   {__   {__\n"
        "           {______ {__ {_   {__  {__{__  {_ {__ \n"
        "           {__     {__{_____ {__ {__{__   {_    \n"
        "           {__     {__{_         {__{__ {_  {__ \n"
        "           {__     {__  {____   {___{__{__   {__\n"
        "                                                \n"
        f"{Colors.END}",
        f"{Colors.MAGENTA}"
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
        "                                                    \n"
        f"{Colors.END}",
        f"{Colors.CYAN}"
        "                                                                       \n"
        "         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "         @                                                            @\n"
        "         @                                                            @\n"
        "         @                                                            @\n"
        "         @                                                            @\n"
        "         @                                .---.                       @\n"
        "         @    .             __.....__     |   |.--.                   @\n"
        "         @  .'|         .-''         '.   |   ||__|                   @\n"
        "         @ <  |        /     .-''\"'-.  `. |   |.--.                   @\n"
        "         @  | |       /     /________\\   \\|   ||  | ____     _____    @\n"
        "         @  | | .'''-.|                  ||   ||  |`.   \\  .'    /    @\n"
        "         @  | |/.'''. \\    .-------------'|   ||  |  `.  `'    .'     @\n"
        "         @  |  /    | |\\    '-.____...---.|   ||  |    '.    .'       @\n"
        "         @  | |     | | `.             .' |   ||__|    .'     `.      @\n"
        "         @  | |     | |   `''-...... -'   '---'      .'  .'`.   `.    @\n"
        "         @  | '.    | '.                           .'   /    `.   `.  @\n"
        "         @  '---'   '---'                         '----'       '----' @\n"
        "         @                                                            @\n"
        "         @                                                            @\n"
        "         @                                                            @\n"
        "         @                                                            @\n"
        "         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "                                                                       \n"
        f"{Colors.END}",
        f"{Colors.GREEN}"
        "                _____                                 \n"
        "             __|  _  |__  ______  ____    ____  __ __ \n"
        "            |  |_| |    ||   ___||    |  |    | \\ ` / \n"
        "            |   _  |    ||   ___||    |_ |    | /   \\ \n"
        "            |__| |_|  __||______||______||____|/__/\_\\\n"
        "               |_____|                                 \n"
        "                                                       \n"
        f"{Colors.END}",
        f"{Colors.YELLOW}"
        "                                                                    \n"
        "           --  ,ggg,        gg                                      \n"
        "           -- dP\"\"Y8b       88           ,dPYb,                    \n"
        "           -- Yb, `88       88           IP'`Yb                    \n"
        "           --  `\"  88       88           I8  8I  gg                \n"
        "           --      88aaaaaaa88           I8  8'  \"\"                \n"
        "           --      88\"\"\"\"\"\"\"88   ,ggg,   I8 dP   gg      ,gg,   ,gg\n"
        "           --      88       88  i8\" \"8i  I8dP    88     d8\"\"8b,dP\" \n"
        "           --      88       88  I8, ,8I  I8P     88    dP   ,88\"   \n"
        "           --      88       Y8, `YbadP' ,d8b,_ _,88,_,dP  ,dP\"Y8,  \n"
        "           --      88       `Y8888P\"Y8888P'\"Y888P\"\"Y88\"  dP\"   \"Y8 \n"
        "           --                                                       \n"
        "           --                                                       \n"
        "           --                                                       \n"
        "                                                                    \n"
        f"{Colors.END}",
        f""
        "              _____                                      _____ \n"
        "             ( ___ )                                    ( ___ )\n"
        "              |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | \n"
        "              |   |            _                         |   | \n"
        "              |   |           ' )     )           /'     |   | \n"
        "              |   |           /'    /'          /'       |   | \n"
        "              |   |        ,/'    /' ____     /' O.    , |   | \n"
        "              |   |       /`---,/' /'    )  /' /'  \  /  |   | \n"
        "              |   |     /'    /' /(___,/' /' /'     \'    |   | \n"
        "              |   | (,/'     (_,(________(__(__ __/' \_  |   | \n"
        "              |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| \n"
        "             (_____)                                    (_____)\n"
        "                                                               \n"
        f"",
        f"{Colors.RED}"
        "                                                                          \n"
        "         .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. \n"
        "        / .. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\\n"
        "        \\ \\/\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ \\/ /\n"
        "         \\/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\\/ / \n"
        "         / /\\      _           _        _          _       _  _      / /\\ \n"
        "        / /\\ \\   _/\\\\___    __/\\\\___  _/\\\\_      _/\\\\_   _/\\/\\\\_   / /\\ \\\n"
        "        \\ \\/ /  (_ __ __)) (_  ____))(_  _))    (____)) (_  / __))  \\ \\/ /\n"
        "         \\/ /    /  |_| \\\\  /  ._))   /  \\\\      /  \\\\    \\/ \\\\      \\/ / \n"
        "         / /\\   /:.  _   \\\\/:. ||___ /:.  \\\\__  /:.  \\\\ __/./.\\\\_    / /\\ \n"
        "        / /\\ \\  \\___| |  //\\  _____))\\__  ____))\\__  //(_  _)  _))  / /\\ \\\n"
        "        \\ \\/ /         \\//  \\//         \\//        \\//   \\// \\//    \\ \\/ /\n"
        "         \\/ /                                                        \\/ / \n"
        "         / /\\.--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\\ \n"
        "        / /\\ \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\/\\ \\\n"
        "        \\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `' /\n"
        "         `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'  "
        "                                                                                            \n"
        f"{Colors.END}",
        f"{Colors.BLUE}"
        "                                                                   \n"
        "                __   __     _____   __       __   __  __  \n"
        "               /\\_\\ /_/\\  /\\_____\\ /\\_\\     /\\_/\\ /\\  /\\ \n"
        "              ( ( (_) ) )( (_____/ ( ( (     \\/_/ \\ \\/ / / \n"
        "               \\ \\___/ /  \\ \\__\\   \\ \\_\\     /\\_\\\\ \\  / /  \n"
        "               / / _ \\ \\  / /__/_  / / /__  / / // /  \\ \\  \n"
        "              ( (_( )_) )( (_____\\( (_____(( (_(/ / /\\ \\ \\ \n"
        "               \\/_/ \\_\\/  \\/_____/ \\/_____/ \\/_/\\/__\\/__/  "
        "                                                                   \n"
        f"{Colors.END}"
    ]
    return random.choice(ascii_arts)
if status_ServerSocket == "activate":
    print("Server socket started on port 12345")
def get_weather(location, app_id):
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(f'weather {location}')
        return next(res.results).text
    except StopIteration:
        return f"Weather information not available."
    except Exception as e:
        return f"An error occurred."
def summarize_weather(weather_info):
    try:
        lines = weather_info.split('\n')
        temperature_info = "none"
        conditions_info = "none"
        humidity_info = "none"
        wind_info = "none"
        for line in lines:
            if "temperature" in line:
                temperature_info = line.split('|')[1].strip()
            elif "conditions" in line:
                conditions_info = line.split('|')[1].strip()
            elif "humidity" in line:
                humidity_info = line.split('|')[1].strip()
            elif "wind speed" in line:
                wind_info = line.split('|')[1].strip()
        temperature = ' '.join(temperature_info.split(' ')[:2]) if '(' in temperature_info else temperature_info
        humidity = humidity_info.split(' ')[0] if humidity_info != "none" else "none"
        conditions = conditions_info if conditions_info != "none" else "none"
        wind_speed = wind_info.split(' ')[0] if wind_info != "none" else "none"
        summary = f"Temp: {temperature}, Humid: {humidity}, Condit: {conditions}, Wind: {wind_speed} m/s"
        return summary
    except Exception as e:
        return "Weather information not available."
def get_google_calendar_events():
    try:
        events_list = []
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        try:
            service = build("calendar", "v3", credentials=creds)
            now = datetime.datetime.utcnow().isoformat() + "Z"  
            print("Getting the upcoming 5 events.")
            events_result = (
                service.events()
                .list(
                    calendarId="primary",
                    timeMin=now,
                    maxResults=5,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                events_list.append((start, event["summary"]))
        except HttpError as error:
            print(f"An error occurred: {error}")
        return events_list
    except:
        print("Files not found.")
def check_files_in_current_directory(file_names):
    current_directory = os.getcwd()
    not_found_files = []
    for file_name in file_names:
        file_path = os.path.join(current_directory, file_name)
        if not os.path.exists(file_path):
            not_found_files.append(file_name)
    if not_found_files:
        if len(not_found_files) == 1:
            print(f"{Colors.YELLOW}Warning: {not_found_files[0]} not set.{Colors.END}")
        else:
            for file_name in not_found_files:
                print(f"{Colors.YELLOW}Warning: {file_name} is not set.{Colors.END}")
def test_api_key_atS(api_key):
    client = wolframalpha.Client(api_key)
    try:
        res = client.query("2+2")
        if res and 'pod' in res:
            return True
        else:
            return False
    except Exception as e:
        print(f"{Colors.YELLOW}Warning: WolframAlpha API Key is not valid.{Colors.END}")
        return False 
def test_api_key_atS2(api_key):
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            model="davinci-002", 
            prompt="This is a test", 
            max_tokens=5
        )
        return True if response else False
    except Exception as e:
        print(f"{Colors.YELLOW}Warning: OpenAI API Key is not valid.{Colors.END}")
        return False
def display_greeting():
    print("For help type 'Help', to exit or clear type 'Exit' or 'Clear'.")
    time_of_day = get_time_of_day()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    ascii_art = get_random_ascii_art()
    if status_events == "activate":
        events = get_google_calendar_events()
    print("\n" + "*" * 80)
    print(ascii_art)
    print(f"{Colors.BLUE}     {time_of_day} {user_name}!{Colors.END}")
    print(f"{Colors.BLUE}     Current time is {current_time}.{Colors.END}")
    print(f"{Colors.BLUE}     How can I help you today?{Colors.END}")
    print("")
    if status_wolfram == "activate" and status_location == "activate":
        if user_location and WOLFRAMALPHA_APP_ID:
            raw_weather_info = get_weather(user_location, WOLFRAMALPHA_APP_ID)
            weather_summary = summarize_weather(raw_weather_info)
            print(f"{Colors.GREEN}     Current Weather: {weather_summary}{Colors.END}")
        else:
            print(f"{Colors.GREEN}     Current Weather: Location or API Key not set.{Colors.END}")
    if status_events == "activate":
        print(f"{Colors.GREEN}     Upcoming Events:{Colors.END}")
        if events:
            for event in events:
                print(f"{Colors.GREEN}     - {event[0]}: {event[1]}{Colors.END}")
        if not events:
            print(f"{Colors.GREEN}     - No events.{Colors.END}")
            print(f"{Colors.GREEN}     - Maybe check files.{Colors.END}")
    print("")
    print("*" * 80 + "\n")
display_greeting()
if status_wolfram == "activate": 
    test_api_key_atS(WOLFRAMALPHA_APP_ID)
if status_openai == "activate": 
    test_api_key_atS2(openai_api_key)
if status_wolfram == "activate":    
    if not WOLFRAMALPHA_APP_ID:
        print(f"{Colors.YELLOW}Warning: WolframAlpha API Key is not set.{Colors.END}")
    if not user_location and status_location == "activate":
        print(f"{Colors.YELLOW}Warning: Location is not set.{Colors.END}")
if status_openai == "activate":
    if not openai.api_key:
        print(f"{Colors.YELLOW}Warning: OpenAI API Key is not set.{Colors.END}")
if status_events == "activate":
    check_files_in_current_directory(["token.json", "credentials.json"])
if not user_name:
    print(f"{Colors.YELLOW}Warning: Name is not set.{Colors.END}")
print("")




# Help Text
help_text = (
    "\n"
    "----Helix----Help--------\n"
    "\n"
    "----Helix----Commands----\n"
    "\n"
    "Function Commands:\n"
    "- Play [song/band/video]: Plays music or videos. Example: Play Imagine Dragons. or play a funny video\n"
    "- Open [website]: Opens a specified website. Example: Open YouTube.\n"
    "  (for youtube, google, gmail, spotify, microsoft office, netflix and amazon without Domain)\n"
    "- Tell me [time/date/joke]: Provides the current time, date, or a random joke. Example: tell me a funny joke\n"
    "- Who is/Who are/What is/What are [query]: Searches for information about a person or a thing on wikipedia.\n"
    "  Example: what is Git Hub\n"
    "- Search wikipedia for [query]: Searches for information about a person or a thing on wikipedia.\n"
    "  Example: search wikipedia for Simpsons\n"
    "- Search browser for [query]: Conducts a web search for the specified query. Example: search browser for a funny cat\n"
    "- Show [weather/calendar/dashboard/settings]: Shows weather information, your events, your dashboard and your settings.\n"
    "  Example: show settings\n"
    "- Change [WolframAlpha API/OpenAI API/location/name/status WolframAlpha/status OpenAI/status events/status location/staus ServerSocket]:\n"
    "  Changes APIs, location, name and activates or deactivates WolframAlpha, OpenAI, events and location.\n"
    "  To change status you should write 'activate' or 'deactivate' next to 'Enter new status:',\n"
    "  after you have executed a command like 'change status events'.\n\n"

    "WolframAlpha Commands:\n"
    "- Calculate [query]: Performs complex calculations. Example: calculate the orbit of Mars.\n"
    "- Solve [query]: Solves mathematical problems. Example: solve x^2 + 3x - 4 = 0.\n"
    "- Convert [unit1 to unit2]: Converts between units. Example: convert 10 meters to feet.\n"
    "- Differentiate [function]: Finds the derivative of a function. Example: differentiate x^2.\n"
    "- Integrate [function]: Finds the integral of a function. Example: integrate cos(x).\n"
    "- Mean [data]: Gives the mean of a word. Example: mean of time.\n"
    "- Properties [object]: Provides properties of a physical object. Example: properties of gold.\n"
    "- Distance [location1 to location2]: Calculates the distance between two locations. Example: distance from New York to London.\n"
    "- Population [location]: Provides population information. Example: population of Japan.\n"
    "- Weather [location]: Provides weather information. Example: weather in Paris.\n"
    "- Length [object]: Measures the length of an object. Example: length of the Amazon River.\n"
    "- Date of [event]: Finds the date of a specific event. Example: date of the first moon landing.\n"
    "- Winners [event]: Lists winners of a specific event. Example: winners of the Nobel Prize in Physics.\n"
    "- Days until [event/date]: Counts the days until a specific event or date. Example: days until Christmas.\n"
    "- Calories [food]: Provides calorie information for food items. Example: calories in an apple.\n"
    "- WolframAlpha answer [query]: Provides a direct answer from WolframAlpha. Example: WolframAlpha answer to the age of the universe.\n\n"

    "OpenAI Commands:\n"
    "- Generate [story/poem/idea/song/dialogue/scenario/joke/script/concept]: Creates original content.\n" 
    "  Example: generate a short story about dragons.\n"
    "- Explain [concept/phenomenon/term/theory/historical event/scientific theory/mathematical concept/technological trend]:\n" 
    "  Explains complex topics. Example: explain the theory of relativity.\n"
    "- Suggest [book/movie/recipe/activity/hobby/app/tool/destination/gift]: Provides suggestions.\n"
    "  Example: suggest a book about space exploration.\n"
    "- Create [recipe/plan/strategy/program]: Helps in creating structured plans. Example: create a workout plan.\n"
    "- Analyze [text/situation/argument/code]: Offers analysis. Example: analyze the plot of 1984.\n"
    "- Translate [sentence/paragraph/phrase/text/word/expression]: Translates into different languages.\n"
    "  Example: translate 'Hello' into French.\n"
    "- Compare [options/choices/products/ideas/techniques/methods/theories/characters]: Compares different entities.\n"
    "  Example: compare renewable energy sources.\n"
    "- Review [book/film/article/product/game/application]: Provides reviews. Example: review the game Cyberpunk 2077.\n"
    "- Summarize [book/text/report]: Summarizes content. Example: summarize the plot of The Great Gatsby.\n"
    "- Brainstorm [ideas/solutions/names/topics/concepts/themes/strategies/plans/alternatives]: Assists in brainstorming.\n"
    "  Example: brainstorm ideas for a science project.\n"
    "- Resolve [conflict/issue/problem/dilemma/challenge/query/coding bug/mathematical problem]: Helps in problem-solving.\n"
    "  Example: resolve a coding issue in Python.\n"
    "- Organize [information/schedule/event/thoughts/workspace/study plan]: Aids in organization. Example: organize a daily schedule.\n"
    "- OpenAI answer [query]: Provides a direct answer from OpenAI. Example: OpenAI answer to the future of AI.\n\n"

    "----Helix----Info----\n"
    "\n"
    "Helix is also adept at understanding everyday conversation, making it versatile in its interactions.\n"
    "Ensure that you don't include any of the aforementioned commands in your everyday interactions, as doing so\n"
    "will trigger the function associated with that specific command.\n\n"

    "You have the option to activate or deactivate OpenAI and WolframAlpha. However, this means that the commands\n"
    "related to WolframAlpha and OpenAI will no longer be available as well as the weather, and Helix will not be capable of handling\n"
    "all everyday commands as effectively. Furthermore, the responses to these everyday commands may not be as satisfactory.\n\n"

    "You also have the option to change your location for weather information, your name (how Helix addresses you),\n"
    "and the APIs for the AIs. To do so, please enter the corresponding command.\n"
    "You can also activate or deactivate location (weather) and events (calendar), but this will result in the\n"
    "absence of this information on your dashboard (start screen), and the specific commands associated with them\n"
    "will no longer function.\n\n"

    "To activate or deactivate the ServerSocket functionality, you can use the corresponding command. When activated,\n"
    "the ServerSocket feature allows you to communicate with Helix from multiple terminals using helix_command command,\n"
    "like helix_command hello. However, to enable this feature globally, you'll need to add specific configuration\n"
    "to your shell configuration file (e.g., bashrc or zshrc). Please refer to the GitHub page for detailed instructions.\n"
    "Keep in mind that when the ServerSocket is deactivated, this functionality will no longer be available.\n"
    "(Remember, when activated the terminal where Helix.py is running still has to be open in the background)\n\n"

    "To obtain the APIs for OpenAI and WolframAlpha, visit their respective websites. For calendar functionality,\n"
    "ensure you have both 'token.json' and 'credentials.json' files saved in the same directory as 'Helix.py'.\n"
    "The 'credentials.json' file can be obtained from Google by following the instructions on their website.\n"
    "After running Helix with Google Calendar for the first time, the token.json file will be automatically\n" 
    "generated in the same directory. However, you may already have the 'credentials.json' file obtained\n"
    "from Google for Calendar. For detailed instructions on activating Google Calendar API and obtaining this file\n,"
    "visit this link https://developers.google.com/calendar/api/quickstart/python.\n\n"

    "For assistance, feel free to reach out to us via email at bytegroovelabs@gmail.com or paul.poandl@gmail.com,\n"
    "or find more information on our website at https://aicommandhub2.wordpress.com.\n\n"
)




# Main Functions and Programm Logic
commands = {
    "play": ["song", "band", "video"],
    "open": ["youtube", "google", "gmail", "spotify", "microsoft office", "netflix","amazon"],
    "show": ["calendar", "weather", "dashboard", "settings"],
    "tell me": ["time", "date", "joke"],
    "who is": [],
    "what is": [],
    "who are": [],
    "what are": [],
    "help": [],
    "clear": [],
    "change": ["WolframAlpha API", "OpenAI API", "location", "status OpenAI", "status WolframAlpha", "name", "status events", "status location", "status ServerSocket"],
    "search browser for": [],
    "search wikipedia for": [],
}
wolframalpha_keywords = {
    "calculate": [],
    "solve": [], 
    "convert": [], 
    "differentiate": [],
    "integrate": [],
    "mean": [],
    "properties": [],
    "distance": [],
    "population": [],
    "weather": [],
    "length": [],
    "date of": [], 
    "winners": [],
    "days until": [], 
    "calories": [],
    "wolframlpha answer": [],
}
openai_keywords = {
    "generate": ["story", "poem", "idea", "song", "dialogue", "scenario", "joke", "script", "concept"],
    "explain": ["concept", "phenomenon", "term", "theory", "historical event", "scientific theory", "mathematical concept", "technological trend"],
    "suggest": ["book", "movie", "recipe", "activity", "hobby", "app", "tool", "destination", "gift"],
    "create": ["recipe", "plan", "strategy", "program"],
    "analyze": ["text", "situation", "argument","code"],
    "translate": ["sentence", "paragraph", "phrase", "text", "word", "expression"],
    "compare": ["options", "choices", "products", "ideas", "techniques", "methods", "theories", "characters"],
    "review": ["book", "film", "article", "product", "game", "application"],
    "summarize": ["book", "text", "report"],
    "brainstorm": ["ideas", "solutions", "names", "topics", "concepts", "themes", "strategies", "plans", "alternatives"],
    "resolve": ["conflict", "issue", "problem", "dilemma", "challenge", "query", "coding bug", "mathematical problem"],
    "organize": ["information", "schedule", "event", "thoughts", "workspace", "study plan"],
    "openai answer": [],
}
def handle_socket_command(client_socket):
    if status_ServerSocket == "activate":
        while True:
            command = client_socket.recv(1024).decode()
            if not command:
                break
            print(f"Received command from socket: {command}")
            server_answer = execute_command_with_input(command)
            if server_answer is not None:
                server_answer 
                client_socket.sendall(server_answer.encode())
        client_socket.close()
def start_server_socket():
    if status_ServerSocket == "activate":
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('localhost', 12345))
        server_socket.listen(5)
        while True:
            client_socket, addr = server_socket.accept()
            print(f"New connection from {addr}")
            client_thread = threading.Thread(target=handle_socket_command, args=(client_socket,))
            client_thread.start()
def main():
    if status_ServerSocket == "activate":
        server_thread = threading.Thread(target=start_server_socket)
        server_thread.start()
    while True:
        command = get_user_input()
        if command.lower() == 'exit':
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Heading out? No problem! I will keep your spot warm for next time.{Colors.END}\n")
            print("When stuck press 'ctrl + c'\n")
            break
        execute_command_with_input(command)
def get_user_input():
    return input(f"{Colors.RED}Command:{Colors.END}")
def execute_command_with_input(command):
    if not command:
        return
    command_lower = command.lower()
    command_parts = command_lower.split()
    joined_command = " ".join(command_parts)
    main_command = command_parts[0]
    closest_command = get_closest_match(main_command, commands)
    closest_wolframalpha_keyword = get_closest_wolframalpha_keyword(main_command)
    closest_openai_keyword = get_closest_openai_keyword(main_command)
    server_answer = ""
    if main_command in commands:
        server_answer = execute_command(command)
    elif any(keyword in joined_command for keyword in wolframalpha_keywords) and status_wolfram == "activate":
        server_answer = wolframalpha_query(command)
        return server_answer
    elif any(keyword in joined_command for keyword in openai_keywords) and status_openai == "activate":
        server_answer = openai_query(command)
        return server_answer
    else:
        if closest_command:
            server_answer = execute_command(closest_command)
            return server_answer
        elif closest_wolframalpha_keyword and status_wolfram == "activate":
            server_answer = wolframalpha_query(closest_wolframalpha_keyword + " " + " ".join(command_parts[1:]))
            return server_answer
        elif closest_openai_keyword and status_openai == "activate":
            server_answer = openai_query(closest_openai_keyword + " " + " ".join(command_parts[1:]))
            return server_answer
        else:    
            if main_command == "play":
                server_answer = play_music(command)
            elif main_command == "open":
                server_answer = open_website(command)
            elif main_command == "tell":
                server_answer = tell_me(command)
            elif main_command == "who" or main_command == "what":
                server_answer = search_wikipedia(command)
            elif main_command == "search":
                server_answer = search_browser(command)
            elif main_command == "help":
                server_answer = need_help(command)
            elif main_command == "clear":
                server_answer = clear_screen(command)
            elif main_command == "change":
                server_answer = change_setting(command)
            elif main_command == "show":
                server_answer = show_dashboard(command)
            elif main_command in wolframalpha_keywords and status_wolfram == "activate":
                server_answer = wolframalpha_query(command)
            elif main_command in openai_keywords and status_openai == "activate":
                server_answer = openai_query(command)
            else:
                if closest_command:
                    server_answer = execute_command(closest_command)
                    return server_answer
                elif closest_wolframalpha_keyword and status_wolfram == "activate":
                    server_answer = wolframalpha_query(closest_wolframalpha_keyword + " " + " ".join(command_parts[1:]))
                    return server_answer
                elif closest_openai_keyword and status_openai == "activate":
                    server_answer = openai_query(closest_openai_keyword + " " + " ".join(command_parts[1:]))
                    return server_answer
                else:
                    server_answer = allday_conversation(command)
                    return server_answer
def execute_command(command):
    command_parts = command.split()
    main_command = command_parts[0].lower()
    if main_command == "play":
        server_answer = play_music(command)
    elif main_command == "open":
        server_answer = open_website(command)
    elif main_command == "tell":
        server_answer = tell_me(command)
    elif main_command == "who" or main_command == "what":
        server_answer = search_wikipedia(command)
    elif main_command == "search":
        server_answer = search_browser(command)
    elif main_command == "help":
        server_answer = need_help(command)
    elif main_command == "clear":
        server_answer = clear_screen(command)
    elif main_command == "change":
        server_answer = change_setting(command)
    elif main_command == "show":
        server_answer = show_dashboard(command)
    return server_answer
def get_closest_match(query, command_dict, threshold=75):
    best_match = None
    best_match_score = -1
    try:
        for command, options in command_dict.items():
            for option in options:
                score = fuzz.token_sort_ratio(query, option)
                if score > best_match_score:
                    best_match_score = score
                    best_match = f"{command} {option}"
        if best_match_score >= threshold:
            return best_match
        else:
            return None
    except Exception as e:
        server_answer = f"{Colors.BLUE}An error occurred: {e}{Colors.END}\n"
        print(f"{Colors.BLUE}An error occurred: {e}{Colors.END}\n")
        return server_answer
def get_closest_wolframalpha_keyword(query, threshold=75):
    best_match = None
    best_match_score = -1
    try:
        for keyword in wolframalpha_keywords:
            score = fuzz.WRatio(query, keyword)  
            if score > best_match_score:
                best_match_score = score
                best_match = keyword
        if best_match_score >= threshold:
            return best_match
        else:
            return None
    except Exception as e:
        server_answer = f"{Colors.BLUE}An error occurred: {e}{Colors.END}\n"
        print(f"{Colors.BLUE}An error occurred: {e}{Colors.END}\n")
        return server_answer
def get_closest_openai_keyword(query, threshold=75):
    best_match = None
    best_match_score = -1
    try:
        for keyword in openai_keywords:
            score = fuzz.WRatio(query, keyword)  
            if score > best_match_score:
                best_match_score = score
                best_match = keyword
        if best_match_score >= threshold:
            return best_match
        else:
            return None
    except Exception as e:
        server_answer = f"{Colors.BLUE}An error occurred: {e}{Colors.END}\n"
        print(f"{Colors.BLUE}An error occurred: {e}{Colors.END}\n")
        return server_answer
def allday_conversation(command):
    custom_commands = {}
    with open("Pre-Trained Commands/allday_commands.txt", "r", encoding="utf-8", errors="replace") as file:
        for line_number, line in enumerate(file, 1):
            try:
                line = line.strip()
                if line:
                    c, r = line.split(" = ", 1)
                    custom_commands[c] = r
            except UnicodeDecodeError as e:
                server_answer = f"{Colors.BLUE}Error on line {line_number}: {e}{Colors.END}\n"
                print(f"{Colors.BLUE}Error on line {line_number}: {e}{Colors.END}\n")
                print(f"{Colors.BLUE}Problematic line: {line}{Colors.END}\n")
                return server_answer
    if command in custom_commands:
        response = custom_commands[command]
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {response}{Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {response}{Colors.END}\n")
        return server_answer
    else:
        max_score = -1
        closest_match = None
        for c, r in custom_commands.items():
            input_tokens = command.split()
            custom_command_tokens = c.split()
            token_scores = [fuzz.token_sort_ratio(input_token, custom_token) for input_token in input_tokens for custom_token in custom_command_tokens]
            command_score = sum(token_scores) / len(token_scores)
            if command_score > max_score:
                max_score = command_score
                closest_match = r
        if max_score >= 40:
            response = closest_match
            server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {response}{Colors.END}\n"
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {response}{Colors.END}\n")
            return server_answer
        else:
            server_answer = last_openai_query(command)    
            return server_answer  
def wolframalpha_query(command):
    if not WOLFRAMALPHA_APP_ID:
        server_answer = f"{Colors.YELLOW}Warning: Make sure your WolframAlpha API Key is valid and set.{Colors.END}\n"
        print(f"{Colors.YELLOW}Warning: Make sure your WolframAlpha API Key is valid and set.{Colors.END}\n")
        return server_answer
    else:
        client = Client(WOLFRAMALPHA_APP_ID)
        try:
            res = client.query(command)
            answer = next(res.results).text
            server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {answer}{Colors.END}\n"
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {answer}{Colors.END}\n")
            return server_answer
        except Exception as e:
            server_answer = conversation(command)
            return server_answer
def last_wolframalpha_query(command):
    if status_wolfram == "activate":
        if not WOLFRAMALPHA_APP_ID:
            server_answer = f"{Colors.YELLOW}Warning: Make sure your WolframAlpha API Key is valid and set.{Colors.END}\n"
            print(f"{Colors.YELLOW}Warning: Make sure your WolframAlpha API Key is valid and set.{Colors.END}\n")
            return conversation(command)
        else:
            client = Client(WOLFRAMALPHA_APP_ID)
            try:
                res = client.query(command)
                answer = next(res.results).text
                if is_sensible_response(command, answer):
                    server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {answer}{Colors.END}\n"
                    print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {answer}{Colors.END}\n")
                    return server_answer
                else:
                    server_answer = conversation(command)
                    return server_answer
            except Exception as e:
                server_answer = conversation(command)
                return server_answer
    else:
        server_answer = conversation(command)
        return server_answer
def is_sensible_response(command, response):
    if len(response) < 15:
        return False
    doc_command = nlp(command)
    doc_response = nlp(response)
    if doc_response.similarity(doc_command) < 0.5: 
        return False
    sentiment = TextBlob(response).sentiment
    if sentiment.polarity > 0.3 or sentiment.polarity < -0.3:
        return False
    return True     
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]
def openai_query(command):
    if not openai.api_key:
        server_answer = f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}"
        print(f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}")
        return server_answer
    else:
        try:
            message = command
            messages.append({"role": "user", "content": message})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            chat_message = response['choices'][0]['message']['content']
            server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {chat_message}{Colors.END}\n"
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {chat_message}{Colors.END}\n")
            messages.append({"role": "assistant", "content": chat_message})
            return server_answer
        except Exception as e:
            server_answer = conversation(command)
            return server_answer
def last_openai_query(command):
    if status_openai == "activate":
        if not openai.api_key:
            server_answer= f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}"
            print(f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}")
            return conversation(command)
        else:
            try:
                message = command
                messages.append({"role": "user", "content": message})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                chat_message = response['choices'][0]['message']['content']
                if is_valid_response(chat_message, command):
                    server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {chat_message}{Colors.END}\n"
                    print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {chat_message}{Colors.END}\n")
                    messages.append({"role": "assistant", "content": chat_message})
                    return server_answer
                else:
                    server_answer = last_wolframalpha_query(command)
                    return server_answer
            except Exception as e:
                server_answer = last_wolframalpha_query(command)
                return server_answer
    else:
        server_answer = last_wolframalpha_query(command)
        return server_answer
def is_valid_response(response, command):
    min_length = 2
    max_length = 500
    if len(response) < min_length or len(response) > max_length:
        return False
    if not re.search(r'\w+', response):
        return False
    return True
def conversation(command):
    responses = [
        "I'm sorry, I didn't understand that.",
        "Could you please rephrase your command?",
        "I'm here to assist you. What can I do for you?"
    ]
    response = random.choice(responses)
    server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {response}{Colors.END}\n"
    print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {response}{Colors.END}\n")
    return server_answer




# Command Functions
def show_dashboard(command):
    if "weather" in command:
        if status_wolfram == "activate" and status_location == "activate":
            if user_location and WOLFRAMALPHA_APP_ID:
                raw_weather_info = get_weather(user_location, WOLFRAMALPHA_APP_ID)
                weather_summary = summarize_weather(raw_weather_info)
                print("")
                print(f"{Colors.GREEN}Current Weather: {weather_summary}{Colors.END}")
                print("")
            else:
                print("")
                print(f"{Colors.GREEN}Current Weather: Location or API Key not set.{Colors.END}")
                print("")
    elif "calendar" in command:
        print("")
        if status_events == "activate":
            events = get_google_calendar_events()
        print(f"{Colors.GREEN}     Upcoming Events:{Colors.END}")
        if events and status_events == "activate":
            for event in events:
                print(f"{Colors.GREEN}     - {event[0]}: {event[1]}{Colors.END}")
        if not events and status_events == "activate":
            print(f"{Colors.GREEN}     - No events.{Colors.END}")
            print(f"{Colors.GREEN}     - Maybe check files.{Colors.END}")
        print("")
    elif "settings" in command:
        print("")
        print("When you change sth. restart Helix to conf.")
        print("")
        print("----------Communication-Settings----------")
        print("")
        if status_wolfram == "activate":
            print(f"{Colors.YELLOW}WolframAlpha(Command and Weather): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}WolframAlpha(Command and Weather): deactivated.{Colors.END}")
        if status_openai == "activate":
            print(f"{Colors.YELLOW}OpenAI(Command): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}OpenAI(Command): deactivated.{Colors.END}")
        print("")
        if openai.api_key:
            displayed_key = openai.api_key[:15] + '*' * (len(openai.api_key) - 15)
            print(f"{Colors.YELLOW}Open AI API Key: {displayed_key}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Open AI API Key: No Key{Colors.END}")
        if WOLFRAMALPHA_APP_ID:
            displayed_key = WOLFRAMALPHA_APP_ID[:5] + '*' * (len(WOLFRAMALPHA_APP_ID) - 5)
            print(f"{Colors.YELLOW}Wolfram Alpha API Key: {displayed_key}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Wolfram Alpha API Key: No Key{Colors.END}")
        print("")
        print("----------Dashboard----Settings-----------")
        print("")
        if status_events == "activate":
            print(f"{Colors.YELLOW}Events(Calendar): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Events(Calendar): deactivated.{Colors.END}")
        if status_location == "activate":
            print(f"{Colors.YELLOW}Location(Weather): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Location(Weather): deactivated.{Colors.END}")
        print("")
        if user_location:
            print(f"{Colors.YELLOW}User Location: {user_location}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}User Location: No Location{Colors.END}")
        if user_name:
            print(f"{Colors.YELLOW}User Name: {user_name}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}User Name: No Name{Colors.END}")
        print("")
        print("----------ServerSocket---Settings---------")
        print("")
        if status_ServerSocket == "activate":
            print(f"{Colors.YELLOW}ServerSocket(Ext. Com.): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}ServerSocket(Ext. Com.): deactivated.{Colors.END}")
        print("")
        print("----------Important----Informations-------")
        print("")
        if status_wolfram == "activate": 
            test_api_key_atS(WOLFRAMALPHA_APP_ID)
        if status_openai == "activate": 
            test_api_key_atS2(openai_api_key)
        if status_wolfram == "activate":    
            if not WOLFRAMALPHA_APP_ID:
                print(f"{Colors.YELLOW}Warning: WolframAlpha API Key is not set.{Colors.END}")
            if not user_location and status_location == "activate":
                print(f"{Colors.YELLOW}Warning: Location is not set.{Colors.END}")
        if status_openai == "activate":
            if not openai.api_key:
                print(f"{Colors.YELLOW}Warning: OpenAI API Key is not set.{Colors.END}")
        if status_events == "activate":
            check_files_in_current_directory(["token.json", "credentials.json"])
        if not user_name:
            print(f"{Colors.YELLOW}Warning: Name is not set.{Colors.END}")
        print(f"{Colors.YELLOW}No Warnings or no further Warnings.{Colors.END}")
        print("")
    elif "dashboard" in command:
        print("For help type 'Help', to exit or clear type 'Exit' or 'Clear'.")
        time_of_day = get_time_of_day()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        ascii_art = get_random_ascii_art()
        if status_events == "activate":
            events = get_google_calendar_events()
        print("\n" + "*" * 80)
        print(ascii_art)
        print(f"{Colors.BLUE}     {time_of_day} {user_name}!{Colors.END}")
        print(f"{Colors.BLUE}     Current time is {current_time}.{Colors.END}")
        print(f"{Colors.BLUE}     How can I help you today?{Colors.END}")
        print("")
        if status_wolfram == "activate" and status_location == "activate":
            if user_location and WOLFRAMALPHA_APP_ID:
                raw_weather_info = get_weather(user_location, WOLFRAMALPHA_APP_ID)
                weather_summary = summarize_weather(raw_weather_info)
                print(f"{Colors.GREEN}     Current Weather: {weather_summary}{Colors.END}")
            else:
                print(f"{Colors.GREEN}     Current Weather: Location or API Key not set.{Colors.END}")
        if status_events == "activate":
            print(f"{Colors.GREEN}     Upcoming Events:{Colors.END}")
            if events:
                for event in events:
                    print(f"{Colors.GREEN}     - {event[0]}: {event[1]}{Colors.END}")
            if not events:
                print(f"{Colors.GREEN}     - No events.{Colors.END}")
                print(f"{Colors.GREEN}     - Maybe check files.{Colors.END}")
        print("")
        print("*" * 80 + "\n")
        if status_wolfram == "activate": 
            test_api_key_atS(WOLFRAMALPHA_APP_ID)
        if status_openai == "activate": 
            test_api_key_atS2(openai_api_key)
        if status_wolfram == "activate":    
            if not WOLFRAMALPHA_APP_ID:
                print(f"{Colors.YELLOW}Warning: WolframAlpha API Key is not set.{Colors.END}")
            if not user_location and status_location == "activate":
                print(f"{Colors.YELLOW}Warning: Location is not set.{Colors.END}")
        if status_openai == "activate":
            if not openai.api_key:
                print(f"{Colors.YELLOW}Warning: OpenAI API Key is not set.{Colors.END}")
        if status_events == "activate":
            check_files_in_current_directory(["token.json", "credentials.json"])
        if not user_name:
            print(f"{Colors.YELLOW}Warning: Name is not set.{Colors.END}")
        print("")
def change_setting(command):
    if "WolframAlpha API" in command:  
        new_key = input(f"{Colors.BLUE}Enter new WolframAlpha API Key: {Colors.END}")
        change_api_key(new_key, api_key_file)
        global WOLFRAMALPHA_APP_ID
        WOLFRAMALPHA_APP_ID = new_key
    elif "OpenAI API" in command:
        new_key = input(f"{Colors.BLUE}Enter new OpenAI API Key: {Colors.END}")
        change_api_key2(new_key, api_key_file2)
        global openai_api_key
        openai_api_key = new_key
    elif "location" in command:
        if not WOLFRAMALPHA_APP_ID:
            print(f"{Colors.YELLOW}Warning: WolframAlpha API Key is not set.{Colors.END}")
            print(f"{Colors.YELLOW}Warning: First set WolframAlpha API Key.{Colors.END}\n")
        else:    
            new_location = input(f"{Colors.BLUE}Enter new location: {Colors.END}")
            change_location(new_location, location_file, WOLFRAMALPHA_APP_ID)
    elif "status" in command:
        if "WolframAlpha" in command:
            new_status = input(f"{Colors.BLUE}Enter new WolframAlpha status: {Colors.END}")
            change_status_wolfram(new_status, status_wolfram_file)
        elif "OpenAI" in command:
            new_status = input(f"{Colors.BLUE}Enter new OpenAI status: {Colors.END}")
            change_status_openai(new_status, status_openai_file)
        elif "events" in command:
            new_status = input(f"{Colors.BLUE}Enter new events status: {Colors.END}")
            change_status_events(new_status, status_events_file)
        elif "location" in command:
            new_status = input(f"{Colors.BLUE}Enter new location status: {Colors.END}")
            change_status_location(new_status, status_location_file)
        elif "ServerSocket" in command:
            new_status = input(f"{Colors.BLUE}Enter new ServerSocket status: {Colors.END}")
            change_status_ServerSocket(new_status, status_ServerSocket_file)
    elif "name" in command:
        new_name = input(f"{Colors.BLUE}Enter new name: {Colors.END}")
        change_name(new_name, name_file)
def play_music(command):
    query = re.sub(r"play (song|band|video) ", "", command)
    if query:
        pywhatkit.playonyt(query)
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Playing your demand!{Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Playing your demand!{Colors.END}\n")
    return server_answer
def open_website(command):
    website = re.sub(r"open ", "", command)
    common_domains = ["youtube", "google", "gmail", "spotify", "microsoft office", "netflix", "amazon"]
    if any(domain in command for domain in common_domains):
        webbrowser.open_new_tab(f"https://www.{website}.com")
    else:
        webbrowser.open_new_tab(f"https://www.{website}")
    server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Opening: {website.capitalize()}{Colors.END}\n"
    print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Opening: {website.capitalize()}{Colors.END}\n")
    return server_answer
def tell_me(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Time: {current_time}{Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Time: {current_time}{Colors.END}\n")
        return server_answer
    elif "date" in command:
        current_date = datetime.date.today().strftime("%B %d, %Y")
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Date: {current_date}{Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Date: {current_date}{Colors.END}\n")
        return server_answer
    elif "joke" in command:
        joke = pyjokes.get_joke()
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Joke: {joke}{Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Joke: {joke}{Colors.END}\n")
        return server_answer
def search_wikipedia(command):
    query = re.sub(r"^(who is|what is|who are|what are|tell me about) ", "", command, flags=re.IGNORECASE).strip()
    try:
        result = wikipedia.summary(query, sentences=1)
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {result}{Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {result}{Colors.END}\n")
        return server_answer
    except wikipedia.exceptions.DisambiguationError as e:
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} This topic has multiple entries. Here are some options:{Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} This topic has multiple entries. Here are some options:{Colors.END}\n")
        return server_answer
        for option in e.options[:6]:  
            try:
                option_summary = wikipedia.summary(option, sentences=1)
                server_answer = f"{Colors.RED}{option}: {Colors.END}{Colors.BLUE}{option_summary}{Colors.END}"
                print(f"{Colors.RED}{option}: {Colors.END}{Colors.BLUE}{option_summary}{Colors.END}")
                return server_answer
            except Exception:
                server_answer = f"{Colors.BLUE}{option}: No summary available.{Colors.END}"
                print(f"{Colors.BLUE}{option}: No summary available.{Colors.END}")
                return server_answer
        print("")
    except wikipedia.exceptions.PageError:
        suggestions = wikipedia.search(query)
        if suggestions:
            try:
                suggested_result = wikipedia.summary(suggestions[0], sentences=1)
                server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Didn't find an exact match, but here's something related: {suggested_result}{Colors.END}\n"
                print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Didn't find an exact match, but here's something related: {suggested_result}{Colors.END}\n")
                return server_answer
            except Exception as e:
                    server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} An error occurred while fetching related information. {Colors.END}\n"
                    print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} An error occurred while fetching related information. {Colors.END}\n")
                    return server_answer
        else:
            server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Couldn't find information on '{query}'. Try another query.{Colors.END}\n"
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Couldn't find information on '{query}'. Try another query.{Colors.END}\n")
            return server_answer
    except Exception as e:
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} An error occurred. {Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} An error occurred. {Colors.END}\n")
        return server_answer
    return server_answer
def search_browser(command):
    query = re.sub(r"search (browser|wikipedia) for ", "", command)
    if "wikipedia" in command:
        try:
            result = wikipedia.summary(query, sentences=1)
            server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {result}{Colors.END}\n"
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {result}{Colors.END}\n")
            return server_answer
        except wikipedia.exceptions.DisambiguationError as e:
            server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} This topic has multiple entries. Here are some options:{Colors.END}\n"
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} This topic has multiple entries. Here are some options:{Colors.END}\n")
            return server_answer
            for option in e.options[:6]:  
                try:
                    option_summary = wikipedia.summary(option, sentences=1)
                    server_answer = f"{Colors.RED}{option}: {Colors.END}{Colors.BLUE}{option_summary}{Colors.END}"
                    print(f"{Colors.RED}{option}: {Colors.END}{Colors.BLUE}{option_summary}{Colors.END}")
                    return server_answer
                except Exception:
                    server_answer = f"{Colors.BlUE}{option}: No summary available.{Colors.END}"
                    print(f"{Colors.BlUE}{option}: No summary available.{Colors.END}")
                    return server_answer
            print("")
        except wikipedia.exceptions.PageError:
            suggestions = wikipedia.search(query)
            if suggestions:
                try:
                    suggested_result = wikipedia.summary(suggestions[0], sentences=1)
                    server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Didn't find an exact match, but here's something related: {suggested_result}{Colors.END}\n"
                    print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Didn't find an exact match, but here's something related: {suggested_result}{Colors.END}\n")
                    return server_answer
                except Exception as e:
                        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} An error occurred while fetching related information. {Colors.END}\n"
                        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} An error occurred while fetching related information. {Colors.END}\n")
                        return server_answer
            else:
                server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Couldn't find information on '{query}'. Try another query.{Colors.END}\n"
                print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Couldn't find information on '{query}'. Try another query.{Colors.END}\n")
                return server_answer
        except Exception as e:
            server_answer= f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} An error occurred. {Colors.END}\n"
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} An error occurred. {Colors.END}\n")
            return server_answer
    else:
        webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
        server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Your search results are open{Colors.END}\n"
        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} Your search results are open{Colors.END}\n")
        return server_answer
    return server_answer
def need_help(command):
    query = re.sub(r"help ", "", command)
    print(help_text)
def clear_screen(command):
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')




if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE
    main()
