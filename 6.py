def solve(a, b, c):
    D = b**2 - 4*a*c   
    if D == 0:
        root = -b / (2*a)
        return f"{root:.1f} {root:.1f}"
    else:
        root1 = (-b - D**0.5) / (2*a)
        root2 = (-b + D**0.5) / (2*a)
        return f"{min(root1, root2):.1f} {max(root1, root2):.1f}"

print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))
