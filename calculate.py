import sympy
import numpy as np

def solve_distance_matrix(symbolic_distance_map, radius_map, dimensionality=2):
    s_map = symbolic_distance_map #placeholder name for readability.
    x_dist = radius_map.shape[0]
    points = [ [0]*dimensionality ] #first point has x/y/z/...n of (0, 0, ...)

    for x in range(1, x_dist): #go through each matrix row, except the first (which is the first point row).
        equation_list = []
        for y in range(x): #generate equations for each index in that matrix row.
            equation_list.append( sum((s_map[y] - s_map[x]) ** 2) - radius_map[y,x]**2 )  # e.g. (x - 5)^2 - radius, and so on
        solution_vars = list(np.trim_zeros( s_map[ x , : ])) #current variables to solve for are the current matrix row (but remove the zeros at the end)

        solution = sympy.solve( equation_list, solution_vars)[1]
        s_map[x, :len(solution)] = solution #update symbolic map for that row
        points.append( format_solution(solution, dimensionality) )
    return points

def format_solution(solution, requested_dims):
    solution = list(solution)
    if len(solution) < requested_dims:
        solution.extend( [0]*(requested_dims - len(solution)))
    rounded = [ round(i, 2) for i in solution ]
    return rounded







