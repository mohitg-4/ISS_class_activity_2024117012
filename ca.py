def find_cube_pairs(target):
    solutions = []  # removed unnecessary semicolon
    max_num = round(target ** (1/3))  # fixed exponentiation operator and variable name
    for a in range(1, max_num + 1):  # fixed ranges -> range
        for b in range(a, max_num + 1):
            if a**3 + b**3 == target:  # fixed exponentiation operator and variable name
                solutions.append((a, b))  # removed unnecessary semicolon
    return solutions

pairs = find_cube_pairs(1729)  # removed trailing comma
print("Valid cube pairs for 1729:")  # fixed target number and removed comma
for a, b in pairs:  # fixed variable name from pair to pairs
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # fixed power calculation and target number