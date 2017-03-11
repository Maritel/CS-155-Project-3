import numpy as np

n_movies = 1682

rating_sums = np.zeros(n_movies)
num_ratings = np.zeros(n_movies)

data = np.load('data/data.npy')
for i in range(len(data)):
    movie_id = data[i][1] - 1
    rating = data[i][2]

    num_ratings[movie_id] += 1
    rating_sums[movie_id] += rating

avg_ratings = np.zeros(n_movies)
for i in range(len(avg_ratings)):
    if num_ratings[i] >= 10:
        avg_ratings[i] = rating_sums[i] / num_ratings[i]

best_rated_movies = np.argsort(avg_ratings)[-10:]
most_popular_movies = np.argsort(num_ratings)[-10:]

print('best rated: ' + str(best_rated_movies))
print('most popular: ' + str(most_popular_movies))

print([avg_ratings[i] for i in best_rated_movies])
print([num_ratings[i] for i in most_popular_movies])
