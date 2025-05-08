from twitchio.ext import commands
import time
import random
import json

with open("settings.json", "r") as f:
    config = json.load(f)

# Replace with your own values
NICK = config["nickname"]
TOKEN = config["token"]
CHANNEL = config["channel"]
COOLDOWN = config["cooldown"]
PROBABILITY = config["probability"]

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TOKEN, prefix='!', initial_channels=[CHANNEL])
        self.last_timeout_time = 0  # timestamp of last timeout
        self.cooldown_period = COOLDOWN #15 * 60  # 15 minutes in seconds

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        if message.echo:
            return

        print(f'{message.author.name}: {message.content}')

        now = time.time()


        if (random.randint(1, PROBABILITY) == 1) and (now - self.last_timeout_time > self.cooldown_period):
            await message.channel.send(f"/timeout {message.author.name} 2")
            await message.channel.send(f"{message.author.name} has been banned (but not really since I'm not a mod)")

            print(f"Timed out {message.author.name}")
            self.last_timeout_time = now  # reset cooldown timer

        await self.handle_commands(message)

bot = Bot()
bot.run()
