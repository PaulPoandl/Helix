# helix.py





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
# Module Import
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
import google.generativeai as genai
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




# Python-file Import
from ascii_art.technical import get_random_ascii_art as technical_art
from ascii_art.modern import get_random_ascii_art as modern_art
from ascii_art.default import get_random_ascii_art as default_art
from ascii_art.simple import get_random_ascii_art as simple_art




# Warnings Filter
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)




# Google Calendar API setup
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'




# Getting random ascii art 
def random_theme_art():
    theme_functions = [technical_art, modern_art, default_art, simple_art]
    random_function = random.choice(theme_functions)
    print(random_function()) 




# Getting Package Manager and Linux Distro
def get_package_manager():
    dist_name = get_linux_distribution()
    package_managers = {
        'almalinux': 'dnf',
        'alpine': 'apk',
        'alt': 'rpm',
        'archlinux': 'pacman',
        'archman': 'pacman',
        'artix': 'pacman',
        'antergos': 'pacman',
        'blackarch': 'pacman',
        'bluestar': 'apt',
        'bodhi': 'apt',
        'calculate': 'emerge',
        'centos': 'yum',
        'chakra': 'pacman',
        'clear': 'yum',
        'condres': 'yum',
        'crux': 'ports',
        'debian': 'apt',
        'debian-gnome': 'apt',
        'debian-kde': 'apt',
        'debian-lxde': 'apt',
        'debian-mate': 'apt',
        'debian-xfce': 'apt',
        'deft': 'apt',
        'deepin': 'apt',
        'elementary': 'apt',
        'elementaryos': 'apt',
        'endeavouros': 'pacman',
        'fedberry': 'dnf',
        'fedora': 'dnf',
        'fermium': 'dnf',
        'garuda': 'pacman',
        'gentoo': 'emerge',
        'gecko': 'pacman',
        'gnew sense': 'apt',
        'huayra': 'apt',
        'kahelos': 'pacman',
        'kali': 'apt',
        'kde neon': 'apt',
        'kaos': 'pacman',
        'lfs': 'lfs',
        'linuxmint': 'apt',
        'linuxmint-cinnamon': 'apt',
        'linuxmint-mate': 'apt',
        'linuxmint-xfce': 'apt',
        'lubuntu': 'apt',
        'mabox': 'apt',
        'mageia': 'urpmi',
        'manjaro': 'pacman',
        'manjaroarm': 'pacman',
        'mklinux': 'apt',
        'nixos': 'nix-env',
        'nixosarm': 'nix-env',
        'openmandriva': 'urpmi',
        'opensuse': 'zypper',
        'opensuse-gnome': 'zypper',
        'opensuse-kde': 'zypper',
        'opensuse-lxde': 'zypper',
        'opensuse-mate': 'zypper',
        'opensuse-xfce': 'zypper',
        'oracle': 'yum',
        'parabola': 'pacman',
        'parrot': 'apt',
        'pclinuxos': 'rpm',
        'pentoo': 'emerge',
        'point': 'apt',
        'pop!_os': 'apt',
        'portlinux': 'apt',
        'pureos': 'apt',
        'q4os': 'apt',
        'reactos': 'setupapi',
        'redcore': 'dnf',
        'redstar': 'urpmi',
        'rosa': 'urpmi',
        'rhel': 'dnf',
        'rocky': 'dnf',
        'sabayon': 'entropy',
        'scientific': 'yum',
        'siduction': 'apt',
        'slackware': 'slackpkg',
        'slax': 'slackpkg',
        'solus': 'eopkg',
        'sparky': 'apt',
        'steamos': 'apt',
        'suse': 'zypper',
        'tails': 'apt',
        'trisquel': 'apt',
        'ubuntu': 'apt',
        'ubuntu-budgie': 'apt',
        'ubuntu-gnome': 'apt',
        'ubuntu-kde': 'apt',
        'ubuntu-kylin': 'apt',
        'ubuntu-mate': 'apt',
        'ubuntu-studio': 'apt',
        'ubuntu-unity': 'apt',
        'ubuntu-xfce': 'apt',
        'ubuntumate': 'apt',
        'ubuntubudgie': 'apt',
        'ultimateedition': 'apt',
        'void': 'xbps-install',
        'voidlinuxarm': 'xbps-install',
        'xubuntu': 'apt',
        'yellowdog': 'rpm',
        'zephyrus': 'pacman',
        'zenwalk': 'netpkg',
        'zorin': 'apt'
    }
    return package_managers.get(dist_name, None)
