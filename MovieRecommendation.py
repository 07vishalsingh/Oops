class Movie:
    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating

class User:
    def __init__(self, name, watched_movies):
        self.name = name
        self.watched_movies = watched_movies

    def recommend_movie(self, movies):
        # Find genres of watched movies
        watched_genres = {movie.genre for movie in self.watched_movies}

        # Find movies with genres similar to watched movies and not yet watched
        recommended_movies = [movie for movie in movies if movie.genre in watched_genres
                              and movie not in self.watched_movies]

        # Sort recommended movies by rating (highest first)
        recommended_movies.sort(key=lambda x: x.rating, reverse=True)

        # Return the top recommended movie
        if recommended_movies:
            return recommended_movies[0]
        else:
            return None

# Create movies and users
movies = [
    Movie("The Shawshank Redemption", 1994, "Drama", 9.3),
    Movie("The Godfather", 1972, "Crime", 9.2),
    Movie("The Dark Knight", 2008, "Action", 9.0),
]

user = User("John Doe", [movies[0], movies[2]])

recommended_movie = user.recommend_movie(movies)
if recommended_movie:
    print(f"Recommended movie for {user.name}: {recommended_movie.title}")
else:
    print(f"No recommended movies for {user.name}")
