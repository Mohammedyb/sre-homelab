# Exercise: Movie Schedule
#
# Look up a movie's showtime from a dictionary of current screenings.
#
# Concepts:
# - Dictionaries
# - Loops
# - User input
# - `.get()`
# - Conditional logic

# Store the current movie schedule in a dictionary.
current_movies = {"The Grinch": "11:00am",
                 "Rudolph": "1:00pm",
                 "Frosty the Snowman": "3:00pm",
                 "Lelo and Stitch": "5:00pm"}

# Print the available movie titles to the user.
print("We're currently shouing the following movies:")
for key in current_movies:
    print(key)

# Ask which movie the user wants and look up its showtime.
movie = input("What movie would you like the showtime for?\n")
showtime = current_movies.get(movie)

# Display the movie time when it is available.
if showtime == None:
    print("Request Movie isn't playing")
else:
    print(movie, "is playing at", showtime)
