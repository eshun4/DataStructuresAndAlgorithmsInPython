#  Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.
import random

def random_choice(data):
    return data[random.randrange(0,len(data))]

print(random_choice([2,5,7,9,8,5,1]))