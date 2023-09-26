#Bootstraping to estimate the confidence interval on a sample of data

from statistics import mean, stdev
timings = [7.18,8.59,12.24,7.39,8.16,8.68,6.98,8.31,9.06,7.06,7.67,10.02,6.87,9.07]

#Build a 90% confidence interval
from random import choices


def bootstrap(data):
    return choices(data, k = len(data))

print(bootstrap(timings))

n = 10000
means = sorted(mean(bootstrap(timings)) for i in range(n)) #sorted arranges the data
print(n*0.05) #confidence interval is [-500;500]
print(f'The observed mean of {mean(timings)}')
print(f'Fall in a 90% confidence interval from {means[500]: .1f} to {means[-500] : .1f}')

#Final code
def bootstrap(data):
    return choices(data, k = len(data))
means = sorted(mean(bootstrap(timings)) for i in range(n)) #sorted arranges the data
print(f'Fall in a 90% confidence interval from {means[500]: .1f} to {means[-500] : .1f}')


#Statistical significance analysis and p-values

drug = [7.1,8.5,6.4]
placebo = [8.2,6.1,7.1]

from statistics import mean, stdev
import random

obs_dif = mean(drug) - mean(placebo)

comb = drug + placebo
nd = len(drug)
#shuffle(comb)

#If we reshuffle the participant is the new mean diff the same ir extreme than observed

def trial():
    random.shuffle(comb)
    drug = comb[:nd]
    placebo = comb[nd:]
    new_diff = mean(drug) - mean(placebo)
    return new_diff >= obs_dif

n = 10000
print(sum(trial() for i in range(n))/n)

#Single server queue simulation

from random import expovariate, gauss
from statistics import mean, median, stdev

average_arrival_interval = 5.6
average_service_time = 5.0
stdev_service_time = 0.0

num_waiting = 0
arrivals = [1,2,3,4,5,6,7,8,9,10,11,13,15] #list of when arrived
starts = [1.5,2.1,3.2,4,5,6,7.5,8.01,9.5,10.95,11,13,19]  #list of when started
arrival = service_end = 0.0

for i in range(20000):
    if arrival <= service_end:
        num_waiting += 1
        arrival + expovariate(1.0 / average_arrival_interval)
        arrivals.append(arrival)
    else:
        num_waiting -= 1
        service_start = service_end if num_waiting else arrival
        service_time = gauss(average_service_time, stdev_service_time)
        service_end = service_start + service_time
        starts.append(service_start)

waits = [start - arrival for arrival, start in zip(arrivals, starts)] #how many time people had to wait 
print(f' Mean wait: {mean(waits): .1f}. Stdev wait: {stdev(waits):.1f}.')
print(f' Median wait: {median(waits): .1f}. Max wait: {max(waits):.1f}.')



