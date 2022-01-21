import os
import discord
import random
from datetime import datetime

client = discord.Client()


@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel})')

        if message.author == client.user:
                return
        if message.channel.name == 'general':
            if user_message.lower() == '!list':
                await message.channel.send('!seenmatt = Will tell you the last time TheBestOffTank made a game night.')
                await message.channel.send('!status = Check the availability of TheBestOffTank.')
                return

        if message.channel.name == 'general':
            if user_message.lower() == '!seenmatt':
                date1 = datetime.now()
                date2 = datetime(day=5, month=1, year=2022)
                timedelta = date1 - date2
                await message.channel.send('Matt White has not been seen in: {}'.format(timedelta))
                return

        if message.channel.name == 'general':
            if user_message.lower() == '!status':
                await message.channel.send('Matt White will not be online gaming again in 2022.')
                return


my_secret = os.environ['token']
client.run(my_secret)
