from sympy import symbols, Eq, solve, Matrix

x, y, z = symbols('x y z')

# 1 a)
equations_1a = [
    Eq(x - 2*y - 2*z, 0),
    Eq(-2*x + y - z, -3),
    Eq(3*x + 2*y + z, 4)
]

# 1 a)
solution_1a = solve(equations_1a, (x, y, z))

# 1 b)
equations_1b = [
    Eq(x + y, 1),
    Eq(2*x + y - z, 1),
    Eq(3*x + y - 2*z, 1)
]

# 1 b)
solution_1b = solve(equations_1b, (x, y, z))

# 2 a)
equations_2a = [
    Eq(2*x + 4*y - z, 11),
    Eq(6*x - y - 3*z, 7),
    Eq(4*x + 5*y - 2*z, 16)
]

# 2 a)
solution_2a = solve(equations_2a, (x, y, z))

# 2 b)
equations_2b = [
    Eq(4*x + 2*y - 2*z, 0),
    Eq(2*x + y - z, 1),
    Eq(3*x + y - 2*z, 1)
]

# 2 b) vastaus on epätosi
solution_2b = solve(equations_2b, (x, y, z))

# kertaus a)
A1 = Matrix([[5, 3], [2, 1]])
B1 = Matrix([[9], [4]])
solution_1 = A1.inv() * B1

# kertaus b)
A2 = Matrix([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
B2 = Matrix([[6], [2], [9]])
solution_2 = A2.inv() * B2

# kertaus c)
A3 = Matrix([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
B3 = Matrix([[-1], [5], [2]])

print(f"1 a) {solution_1a}")
print(f"1 b) {solution_1b}")
print(f"2 a) {solution_2a}")
print(f"2 b) {solution_2b}, ratkaisu on epätosi joten ei ratkaisua. ")
print(f"a) x = {solution_1[0]}, y = {solution_1[1]}\nb) x = {solution_2[0]}, y = {solution_2[1]}, z = {solution_2[2]}")
try:
    solution_3 = A3.inv() * B3
    print(f"c) x = {solution_3[0]}, y = {solution_3[1]}, z = {solution_3[2]}")
    print(solution_3)
except Exception as e:
    print("c) ei voida suorittaa käänteismatriisia:", e)
