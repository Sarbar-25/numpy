import numpy as np

marks = np.array([85,75,86,70,72])

#give 5 marks grace 

# grace = marks+5
# print(grace)

# #calculate average

# avg = np.average(marks)
# print(avg)

# #highest and lowest

# high = np.max(marks)
# low = np.min(marks)

# print(high)
# print(low)

for i in range(len(marks)):
    if marks[i] == 86:
        marks[i] = 89

print(marks)