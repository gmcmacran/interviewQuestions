###############################################
# Overview
#
# Given IDs, count how many occurences there
# are of each value.
#
# Example 1:
# A, B, C -> A: 1, B: 1, C: 1
#
# Example 2: 
# A, A, A, C -> A: 3, C 1
###############################################

# %%
IDs = ['A', 'A', 'A', 'B', 'B', 'C']

# %% Base python
def count_occurences(IDsArg):
    result = {}

    for i in IDsArg:
        if i in result.keys():
            result[i] = result[i]+1
        else:
            result[i] = 1
    
    return result

count_occurences(IDs)

# %% using pandas
import pandas as pd
data = {'ID':IDs}
DF = pd.DataFrame(data = data)
DF['one'] = 1
DF.groupby(['ID'], as_index=False)['one'].sum()

# %%
DF.groupby(['ID'], as_index=False).size()

# %%
