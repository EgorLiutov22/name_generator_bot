def main():
    import discord
    import BasicGenerator

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        mm = (message.content).split()
        if message.author == client.user:
            return
        if len(mm) == 2 and mm[1].isdigit():
            try:
                b = BasicGenerator.BasicGenerator(int(mm[1]), mm[0])
                await message.channel.send(b.generate_nick())
            except:
                await message.channel.send("Ошибка")
        else:
            await message.channel.send("Введите имя и уровень странности")
    client.run('token')
