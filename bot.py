import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!funcoes':
            await message.channel.send(f'{message.author.name} as funções deste bot são as seguintes:{os.linesep}1-undock{os.linesep}2-minOverview{os.linesep}3-minBelt{os.linesep}4-warp{os.linesep}5-lockVeldspar{os.linesep}6-aproch{os.linesep}7-scan{os.linesep}8-scanedVeldpar5k{os.linesep}9-lock{os.linesep}10-ActivateMiners{os.linesep}11-fullOreHold')

#vai carregar a variavel do ficheiro .env
load_dotenv()
client = MyClient()
#correr o bot no discord e vai buscar a pass ao .env
client.run(os.getenv("TOKEN"))
