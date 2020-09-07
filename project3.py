''' Define a function, called get_movies_from_tastedive. It should take one input parameter,
a string that is the name of a movie or music artist.
The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies,
not other kinds of media. It will be a python dictionary with just one key, ‘Similar’. '''

import requests_with_caching
import json

def get_movies_from_tastedive(mname):
    base_url = 'https://tastedive.com/api/similar'
    param = {}
    param["q"] = mname
    param["type"] = "movies"
    param["limit"] = 5
    
    this_page_cache = requests_with_caching.get(base_url, param)
    return json.loads(this_page_cache.text)

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")

'''Please copy the completed function from above into this active code window.
Next, you will need to write a function that extracts just the list of movie titles from a dictionary
returned by get_movies_from_tastedive. Call it extract_movie_titles.'''

import requests_with_caching
import json

def get_movies_from_tastedive(mname):
    base_url = 'https://tastedive.com/api/similar'
    param = {}
    param["q"] = mname
    param["type"] = "movies"
    param["limit"] = 5
    
    this_page_cache = requests_with_caching.get(base_url, param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(mdict):
    lst = []
    for movie in mdict["Similar"]["Results"]:
        lst.append(movie["Name"])
    return lst

extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))

'''Please copy the completed functions from the two code windows above into this active code window.
Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input.
It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list.
Don’t include the same movie twice.'''

import requests_with_caching
import json

def get_movies_from_tastedive(mname):
    base_url = 'https://tastedive.com/api/similar'
    param = {}
    param["q"] = mname
    param["type"] = "movies"
    param["limit"] = 5
    
    this_page_cache = requests_with_caching.get(base_url, param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(mdict):
    lst = []
    for movie in mdict["Similar"]["Results"]:
        lst.append(movie["Name"])
    return lst

def get_related_titles(movies_list):
    movie_lst = []
    for movie in movies_list:
        movie_lst.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(movie_lst))

get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])

'''Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search.
The function should return a dictionary with information about that movie.'''

import requests_with_caching
import json


def get_movie_data(mname2):
    base_url2 = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = mname2
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url2, params=param)

    return json.loads(this_page_cache.text)

get_movie_data("Venom")
get_movie_data("Baby Mama")

'''Please copy the completed function from above into this active code window.
Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer.
For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.'''

import requests_with_caching
import json

def get_movie_data(mname2):
    base_url2 = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = mname2
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url2, params=param)

    return json.loads(this_page_cache.text)

def get_movie_rating(mdict2):
    ranking = mdict2['Ratings']
    for item in ranking:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0

get_movie_rating(get_movie_data("Deadpool 2"))

'''Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window.
Define a function get_sorted_recommendations. It takes a list of movie titles as an input.
It returns a sorted list of related movie titles as output, up to five related movies for each input movie title.
The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function.
Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah'''

import requests_with_caching
import json

def get_movies_from_tastedive(mname):
    base_url = 'https://tastedive.com/api/similar'
    param = {}
    param["q"] = mname
    param["type"] = "movies"
    param["limit"] = 5
    
    this_page_cache = requests_with_caching.get(base_url, param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(mdict):
    lst = []
    for movie in mdict["Similar"]["Results"]:
        lst.append(movie["Name"])
    return lst

def get_related_titles(movies_list):
    movie_lst = []
    for movie in movies_list:
        movie_lst.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(movie_lst))

def get_movie_data(mname2):
    base_url2 = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = mname2
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url2, params=param)

    return json.loads(this_page_cache.text)

def get_movie_rating(mdict2):
    ranking = mdict2['Ratings']
    for item in ranking:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0

def get_sorted_recommendations(lst):
    new_lst = get_related_titles(lst)
    new_dict = {}
    for i in new_lst:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

