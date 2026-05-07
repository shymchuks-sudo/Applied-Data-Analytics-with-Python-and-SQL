import numpy as np
arr = np.array([[1,2,3], [4,5,6]])

print(arr)
# [[1 2 3]
#  [4 5 6]]

print(type(arr))
# <class 'numpy.ndarray'>

#AUTOFILL
arr2 = np.empty([2,2], dtype=int)
# 2 lists of 2 elements each, every element is a random integer
print(arr2)
# [[8247308487062937955 7309475598054157929]
#  [7598538446695527519 7957697952966078054]]

arr3 = np.full((2, 3), 7)
# 2 lists of 3 elements each, every element is a 7
print(arr3)
# [[7 7 7]
#  [7 7 7]]

arr4 = np.zeros([2,3])
print(arr4)
# [[0. 0. 0.]
#  [0. 0. 0.]]

arr5 = np.ones([2,3])
print(arr5)
# [[1. 1. 1.]
#  [1. 1. 1.]]
