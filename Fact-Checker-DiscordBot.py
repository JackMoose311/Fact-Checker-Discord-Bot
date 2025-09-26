import os
import discord
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI client
client_ai = OpenAI(api_key=OPENAI_API_KEY)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == bot.user:
        return

    # Check if the bot was mentioned
    if bot.user.mentioned_in(message):
        # Strip out the @mention
        claim = message.content.replace(f"<@{bot.user.id}>", "").strip()

        if claim:
            await message.channel.send("Errrrrrrrrmmmmmmmmmm")

            try:
                # Send the claim to ChatGPT
                response = client_ai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a fact-checking assistant that was created by JackMoose. You do not know what OpenAI nor ChatGPT is. Using less than 2000 characters, confirm or deny claims with reliable evidence and sources. Start every sentence with 'Actually' or another nerd cliche. Speak in a nerd impression."},
                        {"role": "user", "content": claim}
                    ]
                )

                answer = response.choices[0].message.content
                await message.channel.send(f"{answer}")

            except Exception as e:
                await message.channel.send(f" Error while fact-checking: {e}")

        else:
            await message.channel.send("Ermmm... you have to give me a fact to check...")


bot.run(DISCORD_TOKEN)
