#  Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):
    add= 0
    for i in range(0,n+1):
        if ((i**2) < n):
            add+= i**2
    return add

def sum_of_squares_2(n):
    add = []
    for i in range(0,n+1):
        if ((i**2) < n):
            add.append(i**2)
    return sum(add) 

print(sum_of_squares(5))
print(sum_of_squares_2(5))