# Include modules
import pandas as pd
import numpy as np

# Function implementation
def function(x):
    return (x**2) - 4

# Point we are approaching
approachPoint = 2

steps = []
for i in range(1,7):
    steps.append(10 ** (-i))

# Getting x values from both left and right
xLeft = []
xRight = []
for i in steps:
    xLeft.append(approachPoint - i)
    xRight.append(approachPoint + i)

# Building the table
data = []
for xl, xr in zip(xLeft, xRight):
    fxl = function(xl)
    fxr = function(xr)
    data.append([xl, fxl, xr, fxr])

dataframe = pd.DataFrame(
        data,
        columns = ["x-(left)", "f(xLeft)", "x+(right)", "f(xRight)"]
)

# Final estimate implementation.
tolerance = 1e-5
leftDiff = np.abs(np.diff(dataframe["f(xLeft)"]))
rightDiff = np.abs(np.diff(dataframe["f(xRight)"]))

if np.all(leftDiff < tolerance) and np.all(rightDiff < tolerance):
    leftLimit = dataframe["f(xLeft)"].iloc[-1]
    rightLimit = dataframe["f(xRight)"].iloc[-1]
    
    if np.abs(leftLimit - rightLimit) < tolerance:
        print(f"Limit = {leftLimit + rightLimit / 2}")
    else:
        print("Left and right hand limits differ.")
else:
    print("Function does not converge with tolerance")