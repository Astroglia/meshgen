import math
import numpy as np
import generate
import calculate

radius_map = generate.example_radius_matrix()

##### 2 Dimensional Case: define first point to (0,0) position,
# And second to (radius, 0) position, where radius is first point --> second point radius,
# and the remaining coordinates are unknown.
coordinates = [ [0,0], [radius_map[0,1], 0], [ [None, None] ]*(radius_map.shape[0]-2)  ]
#
print(coordinates)

solution = calculate.generate_x_y([1,2,2,3], [3, 2] )
print(solution)