# NumPy Practice 🧮

This repository contains my practice programs while learning **NumPy in Python**.

I am currently focusing on understanding NumPy fundamentals before moving deeper into Pandas, Machine Learning, and other AI/ML concepts.

## 📚 What I Have Practiced

- Creating NumPy arrays
- 1D arrays
- 2D arrays / matrices
- Adding values to arrays
- Calculating average
- Finding maximum and minimum values
- Array indexing
- Replacing values using indexes
- Basic array operations
- Using loops with NumPy arrays
- Understanding the difference between values and indexes

## 🧪 Current Practice Example

One of my exercises uses student marks:

```python
import numpy as np

marks = np.array([67, 89, 76, 86, 70])

# Add 5 marks
grace = marks + 5
print(grace)

# Calculate average
avg = np.average(marks)
print(avg)

# Find highest and lowest marks
high = np.max(marks)
low = np.min(marks)

print("Highest:", high)
print("Lowest:", low)

# Replace 86 with 89
for i in range(len(marks)):
    if marks[i] == 86:
        marks[i] = 89

print(marks)
