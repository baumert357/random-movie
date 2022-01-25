#! python3
# -*- coding: utf-8 -*-

from random import sample

a = "It Follows"
b = "Norwegian Wood"
c = "Osaka Elegy"
d = "The New York Ripper"
e = "The House by the Cemetery"
f = "Ebriah, Horror of the Deep"
g = "Son of Godzilla"
h = "Boomerang Family"
i = "Hide and Seek"
j = "The Vanishing"

movies = [a, b, c, d, e, f, g, h, i, j]
randomMovies = sample(movies, 10)
index = 0

for m in randomMovies:
    index += 1
    print(str(index) + " - " + m)
