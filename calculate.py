from sympy.solvers import solve
from sympy import Symbol


def generate_x_y(offsets, radii):
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
    return list_soln
