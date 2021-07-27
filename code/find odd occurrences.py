######################################
# Overview
# 
# Given a list, return the numbers that
# occured an odd amount of times.
#
# 1, 2, 2, 5, 5, 5 -> 1, 5
######################################


# mylist = [1, 2, 2, 5, 5, 5]

def get_numbers_with_odd_occurrences(mylist):
    # group wise count:
    counts = dict()
    for e in mylist:
        if e in counts.keys():
            counts[e] = counts[e] + 1
        else:
            counts[e] = 1
            
    result = []
    for key in counts.keys():
        if counts[key] % 2 == 1:
            result.append(key)
            
    return(result)
            
        
get_numbers_with_odd_occurrences([1, 2, 2, 5, 5, 5]) == [1, 5]
get_numbers_with_odd_occurrences([1, 1, 2, 2, 5, 5, 5]) == [5]
get_numbers_with_odd_occurrences([1, 1, 2, 2, 5, 5, 5, 5]) == []
get_numbers_with_odd_occurrences([1, 2, 2, 2, 5, 5, 5]) == [1, 2, 5]
