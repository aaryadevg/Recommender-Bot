import discord
from discord.ext import commands
import Database
import Recommender
import os
import AppSettings


# Reads token from Token.txt


def ReadToken():
    token = os.getenv('DISCORD_TOKEN')
    if token:
        return token
    else:
        raise Exception("Environment variable DISCORD_TOKEN not found")


# Constants...
# Tokens are used to connect the script to the bot
TOKEN = ReadToken()
# Prefix is used before command
BOT_PREFIX = '>'

# creates bot
client = commands.Bot(command_prefix=BOT_PREFIX)

# Check if bot is ready and displays ready on standard output


@client.event
async def on_ready():
    print('ready')


# ====================Commands============================
# Registers a command
# (type ">recommend [genre]" to use comand)
@client.command()
async def recommend(ctx, genre):
    anime = Database.Get(genre)
    print(anime)
    if anime is not None:
        await ctx.send(f"Try out \n{anime}")
    else:
        await ctx.send(f"Unfortunately we could not find an anime like that, type '>genres' for more information")

# (type ">genres to use comand)


@client.command()
async def genres(ctx):
    GENRES = ['Sports', 'Shounen_Ai', 'Seinen', 'Shounen', 'Fantasy', 'Kids', 'Slice_of_Life', 'Mystery', 'Vampire', 'Shoujo', 'Sci-Fi', 'Game', 'Martial_Arts', 'Yuri', 'Adventure', 'Comedy', 'Magic', 'Romance', 'Mecha', 'Supernatural', 'Action',
              'Horror', 'Parody', 'Shoujo_Ai', 'School', 'Josei', 'Psychological', 'Thriller', 'Harem', 'Military', 'Super_Power', 'Samurai', 'Police', 'Demons', 'Music', 'Space', 'Cars', 'Dementia', 'Hentai', 'Historical', 'Yaoi', 'Ecchi', 'Drama']
    msg = '\n'.join(GENRES)
    await ctx.send(msg)

# (type ">search [anime] to use comand)


@client.command()
async def search(ctx, *anime):
    anime = ' '.join(anime)
    res = Database.Search(anime)

    if len(res) != 0:
        out = f'showing {AppSettings.AppSettings["MaxSearchResults"]} of {len(res)} results\n'
        for i, row in enumerate(res[:AppSettings.AppSettings["MaxSearchResults"]],1):
            out += f"{i}. {row.Name}\n"
        await ctx.send(out)
    else:
        await ctx.send(f"Oops, {anime} was not found")

# (type ">similar [anime name]" to use command
@client.command()
async def similar(ctx, *anime):
    anime = ' '.join(anime)
    if anime.strip() == '':
        await ctx.send(f"@{ctx.author} please specify an anime")
    else:
        res = Recommender.FindSimilarJaccard(anime, AppSettings.AppSettings["MaxRecommended"])
        if res == None:
            await ctx.send(f"Oops, seems like we could not find the anime called {anime}")
        else:
            msg = ''
            for row in res:
                msg += f"Try {row[0]} it has a similarity score of {row[1] * 100}%\n"
            await ctx.send(msg)

# (Type >random to use command)
@client.command()
async def random(ctx):
    res = Database.Random()
    await ctx.send(f"{res}")

# Allows user to change settings of the bot
#(type >set [prop] [val] where prop is a string and value is float or int)
@client.command()
async def set(ctx, prop, val):
    if AppSettings.AppSettings.get(prop) == None:
        await ctx.send('Invalid property try >settings for help')
    else:
        if prop == "MinSimilartityScore":
            val =  abs(float(val))
        else:
            val = abs(int(val))
        
        AppSettings.AppSettings[prop] = val

#Allows user to view the settings of the bot
#(type >settings)
@client.command()
async def settings(ctx):
    out = ""    
    for i, key in enumerate(AppSettings.AppSettings.keys()):
        out += f"- {key}\n\t{AppSettings.Descriptions[i]}\n"

    await ctx.send(out)
        


client.run(TOKEN)
