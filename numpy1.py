import numpy as np

# a=np.array([1,2,3,4,5])
# print(a)
# print(a[1:3])

# b=np.array([[1,2,3],[4,5,6]])
# print(b)
# print(b[:,1])

# c=np.array((1,2,3))
# print(c)

# arr=np.array([[-1,2,0,4],
#               [4,-0.5,6,0],
#               [2.6,0,7,8],
#               [3,-7,4,2.0]])
# arr2=arr[:2,::2]
# print(arr2)

# a1=np.array([[1,2],
#             [3,4]])

# b1=np.array([[4,3],
#              [2,1]])
# print(a1+1)
# print(b1-2)
# print(a1.sum())
# print(a1+b1)
# print(a1.max())
# print(a1.min())
# print(a1.mean())

# x=np.array([1,2])
# y=np.array([1.0,2,2])
# print(x.dtype)
# print(y.dtype)

# today=np.datetime64('2025-11-02')
# print(today)
# print(np.datetime64(today,'Y'))

# c=np.array([1,2,3,4,5,6])
# print(c.reshape(3,2))

d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d)
print(d.sum())
print(d.mean())
print(d.sum(axis=0))
print(d.sum(axis=1))
print(d.T)