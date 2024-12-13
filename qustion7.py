movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)]

def averageBudget (movies):
    sum =0
    for movie in movies:
        sum +=movie[1]
        
    return sum / len(movies)

print("The Average is",averageBudget(movies))


average = averageBudget(movies)

def moreThanAverage (movies):
    moreThanAverageFilms =[]
    for movie in movies:
        if movie[1] > average:
            moreThanAverageFilms.append(movie[1])
    return len(moreThanAverageFilms)

print("MoreThanAverage",moreThanAverage(movies))            

def movieNames (movies):
    movieNamesElement = []
    for movie in movies:
        movieNamesElement.append(movie[0])
    return movieNamesElement    

print("movieNames",movieNames(movies))