from sympy.solvers import solve
from sympy import Symbol
import math
import time
import itertools

def generate_x_y(offsets, radii, unwrapped=False, verbose=False):
    if offsets is None:
        offsets = [ 0, 0, 0, 0 ]
    # implement:
    # https://www.wolframalpha.com/input/?i=%28x-a%29%5E2+%2B+%28y-b%29%5E2+%3D+r%5E2%2C+%28x-c%29%5E2+%2B+%28y-d%29%5E2+%3D+m%5E2%2C+solve+for+x%2C+y
    # (x - a)^2 + (y - b) ^2 = (r1)^2 ; (x - c)^2 + (y - d)^2 = (r2)^2
    equations = []
    x = Symbol('x')
    y = Symbol('y')
    oi = 0
    for i in range( len(radii) ):
        curr_eq = (x - offsets[oi])**2 + (y - offsets[oi + 1])**2 - radii[i]**2
        equations.append(curr_eq)
        oi = oi + 2

    solution = solve( equations, [x, y] )
    list_soln = []
    for i in solution:
        list_soln.append( list(i) )
    if unwrapped:
        list_soln = [item for item in list_soln]
    if verbose:
        print("LIST SOLUTION: ", list_soln)
        print("FOR THE FOLLOWING OFFSETS: ", offsets)
        print("AND THE FOLLOWING RADII  : ", radii)
        print("FROM THE FOLLOWING EQS   : ", equations)
    return list_soln


#need to do this so that we can allow for leeway in solution due to float comparison issues (not sure if sympy does this).
def isolate_x_y_solution(solutions_1, solutions_2, radius_between):
    final_solutions_1 = []
    final_solutions_2 = []
    print("ISOLATING...")
    print(solutions_1)
    print(solutions_2)
    print("with a radius of: ", radius_between)

    lw = 0.84*radius_between
    lw2 = 1.2*radius_between

    permutations = list(itertools.product( solutions_1, solutions_2))
    print("==================================")
    for index, curr, in enumerate(permutations):
        print(curr)
        x_y_dist_curr = [i - j for i, j in zip(curr[0], curr[1])]
        radius = math.sqrt( x_y_dist_curr[0]**2 + x_y_dist_curr[1]**2 )
        if lw <= radius <= lw2:
            print("SOLUTION FOUND :) ")
            final_solutions_1.append( curr[0] )
            final_solutions_2.append( curr[1] )
           # break
    return final_solutions_1, final_solutions_2

    # for i in range(len(solutions_1)):
    #     curr_1 = solutions_1[i]
    #     curr_2 = solutions_2[i]
    #
    #     x_y_distance = [i - j for i, j in zip(curr_1, curr_2)]
    #     print(x_y_distance)
    #     time.sleep(3)

