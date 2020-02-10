import numpy as np

# np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
# np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
#
# # shape gives info on np array as in "np_height.shape"
# print(np_height.shape)
#
# # put both weight and heigh int a 2d array
# np_2d = np.array([np_height, np_weight])
# print(np_2d)
# print(np_2d.shape)
#
# print(np_2d[0])
# # [ 1.73  1.68  1.71  1.89  1.79]

# print(np_2d[0][1])
# # OR np_2d[0, 1]
# # 1.68
#
# # select both rows
# print(np_2d[:])
# # [[  1.73   1.68   1.71   1.89   1.79]
# #  [ 65.4   59.2   63.6   88.4   68.7 ]]

# # select 2nd and 3rd column in both rows
# print(np_2d[:, 1:3])
# # [[  1.68   1.71]
# #  [ 59.2   63.6 ]]

# # select only all items in second row
# print(np_2d[1, :])

#####################################################################
# Create baseball, a list of lists
baseball = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Print out the 4th row of np_baseball
print(np_baseball[3, :])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)

# Print out height of 4th player
print(np_baseball[3, 0])

# convert from in and lb to m and kg
conversion = np.array([0.0254, 0.0453592])
print(np_baseball * conversion)
