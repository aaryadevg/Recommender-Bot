import random
import sqlite3 as SQL

import Anime


def GetGenre(anime):
    """Gets Genre of the given anime

    Args:
        anime (string): the anime to find genre of

    Returns:
        [string]: [Returns the genre of the anime]
    """
    AnimeGenres = RunQuery(f'SELECT genre FROM Anime WHERE name = "{anime}" ')
    return AnimeGenres[0].Genre


def RunQuery(sqlStr):
    """Helper function to execute a SQL query

    Args:
        sqlStr (string): The SQL code to be executed

    Raises:
        Exception: Throws exception if there was an error in the SQL query

    Returns:
        [array[Anime]]: All the anime that were returned as a result of the SQL query
    """
    connection = SQL.connect('Anime.db')
    cr = connection.cursor()
    try:
        res = cr.execute(sqlStr)
        arr = list(res)
        r = Anime.Anime.FromQuery(arr)
        connection.commit()
        connection.close()
        return list(r)
    except:
        connection.commit()
        connection.close()
        raise Exception('Error in query')


def Get(genre):
    """Gets a random anime of the given genre

    Args:
        genre (string): Genre to lookup

    Raises:
        Exception: throws exception if the genre was not found

    Returns:
        [Anime object]: Object containing all the the properties of Anime table
    """
    fields = 'name, genre, type, episodes, rating, members'
    query = f'SELECT {fields} FROM Anime WHERE genre LIKE "%{genre}%" '
    result = RunQuery(query)
    if result is None:
        raise Exception(f"Genre not found")
    return random.choice(result)


def Search(name):
    """Searches for anime given the name of the anime
    Note:
        - Search is case insensitive

    Args:
        name (string): Name of anime to search for

    Raises:
        Exception: Throws an exception if the anime does not exist 

    Returns:
        Returns any anime where name is a sub string of Anime Name in Database 
        [Array[Anime]]: Array Containing all results from Database 
    """
    fields = 'name, genre, type, episodes, rating, members'
    query = f'SELECT {fields} FROM Anime WHERE name LIKE "%{name}%" '
    result = RunQuery(query)
    if result is None:
        raise Exception("Anime not Found")
    else:
        return result


def Random():
    """Gets a pseudo random anime

    Returns:
        [Anime]: A random anime
    """
    fields = 'name, genre, type, episodes, rating, members'
    query = f'SELECT {fields} FROM Anime WHERE genre IS NOT NULL'
    result = RunQuery(query)
    return random.choice(result)
