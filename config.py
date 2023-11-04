import os
from dotenv import load_dotenv
load_dotenv()

bot_token = os.getenv("TOKEN") # Set your bot token in the secrets file
bot_time = "%d/%b/%Y %H:%M:%S" # Time structure for logging
bot_color = 0xa6e3a1 # Embed color (#ffffff -> 0xffffff)

# Icons
member_icon = "https://i.imgur.com/DOP6Tei.png"
gear_icon = "https://i.imgur.com/1DI2lNu.png"