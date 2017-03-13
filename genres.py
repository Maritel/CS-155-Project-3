import numpy as np
import matplotlib.pyplot as plt
from adjustText import adjust_text

files = ['animation.npy', 'fantasy.npy', 'scifi.npy']
titles = ['Projections: 10 Animated Movies',
          'Projections: 10 Fantasy Movies',
          'Projections: 10 Sci-Fi Movies']
proj_files = ['5-2-d-animation', '5-2-d-fantasy', '5-2-d-scifi']

proj = np.load('proj.npy')

movie_titles = np.load('data/movie_titles.npy')
movie_titles = [''.join(chr(c) for  c in title) for title in movie_titles]
movie_titles = [title.strip("\"") for title in movie_titles]
assert len(movie_titles) == proj.shape[1]

for k in range(len(files)):
    indices = np.load(files[k])

    movie_projs = proj[:, indices]
    movie_names = [movie_titles[i] for i in indices]

    fig, ax = plt.subplots()
    ax.scatter(movie_projs[0, :], movie_projs[1, :])
    texts = []
    for i in range(len(movie_names)):
        texts.append(ax.text(movie_projs[0][i],
                             movie_projs[1][i],
                             movie_names[i]))
    adjust_text(texts)

    plt.title(titles[k])
    plt.savefig(proj_files[k])