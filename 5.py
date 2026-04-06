def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_valid_password(password):
    parts = password.split(':')
    if len(parts) != 3:
        return False
    a, b, c = parts
    if not (a.isdigit() and b.isdigit() and c.isdigit()):
        return False
    a_num = int(a)
    b_num = int(b)
    c_num = int(c)
    if a_num <= 0 or b_num <= 0 or c_num <= 0:
        return False
    if a != a[::-1]:
        return False
    if not is_prime(b_num):
        return False
    if c_num % 2 != 0:
        return False
    return True

password = input()
print(is_valid_password(password))
