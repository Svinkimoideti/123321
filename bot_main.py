import discord
from bot_logic import gen_pass
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Привет' or 'привет'):
        await message.channel.send("Добрый день")
    if message.content.startswith('Пока'):
        await message.channel.send(":regional_indicator_g: :regional_indicator_o: :o2: :regional_indicator_d:  :regional_indicator_b: :regional_indicator_y: :regional_indicator_e: !")
    if message.content.startswith('Пароль 1'):
        await message.channel.send(gen_pass(1))
    if message.content.startswith('Пароль 2'):
        await message.channel.send(gen_pass(2))
    if message.content.startswith('Пароль 3'):
        await message.channel.send(gen_pass(3))
    if message.content.startswith('Пароль 4'):
        await message.channel.send(gen_pass(4))
    if message.content.startswith('Пароль 5'):
        await message.channel.send(gen_pass(5))
    if message.content.startswith('Пароль 6'):
        await message.channel.send(gen_pass(6))
    if message.content.startswith('Пароль 7'):
        await message.channel.send(gen_pass(7))
    if message.content.startswith('Пароль 8'):
        await message.channel.send(gen_pass(8))
    if message.content.startswith('Пароль 9'):
        await message.channel.send(gen_pass(9))
    if message.content.startswith('Пароль 10'):
        await message.channel.send(gen_pass(10))
    if message.content.startswith('Пароль 11'):
        await message.channel.send(gen_pass(11))
    if message.content.startswith('Пароль 12'):
        await message.channel.send(gen_pass(12))
    if message.content.startswith('Пароль 13'):
        await message.channel.send(gen_pass(13))
    if message.content.startswith('Пароль 14'):
        await message.channel.send(gen_pass(14))
    if message.content.startswith('Пароль 15'):
        await message.channel.send(gen_pass(15))
    if message.content.startswith('Пароль 16'):
        await message.channel.send(gen_pass(16))
    if message.content.startswith('Пароль 17'):
        await message.channel.send(gen_pass(17))
    if message.content.startswith('Пароль 18'):
        await message.channel.send(gen_pass(18))
    if message.content.startswith('Пароль 19'):
        await message.channel.send(gen_pass(19))
    if message.content.startswith('Пароль 20'):
        await message.channel.send(gen_pass(20))
    if message.content.startswith('Пароль 21'):
        await message.channel.send(gen_pass(21))
    if message.content.startswith('Пароль 22'):
        await message.channel.send(gen_pass(22))
    if message.content.startswith('Пароль 23'):
        await message.channel.send(gen_pass(23))
    if message.content.startswith('Пароль 24'):
        await message.channel.send(gen_pass(24))
    if message.content.startswith('Пароль 25'):
        await message.channel.send(gen_pass(25))
    if message.content.startswith('Пароль 26'):
        await message.channel.send(gen_pass(26))
    if message.content.startswith('Пароль 27'):
        await message.channel.send(gen_pass(27))
    if message.content.startswith('Пароль 28'):
        await message.channel.send(gen_pass(28))
    if message.content.startswith('Пароль 29'):
        await message.channel.send(gen_pass(29))
    if message.content.startswith('Пароль 30'):
        await message.channel.send(gen_pass(30))
    if message.content.startswith('Пароль 31'):
        await message.channel.send(gen_pass(31))
    if message.content.startswith('Пароль 32'):
        await message.channel.send(gen_pass(32))
    if message.content.startswith('Пароль 33'):
        await message.channel.send(gen_pass(33))
    if message.content.startswith('Пароль 34'):
        await message.channel.send(gen_pass(34))
    if message.content.startswith('Пароль 35'):
        await message.channel.send(gen_pass(35))
    if message.content.startswith('Пароль 36'):
        await message.channel.send(gen_pass(36))
    if message.content.startswith('Пароль 37'):
        await message.channel.send(gen_pass(37))
    if message.content.startswith('Пароль 38'):
        await message.channel.send(gen_pass(38))
    if message.content.startswith('Пароль 39'):
        await message.channel.send(gen_pass(39))
    if message.content.startswith('Пароль 40'):
        await message.channel.send(gen_pass(40))
    else:
        await message.channel.send(message.content)
client.run("")
