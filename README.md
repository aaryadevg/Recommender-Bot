<img src="Rec bots Logo.png" alt="Logo Image" height="10%" width="10%">

# Recommender-Bot
A simple discord bot for recommending anime <br/>
uses a simple content based recommender system <br/>
This bot is as a learning project, to learn about: 
* recommender systems
* async methods 
* SQL 


## Dataset and Inspiration for the project:
* [Original dataset](https://www.kaggle.com/CooperUnion/anime-recommendations-database) by CooperUnion
* [inspired by this kernel](https://www.kaggle.com/diekanugraha/finding-similar-anime-by-genre) by diekanugraha

## Requirements
This discord bot is made in python and requires python 3.6+
you can install python [Here](https://www.python.org/downloads/)

along with python the discord bot uses a few other additional packages
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
* [Discord.py](https://discordpy.readthedocs.io/en/latest/)
* [Numpy](https://numpy.org/install/)

## Using the bot
First clone or download the source from GitHub

To use the Recommender-Bot you need to sign in to [Discord Devloper Portal](https://discord.com/developers/applications) 
and create a bot application

add the created bot to a server using<br/>`https://discordapp.com/oauth2/authorize?client_id={YOUR CLIENT ID}&scope=bot&permissions=0`

after this you should recieve a token for your bot add this token to your environment variable:

### MacOS
* Navigate to your Home directory<br/>`cd .`
* You may save a copy of the .bash_profile before editing 
* Open the .bash_profile file<br/>`nano .bash_profile`
* Export a variable called 'DISCORD_TOKEN'<br/>`export DISCORD_TOKEN={Your Discord token}`
* Save the .bash_profile and restart your terminal

*If you require any further assistance with this please check out [This article](https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255)*

### Windows 10
* Type "env" in the search
* Click on "Edit system environment variables"
* Click on "environment variables"
* Click on "New"
* Add "DISCORD_TOKEN" under the "Variable" column
* Add Your Discord token under the "Value" column
* Click on "Ok" to save changes

*If you require any further assistance with this please check out [This article](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/)*

**Unfortunetly I do not have much experience with a Linux based systems 🙁**

Now its finally time to run the bot 
Open up terminal or command prompt (on windows)
navigate to the directory where you saved the source for the bot
run the "Bot.py script" using <br/>`Python3 Bot.py` **On MacOS** <br/> `python Bot.py` **On Windows**
After everything is ready you should see a "ready" message printed to the terminal or command prompt

## Commands
|  **Command**         |**description**                                       | **Parameters**  | 
|----------------------|------------------------------------------------------|-----------------|
| `>recommend [genre]` | Recommends a random anime of the given genre         | `genre : string`|
| `>genres`            | Sends a List of all available genres in the Database | `None.`         |
| `>search [anime]`    | Searches for the given anime                         | `anime : string`|
| `>similar [anime]`   | Shows the 5 most similar anime to the given anime    | `anime : string`|
| `>random`            | Gets a random anime from the Database                | `None.`         |

## Contribution
Feel free to contribute to this project any contribution is very welcome and contributions are highly appreciated
* Thank you to Ashish Ghosalkar for the logo [Ashish Ghosalkar](https://aghosalkar.myportfolio.com/) 

**Todo:**
* Add more commands
* Make commands case in-sensitive
* Try using neural colaborative filltering for recommendation
* Build a scrapper to get info for latest anime
* Add a logo to the README


