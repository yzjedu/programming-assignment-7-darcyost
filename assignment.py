import csv

# Constants for column indices
DATE = 0
NAME = 1
BUDGET = 2
GROSS = 3
PROFIT = 4


# Function that loads movie data from a CSV file and returns it as a list of lists.
def load_movie_data(filename):
    f = open(filename, 'r')
    movieList = list(csv.reader(f))
    f.close()
    return movieList

# Function that adds a profit column to the movie data.
def add_profit_column(movie_data):
    for movie in movie_data:
        movie.append(float(movie[GROSS]) - float(movie[BUDGET]))
    return movie_data


# Function that prints the movies with the highest and lowest profits.
def print_min_and_max_profit(movie_data):
    max = movie_data[0]
    min = movie_data[0]
    for movie in movie_data:
        if movie[PROFIT] > max[PROFIT]:
            max = movie
        if movie[PROFIT] < min[PROFIT]:
            min = movie
    print("minimum = " + str(min))
    print("maximum = " + str(max))

# Function that prints detailed information about a movie.
def printDetailedInfo(movie):
    print("The movie " + str(movie[NAME]) + " was created in " + str(movie[DATE]) + " it had a budget of " + str(movie[BUDGET]) + " it had a gross profit of " + str(movie[GROSS]) + " It made a profit of " + str(movie[PROFIT]))



# Function that saves the movie data with the profit column to a new CSV file.
def save_movie_data(movie_data, output_filename):
    f = open(output_filename, "w")
    csv.writer(f).writerows(movie_data)

def main():
    # Write the code for the main function here and delete pass
    movies = load_movie_data("movies.csv")
    movies = add_profit_column(movies)
    print_min_and_max_profit(movies)
    save_movie_data(movies, "test.csv")
    printDetailedInfo(movies[0])

if __name__ == "__main__":
    main()