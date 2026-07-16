import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

RAMEN_EATING = [
    "🍜\n⬜⬜⬜⬜⬜",
    "🍜\n▓⬜⬜⬜⬜",
    "🍜\n▓▓⬜⬜⬜",
    "🍜\n▓▓▓⬜⬜",
    "🍜\n▓▓▓▓⬜",
    "🍜\n▓▓▓▓▓",
    "✨ Ramen eaten! ✨",
]

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='ramen 🍜'))

@bot.command(name='ramen')
async def spawn_ramen(ctx):
    """Spawn a ramen bowl"""
    embed = discord.Embed(title="🍜 Fresh Ramen Bowl", description="A delicious bowl appears!\n\nReact with 🥢 to eat!", color=0xFF6B6B)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🥢')

@bot.command(name='eat')
async def eat_ramen(ctx):
    """Eat the ramen with animation"""
    embed = discord.Embed(title="🍜 Eating Ramen...", description="Slurrrrrp! 😋", color=0xFF6B6B)
    msg = await ctx.send(embed=embed)
    
    for frame in RAMEN_EATING:
        embed.description = frame
        await asyncio.sleep(0.4)
        await msg.edit(embed=embed)
    
    embed.title = "😋 Delicious!"
    embed.description = "You enjoyed your ramen!\n\n+10 Happiness\n+5 Satisfaction"
    await msg.edit(embed=embed)

@bot.command(name='stats')
async def show_stats(ctx):
    """View your ramen stats"""
    embed = discord.Embed(title="🍜 Your Ramen Stats", color=0xFF6B6B)
    embed.add_field(name="Bowls Eaten", value="42", inline=True)
    embed.add_field(name="Happiness", value="210", inline=True)
    embed.add_field(name="Level", value="15", inline=True)
    embed.set_thumbnail(url=ctx.author.avatar.url if ctx.author.avatar else None)
    await ctx.send(embed=embed)

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return
    
    if reaction.emoji == '🥢':
        await reaction.message.channel.send(f"{user.mention} is eating the ramen! 🥢")
        await user.send(f"Yum! Here's an animated eating experience!")
        await user.send("\n".join(RAMEN_EATING[:3]))

bot.run(os.getenv('DISCORD_TOKEN'))
