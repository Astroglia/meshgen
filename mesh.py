### Local python files
import generate
import calculate
import QOL

radius_map = generate.example_radius_matrix()
symbolic_equation_map = generate.form_symbolic_map(radius_map)

position_matrix = calculate.solve_distance_matrix(symbolic_equation_map, radius_map)
QOL.pretty_print_solutions(position_matrix)