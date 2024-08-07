# Helix - Personal Assistant for Linux/GNU

![Helix](https://github.com/PaulPoandl/Helix/assets/75140549/55c5d33d-50f9-4a37-bfa7-90909e07b629)

Helix is a personal Assistant made for Linux/GNU. He supports a wide range of commands and functions, optional you can also
add an WolframAlpha API, Gemini API and OpenAI API for more features. 

## Installation

Run the requirements.txt file:
```bash
pip install -r requirements.txt
```
Then start Helix with Python:
```bash
pyhton3 Helix.py
```
From now on you can then start Helix with "pyhton3 Helix.py", but remember that you always have to navigate to the Helix
folder to start Helix.

## Socket Server Installation

To set up the socket server (to make Helix accesible with a command from any terminal, while it is running in 
the back. in one terminal), you need to perform the following steps:

### 1. Edit .zshrc or .bashrc

Add the following code snippet to your `.zshrc` or `.bashrc` file:

```bash
# Helix
function helix_command() {
    local command="$*"
    if [ -z "$command" ]; then
        echo "Usage: helix_command <command>"
        return 1
    fi
    echo -n "$command" | nc -q 0 localhost 12345 | sed 's/\x00//g'
}
```
To open .zshrc or .bashrc, use a text editor. For example, you can use nano:

```bash
nano ~/.zshrc
```
or

```bash
nano ~/.bashrc
```
Paste the code snippet at the end of the file.
Save the changes and exit the text editor. In nano, you can do this by pressing Ctrl + X, then Y to confirm saving, and Enter to exit.

### 2. Restart Shell/netcat

After saving the changes, restart your shell or source the file for changes to take effect.

```bash
source ~/.zshrc
```
or

```bash
source ~/.bashrc
```
You also have to install netcat-openbsd, when you have not already installed it on your system:

```bash
sudo apt install netcat-openbsd
```
You can also edit other terminal configuration files in a similar manner. For example, if you're using a different shell like fish, the configuration file might be .config/fish/config.fish. You can edit it using a text editor and follow similar steps to apply changes.

## Skills

[HelixVideo.mp4](https://github.com/PaulPoandl/Helix/assets/75140549/4d2c7e3a-704a-498e-a9a9-047a07538ba4)

Compression(clideo.com)/Voice(ElevenLabs - AI Voice Generator & Text to Speech)

### Function Commands

- **Play [song/band/video]:** Plays music or videos.
- **Open [website]:** Opens a specified website.
- **Tell me [time/date/joke]:** Provides the current time, date, or a random joke.
- **Who is/Who are/What is/What are [query]:** Searches for information about a person or thing on Wikipedia.
- **Search wikipedia for [query]:** Searches for information on Wikipedia.
- **Search browser for [query]:** Conducts a web search for the specified query.
- **linux command to [aim of command]:** Gives you a linux command with a specific aim.
- **run tcommand to [aim of command]:** Runs a linux command with a specific aim.
- And more...

### WolframAlpha Commands

- **Calculate [query]:** Performs complex calculations.
- **Solve [query]:** Solves mathematical problems.
- **Convert [unit1 to unit2]:** Converts between units.
- **Differentiate [function]:** Finds the derivative of a function.
- **Integrate [function]:** Finds the integral of a function.
- And more...

### OpenAI Commands

- **Generate [story/poem/idea/song/dialogue/scenario/joke/script/concept]:** Creates original content.
- **Explain [concept/phenomenon/term/theory/historical event/scientific theory/mathematical concept/technological trend]:** Explains complex topics.
- **Suggest [book/movie/recipe/activity/hobby/app/tool/destination/gift]:** Provides suggestions.
- **Create [recipe/plan/strategy/program]:** Helps in creating structured plans.
- And more...

### Gemini Commands

- **get [latest news/weather forecast/stock market update/crypto prices/sports scores/...]:** Helds you up-to-date.
- **get tech [latest tech news/newest software versions/latest CVEs/...]:** Helds you in the world of tech up-to-date.
- **brief [[CVE]/article [link to article]/video [link to youtube video]/book/music/album/...]:** To get a brief summary.
- **code [aim of the code and language]:** Codes you a program.
- And more...

## Good to know

Helix is also adept at understanding everyday conversation, making it versatile in its interactions.
Ensure that you don't include any of the aforementioned commands in your everyday interactions, as doing so
will trigger the function associated with that specific command.

You have the option to activate or deactivate OpenAI, Geimini and WolframAlpha. However, this means that the commands
related to WolframAlpha, Gemini and OpenAI will no longer be available as well as the weather (by deactivating Wolframalpha),
the commands 'run tcommand to' and 'linux command to' (by deactivating OpenAI) and Helix will not be capable of handling
all everyday commands as effectively (by deactivating Wolframalpha or/and OpenAI). Furthermore, the responses to these
everyday commands may not be as satisfactory.

You also have the option to change your location for weather information, your name (how Helix addresses you),
your Ascii preference (the way Helix sign is written at the dashboard) and the APIs for the AIs. To do so,
please enter the corresponding command.
When you change Ascii preference, you can choose between technical/simple/modern/default or random. Random is
a mix of all of them. To look up what Asciis every theme have, please open the corresponding python script for each topic.
You will find them in a folder called 'ascii_art'. in the helix folder. Optionally you can add your own art.
You can also activate or deactivate location (weather), Ascii (Helix sign) and events (calendar), but this will result in the
absence of this information on your dashboard (start screen), and the specific commands associated with them
will no longer function.

[Bildschirmaufzeichnung vom 2024-03-17, 01-08-00.webm](https://github.com/PaulPoandl/Helix/assets/75140549/1a08ce71-4912-439f-be35-f7804caddd85)

To activate or deactivate the ServerSocket functionality, you can use the corresponding command. When activated,
the ServerSocket feature allows you to communicate with Helix from multiple terminals using helix_command command,
like helix_command hello. However, to enable this feature globally, you'll need to add specific configuration
to your shell configuration file (e.g., bashrc or zshrc). Please refer to the GitHub page for detailed instructions.
Keep in mind that when the ServerSocket is deactivated, this functionality will no longer be available.
(Remember, when activated the terminal where Helix.py is running still has to be open in the background)
(Please keep in mind, that the command 'run tcommand to' does not work with ServerSocket, so it only can be
executed in the terminal where Helix.py is running, as well as the 'show' and 'change' commands.

To obtain the APIs for OpenAI, Gemini and WolframAlpha, visit their respective websites. For calendar functionality,
ensure you have both 'token.json' and 'credentials.json' files saved in the same directory as 'Helix.py'.
The 'credentials.json' file can be obtained from Google by following the instructions on their website.
After running Helix with Google Calendar for the first time, the token.json file will be automatically
generated in the same directory. However, you may already have the 'credentials.json' file obtained
from Google for Calendar. For detailed instructions on activating Google Calendar API and obtaining this file,
visit this link https://developers.google.com/calendar/api/quickstart/python.

When you get the warning 'Warning: unsupported distribution.', it means that you are not able to execute the command
'run tcommand to', because your package manager was not found, what is needed for 'run tcommand to update system'.
But beside that you can use Helix.py normally.

For assistance, feel free to reach out to us via email at bytegroovelabs@gmail.com or paul.poandl@gmail.com,
or find more information on our website at https://aicommandhub2.wordpress.com.

![Screenshot 2024-03-09 23 18 46](https://github.com/PaulPoandl/Helix/assets/75140549/2bbb4e37-2272-464d-b1fb-fab67e0cc18a)

## Check out the rating..

![giphy](https://github.com/user-attachments/assets/5ecce3c4-d312-4b20-ba5a-2ed45b661bf0)

Go to -> [medevel.com](https://medevel.com/personal-assistants-1830-p/#:~:text=20.%20Helix%20%2D%20Personal%20Assistant%20for%20Linux/GNU)

Source gif: https://giphy.com/gifs/season-9-the-simpsons-9x19-xT5LMrXqJoOzyuqj8Q
