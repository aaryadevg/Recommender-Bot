import sqlite3 as SQL
import random
    
def GetGenre(anime):
    AnimeGenres = RunQuery(f'SELECT genre FROM Anime WHERE name = "{anime}" ')
    return AnimeGenres[0][0]

def RunQuery(sqlStr):
    connection = SQL.connect('Anime.db')
    print(connection)
    cr = connection.cursor()
    try:
        res = cr.execute(sqlStr)
        r = list(res)
        connection.commit()
        connection.close()
        return r
    except:
        print('Error in query')
        connection.commit()
        connection.close()
        return None

def Get(genre):
    query = f'SELECT name, genre, rating FROM Anime WHERE genre LIKE "%{genre}%" '
    res = RunQuery(query)
    #print(len(res))
    assert res is not None, f"Error in Query: {res}"
    return random.choice(res)

def Search(name):
    result = RunQuery(f'SELECT name, genre, type, episodes, rating, members FROM Anime WHERE name LIKE "%{name}%" ')
    assert result is not None, "Not Found"
    if len(result) > 10:
        return result[:10]
    else:
        return result

def Random():
    result = RunQuery('SELECT name, genre, rating FROM Anime WHERE genre IS NOT NULL')
    return random.choice(result)

#print(Search('black clover'))
