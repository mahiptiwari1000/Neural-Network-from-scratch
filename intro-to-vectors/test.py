from vector import Vector

v1 = Vector([1,2,3])
v2 = Vector([4,5,6])

print(v1, '' , v2)

print(len(v1))
print(v1 == v2)

x = Vector([1,2,3])
print(x)
print(x.coords)

print(x[0])

x[0] = 42
print(x[0])
print(x)

print([1,2].__add__([3,4])) #by default __add__ method in python concatenates and does not add
print([1,2] + [3,4])# same behavior here

##To resolve this problem to add vectors, we should define a custom method in the Vector class

print(v1 + v2)

x = Vector([1,2,3])
print(x * 2.0)
print(2.0 * x)