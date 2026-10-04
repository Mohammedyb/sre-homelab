# Make dictionary of current movies
current_movies ={"The Grinch": "11:00am",
                 "Rudolph": "1:00pm",
                 "Frosty the Snowman": "3:00pm",
                 "Lelo and Stitch" : "5:00pm"}

# Print out which movies are currently showing
print("We're currently shouing the following movies:")
for key in current_movies:
    print(key)
    
# Allow user to input the title of the movie they'd like
movie = input("What movie would you like the showtime for?\n")

# Add showtime variable
showtime = current_movies.get(movie)

# Print out the results
if showtime == None:
    print("Request Movie isn't playing")
else:
    print(movie, "is playing at", showtime)    
