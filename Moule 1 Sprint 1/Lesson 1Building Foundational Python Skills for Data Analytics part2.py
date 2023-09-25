

from random import *

seed(123)
random()

print('Gets a random number in that range:')
print(uniform(1000, 1100)) 

print('Same as above just with boundaries:')
print(triangular(1000, 1100)) 

print('Gauss variable where 100 is average and 15 is deviation:')
print(gauss(100, 15)) 

print('To simulate arrival times:')
print(expovariate(20)) 

from statistics import mean, stdev
print('Triangular statistics:')
data = [triangular(1000, 1100) for i in range(1000)] #1000 data points
print(mean(data))
print(stdev(data))

print('Uniform distribution statistics:')
data = [uniform(1000, 1100) for i in range(1000)] #1000 data points
print(mean(data))
print(stdev(data))

print('Gaussian distribution statistics:')
data = [gauss(100, 15) for i in range(1000)] #1000 data points
print(mean(data))
print(stdev(data))

print('Expo distribution statistics:')
data = [expovariate(20) for i in range(1000)] #1000 data points
print(mean(data))
print(stdev(data))

####Discrete distributions

from random import choice, choices, sample, shuffle

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']
print(choice(outcomes)) #one random choice
print(choices(outcomes, k= 10)) #specific number of choices

from collections import Counter

print(Counter(choices(outcomes, k=10))) #creates a dict of outcomes and how many times it happened
print(Counter(choices(outcomes, k=10000)))
print(Counter(choices(outcomes, [5,4,3,2,1], k=10000))) #puts weights on distribution

shuffle(outcomes) #doesnt work and shows 'none'



print(sample(outcomes, k=4))

print(sorted(sample(range(1,57), k = 6)))


####Relationships

#Below gives the same:
print(sample(outcomes, k=1)[0])
print(choice(outcomes))

shuffle(outcomes)
print(outcomes)
print(sample(outcomes, k= len(outcomes)))



