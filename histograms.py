
import numpy as np 
import operator
import matplotlib
import matplotlib.pyplot as plt


def get_points():
	# Returns data from data.txt and movies.txt

	# takes the data from data.txt file
	# Format: [User ID, Movie ID, Rating]
	# Data type: Int
	data = np.genfromtxt("data\data.txt",delimiter="	",dtype=int)

	# takes the data from movie.txt file
	# Format: [Movie ID]
	# Data type: String
	movie_ids = np.genfromtxt("data\movies.txt",delimiter="	",usecols=(0),dtype=int)

	# Format: [Movie Title]
	movie_titles = np.genfromtxt("data\movies.txt",delimiter="	",usecols=(1),dtype=str)

	# Format: [Unknown, Action, Adventure, Animation, Childrens, Comedy, Crime, Documentary, 
	# 		   Drama, Fantasy, Film-Noir, Horror, Musical, Mystery, Romance, Scifi, Thriller, War, Western]
	# Data type: Int
	movie_genres =  np.genfromtxt("data\movies.txt",delimiter="	",usecols=range(2,21),dtype = int)

	# Format: Everything Combined
	# Data type: String
	movie_data = np.genfromtxt("data\movies.txt",delimiter="	",dtype = str)

	# Returns all data
	return data, movie_ids, movie_titles, movie_genres, movie_data



def plot_stuff(data, title, percentage = 1):
	# Takes in dataset, title, and percentage boolean
	# Plots histogram of dataset

	# Initializes subplots
	fig, ax = plt.subplots()
	# Sets bins with offset of 0.5 to make tick marks align
	bins = [0.5,1.5,2.5,3.5,4.5,5.5]
	# Centers of the aligned bins
	bin_centers = 0.5 * np.diff(bins) + bins[:-1]
	# Creates the histogram 
	counts, bins, patches = ax.hist(data, bins = bins, normed = percentage, rwidth = 0.75, histtype='bar', color= 'orange')
	# Labels each bar with data
	for count, x in zip(counts, bin_centers):
		# If the percentage boolean = True, then prints percentages, otherwise prints actual counts
		if percentage:
			percent = '%0.0f%%' % (100 * float(count) / counts.sum())
			print percent
			ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),	xytext=(0, -32), textcoords='offset points', va='top', ha='center')
		else:
			ax.annotate(str(int(count)), xy = (x, 0), xycoords= ('data', 'axes fraction'), xytext = (0, -32), textcoords = 'offset points', va='top', ha = 'center')

	# Creates a legend
	plt.legend()
	# Sets x and y axis labels
	plt.xlabel("Rating")
	if percentage:
		plt.ylabel("Proportion of Ratings")
	else:
		plt.ylabel("Number of Ratings")
	# Sets title of the histogram
	plt.title(title)
	# Show the histogram
	plt.show()



def plot_dataset():
	# Plots the MovieLens Dataset
	# Retreives data 
	data, movie_ids, movie_titles, movie_genres, movie_data = get_points()	
	# Plots data once with percentages and once with actual counts
	plot_stuff(data[:,2]-0.5, 'MovieLens Dataset Ratings', 1)
	plot_stuff(data[:,2]-0.5, 'MovieLens Dataset Ratings', 0)



def most_popular():
	# Plots the MovieLens Dataset
	# Retreives data 
	data, movie_ids, movie_titles, movie_genres, movie_data = get_points()
	# Finds number of unique counts
	unique, counts = np.unique(data[:,1], return_counts=True)
	# Makes a dictionary to map ratings and counts
	unique_dict = dict(zip(unique, counts))
	# Sorts dictionary and returns in a form of a tuple
	sorted_dict = sorted(unique_dict.items(), key=operator.itemgetter(1))
	# We want the 10 best (i.e., the last 10 in the sorted list)
	ten_best = sorted_dict[-10:]
	# For each movie in the list of ten best, 
	# 	add every rating for the movie in the dataset to a list of ratings
	ratings = []
	for i in range(len(ten_best)):
		mid = ten_best[i][0]
		for j in range(len(data)):
			if data[j][1] == mid:
				ratings.append(data[j][2])

	# Plots data once with percentages and once with actual counts
	plot_stuff(np.asarray(ratings)-0.5, '10 Most Popular Movies Dataset Ratings', 1)
	plot_stuff(np.asarray(ratings)-0.5, '10 Most Popular Movies Dataset Ratings', 0)




