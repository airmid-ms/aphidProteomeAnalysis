## DATA MANIPULATION
# Q: what is correct etiquette in terms of preserving different versions of the df or overwriting it.
# Q: when does it make the most sense to remove empty columns and replace -inf with Nan

import math as math
import numpy as np
import pandas as pd

# load data
aphidProteinsRaw = pd.read_csv('aphidProteins.txt', sep = "\t")
aphidProteins = aphidProteinsRaw.copy()

# print(aphidProteins.columns)
# Q: can i easily remove the C:, N: and T: on the column headers??

# 1. remove reverse positives and potential contaminants
# If Reverse OR Potential contaminant = + then remove.
aphidProteins = aphidProteins.query("`Reverse` != '+' & `Potential contaminant` != '+'")

# 2. apply log squared transformation to any column including 'LFQ intensity'
# axis = 0 is rows, axis = 1 is columns.
# log2() is the function
# the index should be [col for col in aphidProteins.columns if 'LFQ intensity' in col]
aphidLFQ = [col for col in aphidProteins.columns if 'LFQ intensity' in col]
aphidProteins[aphidLFQ] = aphidProteins[aphidLFQ].apply(np.log2)

aphidProteins = aphidProteins.replace(-np.inf, np.nan) # remember -inf and Nan are values not a string.

# 3. remove empty and unnecessary columns
# ["N: Razor + unique peptides", "N: Unique peptides",
# "N: Unique + razor sequence coverage [%]", "N: Unique sequence coverage [%]",
# "N: Q-value", "N: Score", "T: Protein IDs", "T: Majority protein IDs", "T: id"]
aphidProteins = aphidProteins.drop(columns = ["Razor + unique peptides", "Unique peptides",
"Unique + razor sequence coverage [%]", "Unique sequence coverage [%]",
"Q-value", "Score", "Protein IDs", "Majority protein IDs", "id"])

# 4. Put SR and SS columns into different 'groups'.
#    Then remove rows where there isnt at least one group with all values/no NA values.
#    use grouper = [index specification]
##   find a more efficient way of doing this, wait till on github and use to exemplify version control/improvements.
## rename groups???
aphidSS = [col for col in aphidProteins.columns if 'SS' in col]
aphidSR = [col for col in aphidProteins.columns if 'SR' in col]

aphidProteins['countSS'] = aphidProteins[aphidSS].count(axis = 1)
aphidProteins['countSR'] = aphidProteins[aphidSR].count(axis = 1)

# if count of either SS or SR = 5 then keep, else drop. is loop necessary?
aphidProteins = aphidProteins.drop(aphidProteins[(aphidProteins.countSS < 5) &
                                                 (aphidProteins.countSR < 5)].index)





