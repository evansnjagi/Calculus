# Implementation of limit estimation using tables
# Modules
import numpy as np
import pandas as pd

# Function defination
def function(x):
    return (x ** x)  - 4

# x+ values approaching 2 from right hand side.
x_positive = [2.01, 2.001, 2.0001, 2.00001, 2.0000001]

# X- values approaching 2 from left hand side.
x_negative = [1.9, 1.99, 1.999, 1.9999, 1.99999]

# Compute the values
fxPValue = []
for value in x_positive:
    fxPValue.append(round(function(value), 4))
fxNValue = []
for value in x_negative:
    fxNValue.append(round(function(value), 4))

# Full lists
x = x_negative + x_positive
fxValue = fxNValue + fxPValue

# Creating the table
table = pd.DataFrame({
    "x-values": x,
    "f(x)-values": fxValue
})
print(table)