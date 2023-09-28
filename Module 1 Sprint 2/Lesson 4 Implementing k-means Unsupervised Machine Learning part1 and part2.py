from pprint import pprint
from math import fsum, hypot, sqrt
from typing import Iterable, Tuple, Sequence, Dict
from collections import defaultdict

points = [ 
    (10,20,30),
    (40,50,60),
    (70,80,90),
    (18, 15, 25),
    (11, 13, 14),
    (95,85,55),
]

def mean(data: Iterable[float]) -> float:
    data = list(data)
    return (fsum(data))/ len(data)


def dist(p,q):
    [x - y for x,y in zip(p,q)]

from functools import partial
print (pow(2,1))


def compute_centroids(groups):
    #'Compute the centroid of each group'
    return [tuple(map(mean, zip(*groups))) for group in groups]


def k_means (data, k = 2, iterations = 50): #not finished code
    data = list(data)
    centroids = sample(data,k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())

