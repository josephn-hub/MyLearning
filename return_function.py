import collections
from collections import Counter, namedtuple, deque
import random


def check_number(mode, other_number):
    if mode == 'Max':
        return lambda value: value < other_number
    if mode == 'Min':
        return lambda value: value > other_number


check = check_number('Max', 30)

print(check(35))


list_tuple = [ (1, "jobs"), (2, "john"), (3, "mark"), (4, "jack")]

for _, jobs in list_tuple:
    print(jobs)


c = Counter(cats=4, dogs=5)
print(list(c.elements()))

e= Counter({'a': 2, 'b': 3, 'c':4})
print(e.most_common(2))


d = Counter([1, 2, 3, 4,5])
f =[0, 1, 2, 3]

d.subtract(f)
print(d)

g = Counter(a=4 ,b=5, c=5)
h = {"a":4,"b":3}

g.update(h)
print(g)
# Named tuple
#
# point = namedtuple('Point', ['x', 'y'])
# point = Point(1,2)
# print(point)

# Tuple

tuple_example = (2,1,3,4)
x,y,z,e = tuple_example
print(x,y,z,e)

# deque
deq_example = deque([1,2,3,4], maxlen=5)
print(deq_example)
deq_example.append(2)
deq_example.extend([4])
print(deq_example)

deq_example.append(30)
print(deq_example)


def cards_example():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


number_returned = cards_example()
print(number_returned)

