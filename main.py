import discord # pip install discord

from config import Security_1PSID, discord_token # config.py is manually created file.

from bardapi import Bard # pip install bardapi

token = discord_token
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        try:
          print(f'Message from {message.author}: {message.content}')
          if self.user!= message.author:
              if self.user in message.mentions:
                bard = Bard(Security_1PSID, timeout=60)
                response = bard.get_answer(message.content)['content']
                channel = message.channel
                await channel.send(response)
                
        except Exception as e:
          print(e)
            
      
# Creating Objects and Specifying Var
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)