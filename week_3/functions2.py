
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# Write a function that takes a single movie and returns True if its IMDB score is above 5.5


def lol(movies_list):  #создаю функцию для работы с листом фильмов
    for movie in movies_list:    #здесь мы создаем функцию чтобы двигаться по каждому элементу
        imdb_score = movie.get("imdb") #извлекаем c помощью get imdb
        if imdb_score > 5.5:  #проверяем условие
            return True
    return False

result = lol(movies)

print(result)  #выводим используя функцию по отношению к списку фильмов





# Write a function that returns a sublist of movies with an IMDB score above 5.5.

def getHRfilms(movies_list):   #создаем функцию для получения заданной задачи 
    HRfilms = [movies for movies in movies_list if movies.get("imdb") > 5.5]  
    return HRfilms                      # |
                                        # |
                                        # |
HRfilms = getHRfilms(movies)            # |
print(HRfilms)                          # |
                                        # \/
# for movies in movies_list - проходится по каждому элементу списка
# movies.get("imdb") - достается значение imdb
# if movies.get("imdb") > 5.5 - проверяется условие





# Write a function that takes a category name and returns just those movies under that category.

def get_by_category(movies, category):
    category_movies = [movie for movie in movies if movies.get("category") == category]
    return category_movies

category_name = input()
action_movies = get_by_category(movies, category_name)
print(action_movies)







# Write a function that takes a category and computes the average IMDB score.

def average_imdb_by_category(movies, category):
    total_score = 0
    num_movies = 0
    for movie in movies:
        if movies.get(category) == category:
            num_movies += 1
            total_score += movie.get("imdb")
            
    average_score = total_score / num_movies
    return average_score

category = input()
last_average_score = average_imdb_by_category(movies, category)
print(last_average_score)





# Write a function that takes a list of movies and computes the average IMDB score.


def total_imdb_average(movies):
    total_score = 0
    num_movies = 0
    for movie in movies:
        num_movies += 1
        total_score += movie.get("imdb")
            
    average_score = total_score / num_movies
    return average_score


uwu_average_score = total_imdb_average(movies)
print(uwu_average_score)