def most_best():
	# Plots the 10 Best Movies of Dataset
	# Finds the movies with the best average ratings
	# Only includes movies with more than 10 ratings
	# Retreives data 
	data, movie_ids, movie_titles, movie_genres, movie_data = get_points()
	n_movies = 1682
	# Initializes sums and counts of ratings
	rating_sums = np.zeros(n_movies)
	num_ratings = np.zeros(n_movies)
	# Iterate through each data point to find the ratings and update the arrays
	for i in range(len(data)):
	    movie_id = data[i][1] - 1
	    rating = data[i][2]

	    num_ratings[movie_id] += 1
	    rating_sums[movie_id] += rating

	# Initializes array of averages
	avg_ratings = np.zeros(n_movies)
	# Calculates averages
	for i in range(len(avg_ratings)):
	    if num_ratings[i] >= 10:
			avg_ratings[i] = rating_sums[i] / num_ratings[i]
	
	# We want the 10 best (i.e., the last 10 in the sorted list)
	best_rated_movies = np.argsort(avg_ratings)[-10:]

	# For each movie in the list of ten best, 
	# 	add every rating for the movie in the dataset to a list of ratings
	ratings = []
	for i in range(len(best_rated_movies)):
		mid = best_rated_movies[i]
		print mid
		for j in range(len(data)):
			if data[j][1] == mid:
				ratings.append(data[j][2])


	# Plots data once with percentages and once with actual counts
	plot_stuff(np.asarray(ratings)-0.5, '10 Best Movies Dataset Ratings', 0)
	plot_stuff(np.asarray(ratings)-0.5, '10 Best Movies Dataset Ratings', 1)


def most_favorite():
	# Plots 3 Favorite Genres (Separate graphs)
	# Retreives data 
	data, movie_ids, movie_titles, movie_genres, movie_data = get_points()

	# Favorite Genres (Animation, Fantasy, Scifi)
	favorites = [5,11,17]
	# Initialize empty lists for Movie IDs
	animation = []
	fantasy = []
	scifi = []
	# Initliaize empty lists for Ratings
	animation_ratings = []
	fantasy_ratings = []
	scifi_ratings = []
	# Fills movie ID lists for each movie
	for x in movie_data:
		if int(x[5]) == 1:
			# if len(animation) <= 10:
			animation.append(int(x[0])-1)
		if int(x[11]) == 1:
			# if len(fantasy) <= 10:
			fantasy.append(int(x[0])-1)
		if int(x[17]) == 1:
			# if len(scifi) <= 10:
			scifi.append(int(x[0])-1)

	# Fills Ratings lists for each movie		
	for x in animation:
		for j in range(len(data)):
			if data[j][1] == x:
				animation_ratings.append(data[j][2])
	for x in fantasy:
		for j in range(len(data)):
			if data[j][1] == x:
				fantasy_ratings.append(data[j][2])
	for x in scifi:
		for j in range(len(data)):
			if data[j][1] == x:
				scifi_ratings.append(data[j][2])


	# Plots data once with percentages and once with actual counts for each genre 

	plot_stuff(np.asarray(animation_ratings)-0.5, 'Animation Movies Dataset Ratings', 0)
	plot_stuff(np.asarray(animation_ratings)-0.5, 'Animation Movies Dataset Ratings', 1)

	plot_stuff(np.asarray(fantasy_ratings)-0.5, 'Fantasy Movies Dataset Ratings', 0)
	plot_stuff(np.asarray(fantasy_ratings)-0.5, 'Fantasy Movies Dataset Ratings', 1)

	plot_stuff(np.asarray(scifi_ratings)-0.5, 'SciFi Movies Dataset Ratings', 0)
	plot_stuff(np.asarray(scifi_ratings)-0.5, 'SciFi Movies Dataset Ratings', 1)


def main():
	# Run everything
	plot_dataset()
	most_popular()
	most_favorite()      
	most_best()