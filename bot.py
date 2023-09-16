import discord
from discord.ext import commands

# Membuat bot dengan prefix "/"
bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def myping(ctx):
    # Menghitung ping bot ke server Discord
    latency = round(bot.latency * 1000)  # Dalam milidetik

    # Membuat pesan embed dengan custom warna kontol
    embed = discord.Embed(
        title="Your Ping:",
        description=f"{latency} ms",
        color=0x1400fd  # Warna biru tua
    )

    # Mengirim pesan embed ke channel yang sama dengan perintah
    await ctx.send(embed=embed)

# Ganti "YOUR_BOT_TOKEN" dengan token bot Anda
bot.run("YOUR_TOKEN")
