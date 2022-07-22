import numpy as np


# use numpy to output the mean, max, min, standard deviation
# sum of the rows, columns and elements in a 3x3 matrix
# input will contain 9 digits


def calculate(lst):
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    shapedArray = np.array(lst)
    lst3d = shapedArray.reshape(3,3)
    meanList = [lst3d.mean(axis=0).tolist(),lst3d.mean(axis=1).tolist(),np.mean(shapedArray)]
    maxList = [lst3d.max(axis=0).tolist(),lst3d.max(axis=1).tolist(),np.max(shapedArray)]
    minList = [lst3d.min(axis=0).tolist(),lst3d.min(axis=1).tolist(),np.min(shapedArray)]
    stdList = [lst3d.std(axis=0).tolist(),lst3d.std(axis=1).tolist(),np.std(shapedArray)]
    sumList = [lst3d.sum(axis=0).tolist(),lst3d.sum(axis=1).tolist(),np.sum(shapedArray)]
    varList = [lst3d.var(axis=0).tolist(),lst3d.var(axis=1).tolist(),np.var(shapedArray)]


    calculations = {
        "mean": meanList,
        "variance": varList,
        "standard deviation": stdList,
        "max": maxList,
        "min": minList,
        "sum": sumList

    }
    return print(calculations)

# Test Cases
calculate([0,1,2,3,4,5,6,7,8])
calculate([2,6,2,8,4,0,1,5,7])
calculate([9,1,5,3,3,3,2,9,0])

# ValueError: List must contain nine numbers.
calculate([2,6,2,8,4,0,1,])