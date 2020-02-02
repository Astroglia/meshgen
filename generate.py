import math
import numpy as np
import sympy

def calc_radius(current, voltage):
    radius = current/(voltage*4*math.pi)
    return radius

'''
Actual Points:
    A : (   0 ,  0  )
    B : (   5 ,  0  )
    C : (   5 ,  4  )
    D : (   2 , -9  )
    E : ( -10,  -1  )
'''
def example_radius_matrix():
    mat = np.array( [
        # A  B        C       D       E
        [ 0, 5,    6.40,   9.22, 10.049 ], #A
        [ 0, 0,    4.00,   9.48,  15.00 ], #B
        [ 0, 0,       0,  13.34,  15.81 ], #C
        [ 0, 0, 0,            0,  14.42 ], #D
        [ 0, 0, 0, 0,                 0 ]  #E

    ])
    # mat = np.array( [
    #     # A  B        C       D       E
    #     [ 0, 5.1,  6.40,   9.22,    2.23 ], #A
    #     [ 0, 0,    3.00,   10.44,   6.7  ], #B
    #     [ 0, 0,       0,  13.34,    8.48 ], #C
    #     [ 0, 0, 0,            0,    11.4 ], #D
    #     [ 0, 0, 0, 0,                 0  ]  #E

    #])
    return mat

def form_symbolic_map(arr):
    symbolic_arr = sympy.symarray('p', (arr.shape[0], arr.shape[0]))
    symbolic_arr[arr == 0] = 0
    symbolic_arr = symbolic_arr.transpose()
    return symbolic_arr

# def generate_voltage_mapping(num_points, dimensionality=3, current=3, voltage_eq='point'):
#     volt_radius_mapping = np.random.rand( num_points, num_points )
#     #fill in diagonals
#     for i in range(volt_radius_mapping.shape[0]):
#         for j in range( volt_radius_mapping.shape[1] ):
#             if i == j:
#                 volt_radius_mapping[i, j] = 0 #e.g. voltage source @ a --> radius(A,A) = 0
#     return volt_radius_mapping