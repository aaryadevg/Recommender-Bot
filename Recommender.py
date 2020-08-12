import pandas as pd
import numpy as np
import sqlite3
import re


def Encode(genre):
    ENCODING = {'Action': 0, 'Slice of Life': 1, 'Sports': 2, 'Mystery': 3, 'Game': 4, 'Dementia': 5, 'Magic': 6, 'Kids': 7, 'Space': 8, 'Shoujo': 9, 'Josei': 10, 'Yaoi': 11, 'School': 12, 'Shounen': 13, 'Seinen': 14, 'Romance': 15, 'Music': 16, 'Harem': 17, 'Martial Arts': 18, 'Police': 19, 'Hentai': 20, 'Shoujo Ai': 21, 'Shounen Ai': 22, 'Historical': 23, 'Horror': 24, 'Yuri': 25, 'Super Power': 26, 'Mecha': 27, 'Vampire': 28, 'Adventure': 29, 'Ecchi': 30, 'Supernatural': 31, 'Fantasy': 32, 'Military': 33, 'Parody': 34, 'Sci-Fi': 35, 'Thriller': 36, 'Comedy': 37, 'Cars': 38, 'Psychological': 39, 'Demons': 40, 'Samurai': 41, 'Drama': 42}
    genres = genre.split(', ')
    vector = np.zeros(len(ENCODING.keys()), dtype = int)
    for idx in genres:
        vector[ENCODING[idx]] = 1
    #print(len(vector))
    return vector

def jaccard_score(a, b):
    m11, m01, m10 = 0,0,0
    for idx in range(len(a[0])):
        if (a[0][idx] == 1)  and (b[idx] == 1):
            m11 += 1
        elif (a[0][idx] == 0) and (b[idx] == 1):
            m01 += 1
        elif (a[0][idx] == 1) and (b[idx] == 0):
            m10 += 1

    j = m11 / (m11+m01+m10)
    #print(j)
    return j
    
def FindSimilarJaccard(a, k):
    try:
        con = sqlite3.connect("Anime.db")
        anime_df = pd.read_sql_query('SELECT name, genre from Anime WHERE genre IS NOT NULL ', con)
        anime_df['genre'] = anime_df['genre'].apply(lambda genre : Encode(genre))
        anime = anime_df[anime_df['name'] == a]
        anime_df['result'] = anime_df['genre'].apply(lambda x : jaccard_score(anime['genre'].to_numpy() , x))

        res = anime_df.sort_values('result', ascending = False)
        out = res[['name', 'result']]
        regex = f'^{a}'
        filtered = []
        for i in out.values.tolist():
            if len(filtered) == k:
                return filtered
            else:
                if re.search(regex, i[0]) == None:
                    filtered.append(i)
                    
    
        con.close()
    
        #return out.values.tolist()
    except:
        return None
    


#print(FindSimilarJaccard('One Piece', 5))