def get_linux_distribution():
    try:
        with open('/etc/os-release', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('ID='):
                    return line.split('=')[1].strip().lower().replace('"', '')
    except Exception as e:
        return None    
package_manager = get_package_manager()
if not package_manager:
    print("NOTE: Unsupported distribution or package manager not found. Maybe not all works!")

    
    

# API Keys and Location, Status, Name, File Loading, ASCII
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
def read_api_key3(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_api_key3(api_key):
    try:
        genai.configure(api_key=api_key)
        generation_config = {
          "temperature": 0.9,
          "top_p": 1,
          "top_k": 0,
          "max_output_tokens": 2048,
        }
        safety_settings = [
          {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
        ]
        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)
        convo = model.start_chat(history=[
        ])
        convo.send_message("Hello")
        return True
    except Exception as e:
        print(f"Error testing Gemini API Key: {e}\n")
        return False
def change_api_key3(new_key, file_path):
    if test_api_key3(new_key):
        try:
            with open(file_path, 'w') as file:
                file.write(new_key)
            print(f"{Colors.YELLOW}API Key updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating API Key: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid API Key. Please enter a valid key.{Colors.END}\n")
api_key_file3 = 'Memory/api_key_Gemini.txt'
gemini_api_key = read_api_key3(api_key_file3) 
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
def read_status_gemini(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_status_gemini(status):
    if status == "activate" or status == "deactivate":
        return True
    else:
        return False
def change_status_gemini(new_status, file_path):
    if test_status_gemini(new_status):
        try:
            with open(file_path, 'w') as file:
                file.write(new_status)
            print(f"{Colors.YELLOW}Status updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating status: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid status. Please enter a valid status.{Colors.END}\n")
status_gemini_file = 'Memory/gemini_status.txt'
status_gemini = read_status_gemini(status_gemini_file)
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
def read_status_ascii(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_status_ascii(status):
    if status == "activate" or status == "deactivate":
        return True
    else:
        return False
def change_status_ascii(new_status, file_path):
    if test_status_ascii(new_status):
        try:
            with open(file_path, 'w') as file:
                file.write(new_status)
            print(f"{Colors.YELLOW}Status updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating status: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid status. Please enter a valid status.{Colors.END}\n")
status_ascii_file = 'Memory/ascii_status.txt'
status_ascii = read_status_ascii(status_ascii_file)
def read_preference_ascii(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None
def test_preference_ascii(preference):
    if preference == "default" or preference == "modern" or preference == "simple" or preference == "technical" or preference == "random":
        return True
    else:
        return False
def change_preference_ascii(new_preference, file_path):
    if test_preference_ascii(new_preference):
        try:
            with open(file_path, 'w') as file:
                file.write(new_preference)
            print(f"{Colors.YELLOW}Preference updated successfully.{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.YELLOW}Error updating preference: {e}{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}Invalid preference. Please enter a valid status.{Colors.END}\n")
preference_ascii_file = 'Memory/ascii_preference.txt'
preference_ascii = read_preference_ascii(preference_ascii_file)
def load_custom_commands(filename):
    custom_commands = {}
    try:
        with open(filename, 'r', encoding="utf-8", errors="replace") as file:
            for line_number, line in enumerate(file, 1):
                try:
                    line = line.strip()
                    if line:
                        c, r = line.split(" = ", 1)
                        custom_commands[c] = r
                except UnicodeDecodeError as e:
                    print(f"{Colors.BLUE}Error on line {line_number}: {e}{Colors.END}\n")
                    print(f"{Colors.BLUE}Problematic line: {line}{Colors.END}\n")
        return custom_commands
    except FileNotFoundError:
        print("Custom commands file not found.")
        return {}




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
            # now = datetime.now(timezone.utc).isoformat() + "Z"
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
def test_api_key_atS3(api_key):
    try:
        genai.configure(api_key=api_key)
        generation_config = {
          "temperature": 0.9,
          "top_p": 1,
          "top_k": 0,
          "max_output_tokens": 2048,
        }
        safety_settings = [
          {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
        ]
        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)
        convo = model.start_chat(history=[
        ])
        convo.send_message("Hello")
        return True
    except Exception as e:
        print(f"{Colors.YELLOW}Warning: Gemini API Key is not valid.{Colors.END}")
        return False
def display_greeting():
    print("For help type 'Help', to exit or clear type 'Exit' or 'Clear'.")
    time_of_day = get_time_of_day()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if status_events == "activate":
        events = get_google_calendar_events()
    print("\n" + "*" * 80)
    if status_ascii == "activate":
        if preference_ascii == "default":
            print(default_art())
        elif preference_ascii == "modern":
            print(modern_art())
        elif preference_ascii == "simple":
            print(simple_art())
        elif preference_ascii == "technical":
            print(technical_art())
        elif preference_ascii == "random":
            random_theme_art()
        else:
            print(f"")
            print(f"                       -----Check ascii preference.-----           ")
            print(f"")
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
if status_gemini == "activate":
    test_api_key_atS3(gemini_api_key)
if status_wolfram == "activate":    
    if not WOLFRAMALPHA_APP_ID:
        print(f"{Colors.YELLOW}Warning: WolframAlpha API Key is not set.{Colors.END}")
    if not user_location and status_location == "activate":
        print(f"{Colors.YELLOW}Warning: Location is not set.{Colors.END}")
if status_openai == "activate":
    if not openai.api_key:
        print(f"{Colors.YELLOW}Warning: OpenAI API Key is not set.{Colors.END}")
if status_gemini == "activate":
    if not gemini_api_key:
        print(f"{Colors.YELLOW}Warning: Gemini API Key is not set.{Colors.END}")    
if status_events == "activate":
    check_files_in_current_directory(["token.json", "credentials.json"])
if not user_name:
    print(f"{Colors.YELLOW}Warning: Name is not set.{Colors.END}")
if not package_manager:
    print(f"{Colors.YELLOW}Warning: Unsupported distribution.{Colors.END}")
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
    "- Run tcommand to [update system/check diskspace/list directory/display systeminfo/check network/show processes/\n"
    "  show resources/[aim of command]: runs a command in terminal with a specific aim, you can also execute 'run tcommand to'\n"
    "  with any other aim and not only with the pre-defined ones. Example: run tcommand to update system. or run tcommand to delete a file.\n"
    "- linux command to [aim of command]: displays a command with a specific aim. Example: linux command to install a deb file.\n"
    "- Change [WolframAlpha API/OpenAI API/Gemini API/location/name/preference ascii/status WolframAlpha/status OpenAI/status Gemini\n"
    "  status events\status location/status ServerSocket/status Ascii]: Changes APIs, location, name, preference ascii and activates\n"
    "  or deactivates WolframAlpha, OpenAI, Gemini, Ascii, ServerSocket, events and location.\n"
    "  To change status you should write 'activate' or 'deactivate' next to 'Enter new status:',\n"
    "  after you have executed a command like 'change status events'.\n"
    "  To change preference ascii you can choose between technical\simple\modern\default or random\n"
    "  and should write it next to 'Enter new preference:', after you have executed 'change preference ascii'.\n\n"

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
    
    "Gemini Command:\n"
    "- get [latest news/weather forecast/stock market update/crypto prices/sports scores/movie showtimes/traffic updates/music releases]:\n"
    "  To get updated on ceratin things. Example: get latest news.\n"
    "- get tech [latest tech news/newest software versions/latest CVEs/upcoming tech events/hardware releases/software updates]:\n"
    "  To get updated on technical subjects. Example: get tech latest CVEs\n"
    "- get price [on amazon [product]/for [product]/on ebay [product]/for rent [place]/for sale [product]: To receive a price for certain\n"
    "  things. Example: get price on amazon for a new computer.\n" 
    "- brief [[CVE]/article [link to article]/video [link to youtube video]/book/music/album/movie/podcast/[link]]: To get a brief summary\n"
    "  about something. Example: brief video https://www.youtube.com/watch?v=UF_shGiCOpM&t=16s .\n"
    "- code [aim of the code and language]: To code a script with a specific aim. Example: code snake in python.\n"
    "- gemini answer [query]: Provides a direct answer from Gemini. Example: Gemini answer to the aim of AI.\n\n"

    "----Helix----Info----\n"
    "\n"
    "Helix is also adept at understanding everyday conversation, making it versatile in its interactions.\n"
    "Ensure that you don't include any of the aforementioned commands in your everyday interactions, as doing so\n"
    "will trigger the function associated with that specific command.\n\n"

    "You have the option to activate or deactivate OpenAI, Geimini and WolframAlpha. However, this means that the commands\n"
    "related to WolframAlpha, Gemini and OpenAI will no longer be available as well as the weather (by deactivating Wolframalpha),\n"
    "the commands 'run tcommand to' and 'linux command to' (by deactivating OpenAI) and Helix will not be capable of handling\n"
    "all everyday commands as effectively (by deactivating Wolframalpha or/and OpenAI). Furthermore, the responses to these\n" 
    "everyday commands may not be as satisfactory.\n\n"

    "You also have the option to change your location for weather information, your name (how Helix addresses you),\n"
    "your Ascii preference (the way Helix sign is written at the dashboard) and the APIs for the AIs. To do so,\n" 
    "please enter the corresponding command.\n"
    "When you change Ascii preference, you can choose between technical/simple/modern/default or random. Random is\n"
    "a mix of all of them. To look up what Asciis every theme have, please open the corresponding python script for each topic.\n"
    "You will find them in a folder called 'ascii_art'. in the helix folder. Optionally you can add your own art.\n"
    "You can also activate or deactivate location (weather), Ascii (Helix sign) and events (calendar), but this will result in the\n"
    "absence of this information on your dashboard (start screen), and the specific commands associated with them\n"
    "will no longer function.\n\n"

    "To activate or deactivate the ServerSocket functionality, you can use the corresponding command. When activated,\n"
    "the ServerSocket feature allows you to communicate with Helix from multiple terminals using helix_command command,\n"
    "like helix_command hello. However, to enable this feature globally, you'll need to add specific configuration\n"
    "to your shell configuration file (e.g., bashrc or zshrc). Please refer to the GitHub page for detailed instructions.\n"
    "Keep in mind that when the ServerSocket is deactivated, this functionality will no longer be available.\n"
    "(Remember, when activated the terminal where Helix.py is running still has to be open in the background)\n"
    "(Please keep in mind, that the command 'run tcommand to' does not work with ServerSocket, so it only can be\n"
    "executed in the terminal where Helix.py is running, as well as the 'show' and 'change' commands.\n\n"

    "To obtain the APIs for OpenAI, Gemini and WolframAlpha, visit their respective websites. For calendar functionality,\n"
    "ensure you have both 'token.json' and 'credentials.json' files saved in the same directory as 'Helix.py'.\n"
    "The 'credentials.json' file can be obtained from Google by following the instructions on their website.\n"
    "After running Helix with Google Calendar for the first time, the token.json file will be automatically\n" 
    "generated in the same directory. However, you may already have the 'credentials.json' file obtained\n"
    "from Google for Calendar. For detailed instructions on activating Google Calendar API and obtaining this file\n,"
    "visit this link https://developers.google.com/calendar/api/quickstart/python.\n\n"
    
    "When you get the warning 'Warning: unsupported distribution.', it means that you are not able to execute the command\n"
    "'run tcommand to', because your package manager was not found, what is needed for 'run tcommand to update system'.\n"
    "But beside that you can use Helix.py normally.\n\n"

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
    "change": ["WolframAlpha API", "OpenAI API", "Gemini API", "location", "status OpenAI", "status Gemini", "status WolframAlpha", "name", "status events", "status location", "status ServerSocket", "status ascii", "preference ascii"],
    "search browser for": [],
    "search wikipedia for": [],
    "run tcommand to": ["update system", "check diskspace", "list directory", "display systeminfo", "check network", "show processes", "show resources", ""],
    "linux command to": [],
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
gemini_keywords = {
    "get": ["latest news", "weather forecast", "stock market update", "crypto prices", "sports scores", "movie showtimes", "traffic updates", "music releases"],
    "get tech": ["latest tech news", "newest software versions", "latest CVEs", "upcoming tech events", "hardware releases", "software updates"],
    "get price": ["on amazon", "for", "on ebay", "for rent", "for sale"],
    "brief": ["CVE", "article", "video", "book", "music", "album", "movie", "podcast", "link"],
    "code": [],
    "gemini answer": [],
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
    closest_gemini_keyword = get_closest_gemini_keyword(main_command)
    server_answer = ""
    if main_command in commands:
        server_answer = execute_command(command)
    elif any(keyword in joined_command for keyword in wolframalpha_keywords) and status_wolfram == "activate":
        server_answer = wolframalpha_query(command)
        return server_answer
    elif any(keyword in joined_command for keyword in openai_keywords) and status_openai == "activate":
        server_answer = openai_query(command)
        return server_answer
    elif any(keyword in joined_command for keyword in gemini_keywords) and status_gemini == "activate":
        server_answer = gemini_query(command)
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
        elif closest_gemini_keyword and status_gemini == "activate":
            server_answer = gemini_query(closest_openai_keyword + " " + " ".join(command_parts[1:]))
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
            elif main_command == "run":
                server_answer = run_tcommand_to(command)
            elif main_command == "linux command to":
                server_answer = linux_command_to(command)
            elif main_command in wolframalpha_keywords and status_wolfram == "activate":
                server_answer = wolframalpha_query(command)
            elif main_command in openai_keywords and status_openai == "activate":
                server_answer = openai_query(command)
            elif main_command in gemini_keywords and status_gemini == "activate":
                server_answer = gemini_query(command)
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
                elif closest_gemini_keyword and status_gemini == "activate":
                    server_answer = gemini_query(closest_openai_keyword + " " + " ".join(command_parts[1:]))
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
    elif main_command == "run":
        server_answer = run_tcommand_to(command)
    elif main_command == "linux command to":
        server_answer = linux_command_to(command)
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
def get_closest_gemini_keyword(query, threshold=75):
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
        server_answer = f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}\n"
        print(f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}\n")
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
def gemini_query(command):
    if not gemini_api_key:
        server_answer = f"{Colors.YELLOW}Warning: Make sure your Gemini API Key is valid set.{Colors.END}\n"
        print(f"{Colors.YELLOW}Warning: Make sure your Gemini API Key is valid set.{Colors.END}\n")
        return server_answer
    else:
        try:
            genai.configure(api_key=gemini_api_key)
            generation_config = {
              "temperature": 0.9,
              "top_p": 1,
              "top_k": 0,
              "max_output_tokens": 2048,
            }
            safety_settings = [
              {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
              },
              {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
              },
              {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
              },
              {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
              },
            ]
            model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                          generation_config=generation_config,
                                          safety_settings=safety_settings)
            convo = model.start_chat(history=[])
            convo.send_message(command)
            server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {convo.last.text}{Colors.END}\n"
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE} {convo.last.text}{Colors.END}\n")
            return server_answer  # Return the server answer
        except Exception as e:
            server_answer = conversation(command)
            return server_answer
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
        print("Helix-Version: 0.6        When you change sth. restart Helix to conf.")
        print("")
        print("-----------------------Communication--Settings-----------------------")
        print("")
        if status_wolfram == "activate":
            print(f"{Colors.YELLOW}WolframAlpha(Com., Weath.): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}WolframAlpha(Com., Weath.): deactivated.{Colors.END}")
        if status_openai == "activate":
            print(f"{Colors.YELLOW}OpenAI(Com., runtc. linuxc.): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}OpenAI(Com., runtc. linuxc.): deactivated.{Colors.END}")
        if status_gemini == "activate":
            print(f"{Colors.YELLOW}Gemini(Com.): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Gemini(Com): deactivated.{Colors.END}")
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
        if gemini_api_key:
            displayed_key = gemini_api_key[:10] + '*' * (len(gemini_api_key) - 10)
            print(f"{Colors.YELLOW}Gemini API Key: {displayed_key}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Gemini API Key: No Key{Colors.END}")
        print("")
        print("------------------------Dashboard----Settings------------------------")
        print("")
        if status_events == "activate":
            print(f"{Colors.YELLOW}Events(Calend.): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Events(Calend.): deactivated.{Colors.END}")
        if status_location == "activate":
            print(f"{Colors.YELLOW}Location(Weath.): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Location(Weath.): deactivated.{Colors.END}")
        if status_ascii == "activate":
            print(f"{Colors.YELLOW}Ascii(Asci.): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Ascii(Asci.): deactivated.{Colors.END}")
        print("")
        if preference_ascii:
            print(f"{Colors.YELLOW}Ascii Preference: {preference_ascii}{Colors.END}") 
        else:
            print(f"{Colors.YELLOW}Ascii Preference: No Preference{Colors.END}")
        if user_location:
            print(f"{Colors.YELLOW}User Location: {user_location}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}User Location: No Location{Colors.END}")
        if user_name:
            print(f"{Colors.YELLOW}User Name: {user_name}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}User Name: No Name{Colors.END}")
        print("")
        print("----------------------ServerSocket-----Settings----------------------")
        print("")
        if status_ServerSocket == "activate":
            print(f"{Colors.YELLOW}ServerSocket(Ext. Com.): activated.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}ServerSocket(Ext. Com.): deactivated.{Colors.END}")
        print("")
        print("-----------------------System----Compatibility-----------------------")
        print("")
        package_manager = get_package_manager()
        if package_manager:
            print(f"{Colors.YELLOW}Compatibility(runtc. linuxc.): supported.{Colors.END}")
        else:
            print(f"{Colors.YELLOW}Compatibility(runtc. linuxc.): unsupported.{Colors.END}")    
        print("")
        print("----------------------Important----Informations----------------------")
        print("")
        if status_wolfram == "activate": 
            test_api_key_atS(WOLFRAMALPHA_APP_ID)
        if status_openai == "activate": 
            test_api_key_atS2(openai_api_key)
        if status_gemini == "activate":
            test_api_key_atS3(gemini_api_key)
        if status_wolfram == "activate":    
            if not WOLFRAMALPHA_APP_ID:
                print(f"{Colors.YELLOW}Warning: WolframAlpha API Key is not set.{Colors.END}")
            if not user_location and status_location == "activate":
                print(f"{Colors.YELLOW}Warning: Location is not set.{Colors.END}")
        if status_openai == "activate":
            if not openai.api_key:
                print(f"{Colors.YELLOW}Warning: OpenAI API Key is not set.{Colors.END}")
        if status_gemini == "activate":
            if not gemini_api_key:
                print(f"{Colors.YELLOW}Warning: Gemini API Key is not set.{Colors.END}")
        if status_events == "activate":
            check_files_in_current_directory(["token.json", "credentials.json"])
        if not user_name:
            print(f"{Colors.YELLOW}Warning: Name is not set.{Colors.END}")
        if not package_manager:
            print(f"{Colors.YELLOW}Warning: Unsupported distribution.{Colors.END}")
        print(f"{Colors.YELLOW}No Warnings or no further Warnings.{Colors.END}")
        print("")
    elif "dashboard" in command:
        package_manager = get_package_manager()
        print("For help type 'Help', to exit or clear type 'Exit' or 'Clear'.")
        time_of_day = get_time_of_day()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if status_events == "activate":
            events = get_google_calendar_events()
        print("\n" + "*" * 80)
        if status_ascii == "activate":
            if preference_ascii == "default":
                print(default_art())
            elif preference_ascii == "modern":
                print(modern_art())
            elif preference_ascii == "simple":
                print(simple_art())
            elif preference_ascii == "technical":
                print(technical_art())
            elif preference_ascii == "random":
                random_theme_art()
            else:
                print(f"")
                print(f"                       -----Check ascii preference.-----           ")
                print(f"")
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
        if status_gemini == "activate":
            test_api_key_atS3(gemini_api_key)
        if status_wolfram == "activate":    
            if not WOLFRAMALPHA_APP_ID:
                print(f"{Colors.YELLOW}Warning: WolframAlpha API Key is not set.{Colors.END}")
            if not user_location and status_location == "activate":
                print(f"{Colors.YELLOW}Warning: Location is not set.{Colors.END}")
        if status_openai == "activate":
            if not openai.api_key:
                print(f"{Colors.YELLOW}Warning: OpenAI API Key is not set.{Colors.END}")
        if status_gemini == "activate":
            if not gemini_api_key:
                print(f"{Colors.YELLOW}Warning: Gemini API Key is not set.{Colors.END}")
        if status_events == "activate":
            check_files_in_current_directory(["token.json", "credentials.json"])
        if not user_name:
            print(f"{Colors.YELLOW}Warning: Name is not set.{Colors.END}")
        if not package_manager:
            print(f"{Colors.YELLOW}Warning: Unsupported distribution.{Colors.END}")
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
    elif "Gemini API" in command:
        new_key = input(f"{Colors.BLUE}Enter new Gemini API Key: {Colors.END}")
        change_api_key3(new_key, api_key_file3)
        global gemini_api_key
        gemini_api_key = new_key
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
        elif "Gemini" in command:
            new_status = input(f"{Colors.BLUE}Enter new Gemini status: {Colors.END}")
            change_status_gemini(new_status, status_gemini_file)            
        elif "events" in command:
            new_status = input(f"{Colors.BLUE}Enter new events status: {Colors.END}")
            change_status_events(new_status, status_events_file)
        elif "location" in command:
            new_status = input(f"{Colors.BLUE}Enter new location status: {Colors.END}")
            change_status_location(new_status, status_location_file)
        elif "ServerSocket" in command:
            new_status = input(f"{Colors.BLUE}Enter new ServerSocket status: {Colors.END}")
            change_status_ServerSocket(new_status, status_ServerSocket_file)
        elif "ascii" in command:
            new_status = input(f"{Colors.BLUE}Enter new ascii status: {Colors.END}")
            change_status_ascii(new_status, status_ascii_file)     
    elif "name" in command:
        new_name = input(f"{Colors.BLUE}Enter new name: {Colors.END}")
        change_name(new_name, name_file)
    elif "preference ascii" in command:
        new_preference = input(f"{Colors.BLUE}Enter new ascii preference: {Colors.END}")
        change_preference_ascii(new_preference, preference_ascii_file)    
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
def run_tcommand_to(command):
    package_manager = get_package_manager()
    if not package_manager:
        print(f"{Colors.YELLOW}Warning: Unsupported distribution.{Colors.END}")
        print("")
        return 
    if "update system" in command:
        try:
            if package_manager == 'apt':
                os.system('sudo apt update')
                os.system('sudo apt upgrade -y')
                print("")
            elif package_manager == 'yum':
                os.system('sudo yum update -y')
                print("")
            elif package_manager == 'dnf':
                os.system('sudo dnf update -y')
                print("")
            elif package_manager == 'pacman':
                os.system('sudo pacman -Syu --noconfirm')
                print("")
            elif package_manager == 'xbps-install':
                os.system('sudo xbps-install -Su')
                server_answer = f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}Helix is updating in the Host-Terminal. Check there for status!{Colors.END}\n"
                print("")
            elif package_manager == 'apk':
                os.system('sudo apk update')
                os.system('sudo apk upgrade')
                print("")
            elif package_manager == 'emerge':
                os.system('sudo emerge --sync')
                os.system('sudo emerge -auDN @world')
                print("")
            elif package_manager == 'zypper':
                os.system('sudo zypper refresh')
                os.system('sudo zypper update -y')
                print("")
            elif package_manager == 'entropy':
                os.system('sudo equo update')
                os.system('sudo equo upgrade')
                print("")
            elif package_manager == 'eopkg':
                os.system('sudo eopkg update-repo')
                os.system('sudo eopkg upgrade -y')
                print("")
            elif package_manager == 'ports':
                os.system('sudo portsnap fetch update')
                os.system('sudo pkg upgrade')
                print("")
            elif package_manager == 'urpmi':
                os.system('sudo urpmi.update -a')
                os.system('sudo urpmi --auto-select')
                print("")
            elif package_manager == 'rpm':
                os.system('sudo rpm --rebuilddb')
                os.system('sudo dnf update -y')
                print("")
            elif package_manager == 'slackpkg':
                os.system('sudo slackpkg update')
                os.system('sudo slackpkg upgrade-all')
                print("")
            elif package_manager == 'setupapi':
                os.system('sudo reactos rapps --update-all')
                print("")
            elif package_manager == 'lfs':
                os.system('sudo rm -rf /usr/portage/*')
                os.system('sudo emerge-webrsync')
                os.system('sudo emerge --sync')
                os.system('sudo emerge -auDN @world')
                print("")
            elif package_manager == 'nix-env':
                os.system('sudo nix-channel --update')
                os.system('sudo nix-env -u')
                print("")
            else:
                print(f"{Colors.YELLOW}Warning: Unsupported package manager for system update.{Colors.END}")
                print("")
            return True
        except Exception as e:
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system update.{Colors.END}\n")
            return False
    elif "check diskspace" in command:
        try:
            os.system('df -h')
            print("")
            return True
        except Exception as e:
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
            return False
    elif "list directory" in command:
        try:
            os.system('ls -l')
            print("")
            return True
        except Exception as e:
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
            return False
    elif "display systeminfo" in command:
        try:
            os.system('uname -a')
            os.system('cat /etc/*release')
            print("")
            return True
        except Exception as e:
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
            return False
    elif "check network" in command:
        try:
            host = "google.com"  
            os.system(f'ping -c 4 {host}')
            print("")
            return True
        except Exception as e:
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
            return False
    elif "show processes" in command:
        try:
            os.system('ps aux')
            print("")
            return True
        except Exception as e:
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
            return False
    elif "show resources" in command:
        try:
            os.system('top')
            print("")
            return True
        except Exception as e:
            print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
            return False
    else:
        def fuzzy_match(command, commands):
            max_score = -1
            closest_match = None
            for c, r in commands.items():
                input_tokens = command.split()
                tcustom_command_tokens = c.split()
                token_scores = [fuzz.token_sort_ratio(input_token, tcustom_token) for input_token in input_tokens for tcustom_token in tcustom_command_tokens]
                tcommand_score = sum(token_scores) / len(token_scores)
                if tcommand_score > max_score:
                    max_score = tcommand_score
                    closest_match = r
            return closest_match if max_score >= 40 else None
        def get_command_from_chatgpt(command):
            if not openai.api_key:
                print(f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}")
                print("")
                return None
            messages = [{"role": "user", "content": f"give me a linux command to {command} with not text, just write me the command, nothing else, only the command, no unnecessary text, just the command, nothing else, also not bash, just the command as plain text, only the command in no bash, just the plain text!"}]
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                chat_message = response['choices'][0]['message']['content']
                return chat_message
            except:
                print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
                return None
        def explain_command_and_execute(command_to_run):
            if not openai.api_key:
                print(f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}")
                return True
            messages = [{"role": "user", "content": f"explain this linux command {command_to_run} just short, only with maximum of 10 words, not more, just 10, not more, and nothing else, nothing else!"}]
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                chat_message = response['choices'][0]['message']['content']
                print(f"Explanation:'{chat_message}'")
                print("Execute Command?: Y|N (N - try giving you a new command)")
                user_input = input()
                if user_input == "Y":
                    os.system(command_to_run)
                    print("")
                    time.sleep(12)
                    return True  
                elif user_input == "N":
                    if not openai.api_key:
                        print(f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}")
                        return True
                    try:
                        chat_message = get_command_from_chatgpt(command)
                        print(f"Is this your requested command (ChatGPT - API): '{chat_message}'? Y|N (No idea? - type 'explain again' + enter)")
                        user_input = input()
                        if user_input == "Y":
                            os.system(chat_message)
                            print("")
                            time.sleep(12)
                            return True
                        elif user_input == "explain again":
                            if not openai.api_key:
                                print(f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}")
                                return True
                            messages = [{"role": "user", "content": f"explain this linux command {chat_message} just short, only with maximum of 10 words, not more, just 10, not more, and nothing else, nothing else!"}]
                            try:
                                response = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=messages
                                )
                                chat_message = response['choices'][0]['message']['content']
                                print(f"Explanation:'{chat_message}'")
                                print("Execute Command?: Y|N (N - end process of searching command)")
                                user_input = input()
                                if user_input == "Y":
                                    os.system(command_to_run)
                                    print("")
                                    time.sleep(12)
                                    return True 
                                elif user_input == "N":
                                    print("Database (TXT file) and ChatGPT (API) couldn't match your request.")
                                    print("")
                                    return True
                            except:
                                print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
                                return True 
                        elif user_input == "N":
                            print("Database (TXT file) and ChatGPT (API) couldn't match your request.")
                            print("")
                            return True
                    except:
                        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
                        return True
            except:
                print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
            return False  
        while True:
            tcustom_commands = load_custom_commands('./Pre-Trained Commands/tcustom_command.txt')
            command = command.split("run tcommand to", 1)[-1].strip()
            if command in tcustom_commands:
                command_to_run = tcustom_commands[command]
                print(f"Is this your requested command (Database - TXT): '{command_to_run}'? Y|N (No idea? - type 'explain' + enter)")
                user_input = input()
                if user_input == "Y":
                    os.system(command_to_run)
                    print("")
                    time.sleep(12)
                    break
                elif user_input == "explain":
                    try:
                        if explain_command_and_execute(command_to_run):
                            break
                    except:
                        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
                        break
                        return True
                elif user_input == "N":
                    try:
                        chat_message = get_command_from_chatgpt(command)
                        print(f"Is this your requested command (ChatGPT - API): '{chat_message}'? Y|N (No idea? - type 'explain' + enter)")
                        user_input = input()
                        if user_input == "Y":
                            os.system(chat_message)
                            print("")
                            time.sleep(12)
                            break
                        elif user_input == "explain":
                            if explain_command_and_execute(chat_message):
                                break
                        elif user_input == "N":
                            print("Database (TXT file) and ChatGPT (API) couldn't match your request.")
                            print("")
                            break
                            return True
                    except:
                        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
                        break
                        return True
            elif fuzzy_match(command, tcustom_commands):
                command_to_run = fuzzy_match(command, tcustom_commands)
                print(f"Is this your requested command (Database - TXT): '{command_to_run}'? Y|N (No idea? - type 'explain' + enter)")
                user_input = input()
                if user_input == "Y":
                    os.system(command_to_run)
                    print("")
                    time.sleep(12)
                    break
                elif user_input == "explain":
                    try:
                        if explain_command_and_execute(command_to_run):
                            break
                    except:
                        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
                        break
                        return True
                elif user_input == "N":
                    try:
                        chat_message = get_command_from_chatgpt(command)
                        print(f"Is this your requested command (ChatGPT - API): '{chat_message}'? Y|N (No idea? - type 'explain' + enter)")
                        user_input = input()
                        if user_input == "Y":
                            os.system(chat_message)
                            print("")
                            time.sleep(12)
                            break
                        elif user_input == "explain":
                            if explain_command_and_execute(chat_message):
                                break
                        elif user_input == "N":
                            print("Database (TXT file) and ChatGPT (API) couldn't match your request.")
                            print("")
                            break
                            return True
                    except:
                        print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
                        break
                        return True
            else:
                try:
                    chat_message = get_command_from_chatgpt(command)
                    print(f"Is this your requested command (ChatGPT - API): '{chat_message}'? Y|N (No idea? - type 'explain' + enter)")
                    user_input = input()
                    if user_input == "Y":
                        os.system(chat_message)
                        print("")
                        time.sleep(12)
                        break
                    elif user_input == "explain":
                        if explain_command_and_execute(chat_message):
                            break
                    elif user_input == "N":
                        print("Database (TXT file) and ChatGPT (API) couldn't match your request.")
                        print("")
                        break
                        return True
                except:
                    print(f"{Colors.RED}Helix:{Colors.END}{Colors.BLUE}An error occurred during system action.{Colors.END}\n")
                    break
                    return True
                    
            valid_inputs = ["Y", "N", "explain", "explain again"]
            user_input = input()
            if user_input not in valid_inputs:
                print("Invalid input. Please enter try again.")
                break
def linux_command_to(command):
    if not openai.api_key:
        server_answer = f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}\n"
        print(f"{Colors.YELLOW}Warning: Make sure your OpenAI API Key is valid set.{Colors.END}\n")
        return server_answer
    else:
        try:
            message = [{"role": "helpful data base of linux commands", "linux command directory": f"give me a {command} with not text, just write me the command with explaination, nothing else, only the command and the explanation of it, no unnecessary text, just the command and explanation, nothing else!"}]
            messages.append({"role": "helpful data base of linux commands", "linux command directory": message})
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
