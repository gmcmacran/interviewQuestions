###############################
# Overview
#
# Without using built a math
# library, calculate the square root
# of a number.
#
# Assume number is not negative.
# Comlex numbers out of scope.

# square root 4 -> 2
###############################


# Using newton's method
#   y ^ (1/2) = x       =>
#   y = x^2             =>
#   0 = x^2 - y         Can now apply newtons method!
#
#   f(x) = x^2 -y (where y is a constant given by user. Not y = f(x))
#   f'(x) = 2x
def calc_squre_root(y):
    
    x_t = y 
    tol = 1000000
    while(tol > .000001):
        fx = x_t**2 - y
        fprime = 2*x_t
        x_t_1 = x_t - fx/fprime # Newtom's method
        # print(x_t_1)
        
        tol = x_t_1 - x_t
        if tol < 0 :
            tol = -1 * tol
            
        x_t = x_t_1
        
    return(x_t_1)

# Test perfect squares
calc_squre_root(4)
calc_squre_root(9)
calc_squre_root(16)
calc_squre_root(25)
calc_squre_root(36)
calc_squre_root(49)
calc_squre_root(64)
calc_squre_root(81)
calc_squre_root(100)

# Test when number is it's own square root
calc_squre_root(1)

# Test numbers that are not perfect squares
calc_squre_root(2)
calc_squre_root(8)
