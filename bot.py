import discord
from discord.ext import commands

# Membuat bot dengan prefix "/" nOte : Bisa custom prefix :3
bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def myping(ctx):
    # Menghitung ping 
    latency = round(bot.latency * 1000)  # Dalam milidetik

    # Membuat  mssg embed dgn custom warna kontol note : Bebas mau warna apa SU
    embed = discord.Embed(
        title="Your Ping:",
        description=f"{latency} ms",
        color=0x1400fd  # Warna biru tua
    )

    # Mengirim pesan embed ke channel yang sama dengan perintah
    await ctx.send(embed=embed)

# Ganti "YOUR_TOKEN" dengan token bot KOE SU
bot.run("YOUR_TOKEN")
