def solve(a, b, c):
    D = b**2 - 4*a*c   
    if D == 0:
        root = -b / (2*a)
        return f"{root:.1f} {root:.1f}"
    else:
        root1 = (-b - D**0.5) / (2*a)
        root2 = (-b + D**0.5) / (2*a)
        return f"{min(root1, root2):.1f} {max(root1, root2):.1f}"

a = int(input())
b = int(input())
c = int(input())
print(solve(a, b, c))
