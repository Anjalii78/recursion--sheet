def is_pal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_pal(s[1:-1])

s = input()
if is_pal(s):
    print("Palindrome")
else:
    print("Not Palindrome")
