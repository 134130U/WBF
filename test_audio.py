import os
from embedchain import App

# Create a bot instance
os.environ["OPENAI_API_KEY"] = "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"
elon_bot = App()

# Embed online resources
elon_bot.add("https://en.wikipedia.org/wiki/Elon_Musk")
elon_bot.add("https://www.forbes.com/profile/elon-musk")

# Query the bot
elon_bot.query("How many companies does Elon Musk run and name those?")
# Answer: Elon Musk currently runs several companies. As of my knowledge, he is the CEO and lead designer of SpaceX, the CEO and product architect of Tesla, Inc., the CEO and founder of Neuralink, and the CEO and founder of The Boring Company. However, please note that this information may change over time, so it's always good to verify the latest updates.
