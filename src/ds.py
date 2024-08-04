# Data structure practice for Python

Tuple1 = ('bryan', 'melendez')
print(Tuple1)

Tuple2 = ('image/path', 'Image Title')
print(Tuple2)

Tuple3 = ('bryan', 'robert', 'melendez')
print(Tuple3)

# concatenating tuples
Tuple4 = Tuple1 + Tuple2
print(Tuple4)

del Tuple1
# print(Tuple1) -> you cannot print it because it does not exist anymore

# returns the maximum element, don't know what that means for strings
print(max(Tuple3))

# implemented as key value pairs
Dict = dict({1: 'bryan'})
print(Dict)

# implemented using tuples
Dict2 = dict([(2, 'bryan')])
print(Dict2)

Dict3 = dict({'blue': 'bryan', 'green': 'ethan'})
print(Dict3['blue'])

Dict4 = {'bryan': 'melendez', 'ethan': 'melendez'}
print(Dict4)

# types
test_bool = True
