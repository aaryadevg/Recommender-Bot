import discord
from discord.ext import commands
import Database
import Recommender
import os

#Reads token from Token.txt
def ReadToken():
    token =  os.getenv('DISCORD_TOKEN')
    if token:
        return token
    else:
        raise Exception("Environment varible DISCORD_TOKEN not found") 

#Constants...
#Tokens are used to connect the script to the bot
TOKEN = ReadToken()
#Prefix is used before command
BOT_PREFIX = '>'

#creates bot
client = commands.Bot(command_prefix = BOT_PREFIX)

#Check if bot is ready and displays ready on standard output
@client.event
async def on_ready():
    print('ready')


#====================Commands============================
#Registers a command
#(type ">recommend [genre]" to use comand)
@client.command()
async def recommend(ctx, genre):
    anime = Database.Get(genre)
    print(anime)
    if anime is not None:
        await ctx.send(f"Try out {anime[0]}  anime and has an average rating of {anime[2]}")
    else:
        await ctx.send(f"Unfortunetly we could not find an anime like that, type '>genres' for more information")

#(type ">genres to use comand)
@client.command()
async def genres(ctx):
    GENRES = ['Sports', 'Shounen_Ai', 'Seinen', 'Shounen', 'Fantasy', 'Kids', 'Slice_of_Life', 'Mystery', 'Vampire', 'Shoujo', 'Sci-Fi', 'Game', 'Martial_Arts', 'Yuri', 'Adventure', 'Comedy', 'Magic', 'Romance', 'Mecha', 'Supernatural', 'Action', 'Horror', 'Parody', 'Shoujo_Ai', 'School', 'Josei', 'Psychological', 'Thriller', 'Harem', 'Military', 'Super_Power', 'Samurai', 'Police', 'Demons', 'Music', 'Space', 'Cars', 'Dementia', 'Hentai', 'Historical', 'Yaoi', 'Ecchi', 'Drama']
    msg = '\n'.join(GENRES)
    await ctx.send(msg)

#(type ">search [anime] to use comand)
@client.command()
async def search(ctx, *anime):
    anime = ' '.join(anime)
    res = Database.Search(anime)

    if len(res) != 0:
        out = f'Found: {len(res)} results\n'
        for row in res:
            out += "Name: {}\n\tGenre: {}\n\tType: {}\n\tEpisodes: {}\n\tAverage rating: {}\n".format(row[0],row[1],row[2],row[3],row[4])
        await ctx.send(out)
    else:
        await ctx.send(f"Oops, {anime} was not found")

#(type ">similar [anime name]" to use command
@client.command()
async def similar(ctx, *anime):
    anime = ' '.join(anime)
    if anime.strip() == '':
        await ctx.send(f"@{ctx.author} please specify an anime")
    else:
        res = Recommender.FindSimilarJaccard(anime, 5)
        if res == None:
            await ctx.send(f"Oops, seems like we could not find the anime called {anime}")
        else:
            msg = ''
            for row in res:
                msg += f"Try {row[0]} it has a similarity score of {row[1] * 100}%\n"
            await ctx.send(msg)
            
@client.command()
async def random(ctx):
    name, genre, rating = Database.Random()
    await ctx.send(f"{name}:\n\tgenre: {genre}\n\trating: {rating}")


client.run(TOKEN)
    
