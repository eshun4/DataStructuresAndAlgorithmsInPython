# Check if a number is even or odd

def is_even(n):
    if n & 1:
        return 'odd'
    else:
        return 'even'
    
print(is_even(46))