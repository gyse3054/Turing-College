
#How to import CSV file
with open('file.csv', encoding= 'UTF-8') as f:
    print(f.read())


#How to play with data. Tuple unpacking. Various things with data.
import csv
from collections import namedtuple, defaultdict, Tuple, Counter
from pprint import pprint
import glob
from typing import NamedTuple
from kmeans import k_means, assign_data

Senator = NamedTuple('Senator', [('name', str),('party', str),('state', str)]) #IS KEY
VoteValue = int
VoteHistory = Tuple[VoteValue, ...]

#Load votes which were arranged by topic and accumulate votes by senator
vote_value = {'Yea':1, 'Nay': -1, 'Not voting': 0}          #type: Dict[str, VoteValue]
accumulated_record = DefaultDict(list)

for filename in glob.glob('file.csv'):
    with open('file.csv', encoding= 'UTF-8') as f:
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, distict, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote) #this is list

# Transform the record into a plain dict that maps to tuple of votes
record = {senator: tuple(votes) for senator, votes in accumulated_record.items()}       #type: Dict[Senator, VoteHistory]

pprint(accumulated_record)   


#Use k-means to locate the cluster (common paterns) centroids (middle of the clusters) from pattern of votes. Assing each senator to the nearest cluster.

centroids = k_means(record.values(), k = 3)
clustered_votes = assign_data(centroids, record.values())

#Build a reverse mapping from a vote history to a list of senators who voted that way

votes_to_senators = defaultdict(list)                                                   #type: defaultdict[VoteHistory, list[Senator]]
for senator, VoteHistory in record.items():
    votes_to_senators[VoteHistory].append(senator)

NUM_SENATORS = 100
assert sum(len(cluster) for cluster in votes_to_senators.values()) == NUM_SENATORS

#Display the clusters and the members (senators) of each cluster
for i, votes_in_cluster in enumerate(clustered_votes.values(), start = 1):
    print(i)
    party_totals = Counter()
    for votes in set(votes_in_cluster): #set removes dublicate
        for senator in votes_to_senators[votes]:
            party_totals[senator.party] += 1
            print(senator)
    print(party_totals)






