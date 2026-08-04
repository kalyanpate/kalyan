# Module 1- Mid Test

import numpy as np
scores = np.array([
    [72, 85, 90, 60],
    [55, 48, 70, 80],
    [90, 92, 88, 95],
    [40, 55, 45, 50],
    [78, 80, 75, 82]
])

# Math, Science, English, History
# print(scores)
# Extract the scores of all students for the third subject (English) using 2D slicing.

print(scores[:,2])

# Use boolean masking to extract all score values from the entire array that are strictly above 80.
# ls= scores[scores> 80]
# print(ls)
print(scores[scores> 80])

# Replace every score that is below 50 with 0 (simulating a fail marker) using boolean masking assignment.
scores[scores < 50] =0
print(scores)

# Compute and print the overall mean score of the entire modified array (after step 3) using np.mean().
print(np.mean(scores))

