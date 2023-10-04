from collections import namedtuple, deque, defaultdict
import time
from itertools import islice

# namedtuple creates a tuple with categories
namedtuple('post', ['timestamp', 'user', 'something'])
# deque is similar to list, but sorts from newest to oldest
deque()
# we can create defaultdict with deque to accumulate the data
defaultdict(deque)

#How to know who is following who?

# we can have dict() which is Dict[User, Set[User]]. We have a user and the set of users he has
dict()          #type:  Dict[User, Set[User]]
# Set eliminates dublicates

#islice() can help to pick specific elemnts (not taking all)
islice() #can go with limit to specify how to slice


