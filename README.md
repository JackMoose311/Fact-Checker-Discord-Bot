Fact-Checker Discord Bot!!!
A Discord bot that fact-checks user claims in real time using OpenAI’s GPT models.  
Mention the bot in any server, and it will respond with concise, evidence-based verification — always in a playful “nerdy” tone.

Features:
- Responds whenever it’s mentioned in a message  
- Sends claims to **OpenAI GPT-4o-mini** for fact-checking  
- Provides concise, evidence-backed answers  
- Secure API key handling with `.env` variables

Installation:
1. Clone the Repository ww

```bash
git clone https://github.com/your-username/Fact-Checker-Discord-Bot.git
cd Fact-Checker-Discord-Bot
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Create a .env file in the project root:
DISCORD_TOKEN=your_discord_token_here
OPENAI_API_KEY=your_openai_api_key_here

4. Run the bot:
```bash
python Fact-Checker-DiscordBot.py
```

Dependencies:
The project uses:
- discord.py>=2.3.0
- openai>=1.0.0
- python-dotenv

This bot is hosted on Discloud for 24/7 runtime.

~~~~INVITE THE BOT TO YOUR SERVER~~~~
https://discord.com/oauth2/authorize?client_id=1420869593089572876
