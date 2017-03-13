import numpy as np
import matplotlib.pyplot as plt
from adjustText import adjust_text

proj = np.load('proj.npy')


# just a test
# matrix should be 2 x n
def basic_scatterplot(matrix):
    plt.scatter(matrix[0, :],
                matrix[1, :],
                c='blue')
    plt.show()


def random_movies(matrix=proj, n_movies=10):
    movie_titles = np.load('data/movie_titles.npy')
    movie_titles = [''.join(chr(c) for  c in title) for title in movie_titles]
    movie_titles = [title.strip("\"") for title in movie_titles]
    assert len(movie_titles) == matrix.shape[1]

    # Pick <n_movies> random indices
    movie_indices = np.random.choice(a=len(movie_titles), size=n_movies)
    movie_projs = matrix[:, movie_indices]
    movie_names = [str(movie_titles[i]) for i in movie_indices]

    fig, ax = plt.subplots()
    ax.scatter(movie_projs[0, :], movie_projs[1, :])
    texts = []
    for i in range(len(movie_names)):
        texts.append(ax.text(movie_projs[0][i],
                             movie_projs[1][i],
                             movie_names[i]))
    adjust_text(texts)
    plt.title('Projections: 10 Random Movies')
    plt.savefig('5-2-a.png')


def ten_best():
    best_indices = [177, 49, 11, 602, 63, 113, 482, 168, 317, 407]
    movie_titles = np.load('data/movie_titles.npy')
    movie_titles = [''.join(chr(c) for  c in title) for title in movie_titles]
    movie_titles = [title.strip("\"") for title in movie_titles]
    assert len(movie_titles) == proj.shape[1]

    movie_projs = proj[:, best_indices]
    movie_names = [movie_titles[i] for i in best_indices]

    fig, ax = plt.subplots()
    ax.scatter(movie_projs[0, :], movie_projs[1, :])
    texts = []
    for i in range(len(movie_names)):
        texts.append(ax.text(movie_projs[0][i],
                             movie_projs[1][i],
                             movie_names[i]))
    adjust_text(texts)
    plt.title('Projections: 10 Best Movies')
    plt.savefig('5-2-c.png')


def ten_popular():
    popular_indices = [120, 299, 0, 287, 285, 293, 180, 99, 257, 49]
    movie_titles = np.load('data/movie_titles.npy')
    movie_titles = [''.join(chr(c) for  c in title) for title in movie_titles]
    movie_titles = [title.strip("\"") for title in movie_titles]
    assert len(movie_titles) == proj.shape[1]

    movie_projs = proj[:, popular_indices]
    movie_names = [movie_titles[i] for i in popular_indices]

    fig, ax = plt.subplots()
    ax.scatter(movie_projs[0, :], movie_projs[1, :])
    texts = []
    for i in range(len(movie_names)):
        texts.append(ax.text(movie_projs[0][i],
                             movie_projs[1][i],
                             movie_names[i]))
    adjust_text(texts)

    plt.title('Projections: 10 Most Popular Movies')
    plt.savefig('5-2-b.png')

random_movies(proj, 10)
ten_best()
ten_popular()