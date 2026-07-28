from dimensional_vector import DimensionalVector 
v = DimensionalVector(2)
v[0] = 3
v[1] = 6
print("v =", v)

u = v + v 
print("vector addition")
print("u =", u)

# 3D vector example
a =DimensionalVector(3)
a[0] = 1
a[1] = 3
a[2] = 7
b = DimensionalVector(3)
b[0] = 2
b[1] = 8
b[2] = 5
c = a + b
print("c =", c)