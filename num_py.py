#in this we will write about numpy
import numpy as np

## Convert a Python list to array
arr = np.array([[1,2,3,4,5],[0,9,8,7,6]])
print(arr)

#Creating a matrix of zeros
zeros = np.zeros((2,3))
print(zeros)

#creating ones
ones =  np.ones((3,3))
print(ones)

# Array with steps: [0, 2, 4, 6, 8]
arr_steps = np.arange(1,20,5)
print(arr_steps)

# 5 evenly spaced numbers between 0 and 1
spaced_arr = np.linspace(1,2,10,endpoint=False)
print("\n",spaced_arr)

# 3x3 Identity matrix
iden_matrix =np.eye(5)
print("\n",iden_matrix)

# 2. Inspecting Array Properties
# Inspecting array structure, size, or data types.

#shape
arr_shape = np.shape(arr)
print(arr_shape)

print(arr.ndim)    # Output: 2 - Number of dimensions
print(f"The size of the array is {arr.size}")
print(f"The dtype of the array is {arr.dtype}")

# 3. Reshaping & Restructuring
# Changing layout and structure without altering data.

a = np.arange(10)
reshaped = a.reshape(5,2)
print(f"Array Reshaped: {reshaped}")
flattened = reshaped.flatten()
print(flattened)

#transpose method flip axes of the matrix
transposed = reshaped.transpose()
print(f"The transpose of the array is {transposed}")

# 4. Mathematical & Statistical Operations
# Summarizing data or calculating statistics.
data = np.array([[1,2,4],[3,5,6]])
print(data.sum())

print(f"The mean of the data is: {data.mean()}")
print(f"The max of the data is: {data.max()}")
print(f"The min of the data is: {data.min(axis= 0)}")
print(f"The argmax of the data is: {data.argmax()}") #return the max 


#5. Conditional & Logical Selection
# Filtering data or finding elements matching conditions.
scores = np.array([55,66,77,88,99])
passed = np.where(scores >= 70, "Pass", "Fail")
print(passed)

high_score = scores[scores >70]
print(high_score)

# Combining and splitting arrays
arr1 = np.array([[10,20,30]])
arr2 = np.array([[100,200,300]])
v_stacked = np.vstack((arr1,arr2))
print(v_stacked)
h_stacked = np.stack((arr1,arr2))
print(v_stacked)
