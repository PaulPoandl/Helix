# Helix - Personal Assistant for Linux/GNU

![Helix](https://github.com/PaulPoandl/Helix/assets/75140549/55c5d33d-50f9-4a37-bfa7-90909e07b629)

Helix is a personal Assistant made for Linux/GNU. He supports a wide range of commands and functions, optional you can also
add an WolframAlpha API and OpenAI API for more features. 

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

## Skills

![Screenshot 2024-03-09 23 18 46](https://github.com/PaulPoandl/Helix/assets/75140549/2bbb4e37-2272-464d-b1fb-fab67e0cc18a)

### Function Commands

- **Play [song/band/video]:** Plays music or videos.
- **Talk to/talk/start [WolframAlpha Chat/OpenAI Chat]:** Initiates a conversation with the specified AI service.
- **Open [website]:** Opens a specified website.
- **Tell me [time/date/joke]:** Provides the current time, date, or a random joke.
- **Who is/Who are/What is/What are [query]:** Searches for information about a person or thing on Wikipedia.
- **Search wikipedia for [query]:** Searches for information on Wikipedia.
- **Search browser for [query]:** Conducts a web search for the specified query.
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

## Good to know

Helix is also adept at understanding everyday conversation, making it versatile in its interactions.
Ensure that you don't include any of the aforementioned commands in your everyday interactions, as doing so
will trigger the function associated with that specific command.

You have the option to activate or deactivate OpenAI and WolframAlpha. However, this means that the commands
related to WolframAlpha and OpenAI will no longer be available as well as the weather, and Helix will not be capable of handling
all everyday commands as effectively. Furthermore, the responses to these everyday commands may not be as satisfactory.

You also have the option to change your location for weather information, your name (how Helix addresses you),
and the APIs for the AIs. To do so, please enter the corresponding command.
You can also activate or deactivate location (weather) and events (calendar), but this will result in the
absence of this information on your dashboard (start screen), and the specific commands associated with them
will no longer function.

To obtain the APIs for OpenAI and WolframAlpha, visit their respective websites. For calendar functionality, 
ensure you have both 'token.json' and 'credentials.json' files saved in the same directory as 'Helix.py'. 
The 'credentials.json' file can be obtained from Google by following the instructions on their website.
After running Helix with Google Calendar for the first time, the token.json file will be automatically 
generated in the same directory. However, you may already have the 'credentials.json' file obtained 
from Google for Calendar. For detailed instructions on activating Google Calendar API and obtaining this file
visit this link https://developers.google.com/calendar/api/quickstart/python.

For assistance, feel free to reach out to us via email at bytegroovelabs@gmail.com or paul.poandl@gmail.com,
or find more information on our website at https://aicommandhub2.wordpress.com.

[Screen recording 2024-03-09 23.26.36.webm](https://github.com/PaulPoandl/Helix/assets/75140549/6dee5dd3-35a2-42e7-a21a-774f80120589)

