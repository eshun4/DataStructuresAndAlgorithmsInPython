# Convert any binary number to digits

def from_binary(k):
    str_number = str(k)
    n = len(str_number)
    number = 0
    index = 0
    for i in range(0,n):
        index-=1
        number += int(str_number[index]) * 2 ** i
    return number
    
# BitWise AND & Compares each digit in both binary digits and return 1 if both are set(=1)and 0 if both or either are clear(=0)
# print(from_binary(11001011))
# x = 0b11001011
# y = 0b10101101
# print(x)
# print(y)
# print(x & y)
# z = 0b101
# print(z & 0b100)