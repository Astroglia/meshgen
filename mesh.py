import math
import numpy as np
import generate
import calculate
import time

radius_map = generate.example_radius_matrix()

##### 2 Dimensional Case: define first point to (0,0) position,
# And second to (radius, 0) position, where radius is first point --> second point radius,
# and the remaining coordinates are unknown.
coordinates = [ [0,0], [radius_map[0,1], 0], [ [None, None] ]*(radius_map.shape[0]-2)  ]

##get an estimate for the third coordinate, then loop through the rest.
temp_offsets = [coordinates[0] , coordinates[1]]
temp_offsets = [item for sublist in temp_offsets for item in sublist]
solution = calculate.generate_x_y( temp_offsets, [radius_map[0,2], radius_map[1,2]] )

previous_coord_soln = [ solution[0], solution[1] ]
previous_coord_soln = [item for sublist in previous_coord_soln for item in sublist]
for i in range( 2, radius_map.shape[1]): #go through each column in the matrix
    curr_analysis_col = radius_map[ :, i ]
    #remove zeros from the symmetric matrix
    curr_analysis_col = np.trim_zeros(curr_analysis_col)

    coordinate_solution = calculate.generate_x_y( previous_coord_soln, [ curr_analysis_col[-1], curr_analysis_col[-1] ]  )
    print( coordinate_solution )
    time.sleep(50)