def print_rev(n):
    if n == 0:
        return
    print(n, end=" ")
    print_rev(n - 1)

n = int(input())
print_rev(n)
