from sympy.solvers import solve
from sympy import Symbol


def generate_x_y(offsets, r1, r2):
    if offsets is None:
        offsets = [ 0, 0, 0, 0 ]
    a = offsets[0]
    b = offsets[1]
    c = offsets[2]
    d = offsets[3]
    # implement:
    # https://www.wolframalpha.com/input/?i=%28x-a%29%5E2+%2B+%28y-b%29%5E2+%3D+r%5E2%2C+%28x-c%29%5E2+%2B+%28y-d%29%5E2+%3D+m%5E2%2C+solve+for+x%2C+y
    # (x - a)^2 + (y - b) ^2 = (r1)^2 ; (x - c)^2 + (y - d)^2 = (r2)^2
    x = Symbol('x')
    y = Symbol('y')
    solution = solve( [(x-a)**2 + (y - b)**2 - r1**2, (x-c)**2 + (y - d)**2 - r2**2 ], [x,y] )
    for i in solution:
        for x in i:
            print( float(x))
    #print(solution)