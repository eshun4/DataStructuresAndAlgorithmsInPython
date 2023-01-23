#  Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    sorted_data = sorted(data)
    return (sorted_data[0], sorted_data[-1])

print(minmax([2,4,3,1,6,8,7,9]))