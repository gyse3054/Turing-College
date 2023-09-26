#Six roulette wheel spins
from random import *
from statistics import *
from collections import *

#18 red slots; 18 black slots and 2 green
print(choice(['red', 'red', 'red', 'black', 'black', 'black', 'green', 'green']))
print(choice(['red'] * 18 + ['black'] * 18 + ['green']  *2))
population = ['red'] * 18 + ['black'] * 18 + ['green']  *2
print(choice(population))

print([choice(population) for i in range(6)])
print(Counter([choice(population) for i in range(6)]))


print(Counter(choices(['black', 'red', 'green'], [18,18,2], k = 6))) #the best example. You can make a list of colours, defining how many of each should be and then it will show 6 random


#Deal 20 playing cards without replacement (16 tens, 36 low)
deck = Counter(tens = 16, low = 36) #take 52 cards
#print(deck)
deck = list(deck.elements()) #make them in a list
#print(deck)
#deal = sample(deck,20)
#print(Counter(deal))
deal = sample(deck,52) #sample all of them
remainder = deal[20:] #pick first twenty
print(Counter(remainder))

#5 or more head from 7 spins of a biased coin:

pop = ['head','tails']
wgt = [6,4]
cumwgt = [0.6, 1.00]

print(Counter(choices(pop, cum_weights = [0.60,1.00], k = 7))) #to count
print(choices(pop, cum_weights = [0.60,1.00], k = 7).count('head')) #to count
print(choices(pop, cum_weights = [0.60,1.00], k = 7).count('head') > 4) 

trial = lambda: choices(pop, cum_weights = [0.60,1.00], k = 7).count('head') > 4
print(trial())

n = 10000
print(sum(trial() for i in range(n))/ n)

#Compare to analytic approach

from math import factorial as fact
print(fact(4))


def comb(n, r):
    return fact(n) / fact(r) / fact(n-r)  # /gives float

print(comb(10,2))

def comb(n, r):
    return fact(n) // fact(r) // fact(n-r)  # /gives integer

print(comb(10,2))

ph = 0.6
print(ph ** 5* (1-ph) ** 2 * comb(7, 5)) #5 heads out of 7 spins probability
print(ph ** 6* (1-ph) ** 1 * comb(7, 6)) #6 heads out of 7 spins probability
print(ph ** 7* (1-ph) ** 0 * comb(7, 7)) #7 heads out of 7 spins probability

print(0.2612736 + 0.13063679999999997 + 0.027993599999999993) #theoretical result
print(sum(trial() for i in range(n))/ n) #empirical results

#Does the median of 5 fall in the middle of two quartiles?

n = 10000
trial = lambda: n//4 < median(sample(range(n),5)) <= 3*n//4
print(sum(trial() for i in range(n))/n) #Probability that median of 5 fall in the middle of two quartiles