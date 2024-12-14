## Overview
This Discord bot provides various functionalities, including sending welcome messages, random encouragements, virtual hugs, and support messages. It also logs errors and ensures smooth user interaction. This Discord bot is made for the Norwegian language.

---

## Features

### Core Features
- **Welcome Messages**: Sends a welcome message to new members upon joining.
- **Help Command (`!hjelp`)**: Displays a list of commands and their uses.
- **Encouragement (`!oppmuntring`)**: Sends a random encouraging message.
- **Hugs (`!klem`)**: Sends a virtual hug to the sender or a specified member.
- **Support (`!støtte`)**: Supports a mentioned member or chooses a random active participant to support.

### Error Handling
- Logs unexpected errors to `err.log` with timestamps for debugging.

---

## Requirements

### Libraries
Ensure the following Python libraries are installed:
```python
import os
import random
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime, timedelta, timezone
```
Install missing libraries using:
```bash
pip install discord.py python-dotenv
```

### Files
The bot depends on the following files:
1. **`.env`**: Stores your bot's token and guild name.
   - Example:
     ```env
     DISCORD_TOKEN=your-bot-token
     DISCORD_GUILD=your-guild-name
     ```
2. **`welcome_message.txt`**: Contains the welcome message for new members.
3. **`help_message.txt`**: Contains help information for commands.
4. **`encourage_message.txt`**: Stores lines of encouraging messages.
5. **`hug_message.txt`**: Contains hug messages.
6. **`hug_gifs.txt`**: (Optional) Stores URLs of hug GIFs.
7. **`support_phrases.txt`**: Contains phrases used to show support.
8. **`support_emojis.txt`**: Stores emojis used alongside support messages.
9. **`err.log`**: Logs runtime errors (created automatically).

---

## Setup and Usage

### Step 1: Clone the Repository
Clone or download the bot's repository to your local machine.

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Create a `.env` file in the root directory and add your bot token and guild name:
```env
DISCORD_TOKEN=your-bot-token
DISCORD_GUILD=your-guild-name
```

### Step 4: Add Required Files
Ensure all required text files (listed above) are present in the same directory as the bot script.

### Step 5: Run the Bot
Run the bot using:
```bash
python your_bot_script.py
```

---

## Commands

### General Commands
- **`!hjelp`**: Displays a list of commands and their descriptions.
- **`!oppmuntring`**: Sends a random encouraging message.
- **`!klem [member]`**: Sends a hug to the mentioned member or the sender themselves if no member is specified.
- **`!støtte [member]`**: Supports the mentioned member or a randomly selected active participant.

---

## Error Handling
Errors are logged in the `err.log` file. Example log entry:
```log
[14-12-2024 12:00:00] Unhandled message: Hello World
```

---

## Contributing
Feel free to fork the repository and submit pull requests for improvements or additional features.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

