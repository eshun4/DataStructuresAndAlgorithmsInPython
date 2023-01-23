#  Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sum_of_all_odd_positives(n):
    add = 0
    for i in range(0, n+1):
        if(i**2 < n) and ((i**2) % 2 !=0):
            add += i **2
    return add

def sum_of_all_odd_positives_2(n):
    add = [i **2 for i in range(0, n+1) if(i**2 < n) and ((i**2) % 2 !=0)]
    # for i in range(0, n+1):
    #     if(i**2 < n) and ((i**2) % 2 !=0):
    #         add.append()
    return sum(add)

print(sum_of_all_odd_positives(5))
print(sum_of_all_odd_positives_2(5))

# for i in range(50,90,10):
#     print(i)
    
# for i in range(8,-9,-2):
#     print(i)
    
# print([2**i for i in range(9)])
