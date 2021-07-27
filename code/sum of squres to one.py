######################################
# Overview
# 
# Does the sum of the squares of each
# digit eventually sum to one?
#
# Example of true case
# 19 -> 1^2 + 9^2 -> 82
# 82 -> 8^2 + 2^2 -> 68
# 68 -> 6^2 + 8^2 -> 100
# 100 -> 1^2 + 0^2 + 0^2 -> 1
#
# Example of false case
# 4 -> 4^2 -> 16
# 16 -> 1^2 + 6^2 - > 37
# 37 -> 3^2 + 7^2 -> 58
# 58 -> 5^2 + 8^2 -> 89
# 89 -> 8^2 + 9^2 -> 145
# 145 -> 1^2 + 4^2 + 5^2 -> 42
# 42 -> 4^2 + 2^2 -> 20
# 20 -> 2^2 + 0^2 -> 4 (cyclical)
######################################
import math

# x = 19

def check(x, prev_x = []):
    # print(x)
    
    x100 = math.floor(x / 100)
    x10 = math.floor(x / 10)
    x10 = x10 % 10
    x1 = x % 100
    x1 = x1 % 10
    
    SS = x100**2 + x10**2 + x1**2
    
    if (SS == 1):
        return True
    elif SS in prev_x:
        return False
    else:
        prev_SS = prev_x + [SS]
        return check(SS, prev_SS)
    

check(19)
check(4)



