# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
# passwords = ['0vbno0re', 'ad12', 'fgghut', '4qp', 'qwerty']
sorted_passwords = sorted(passwords, key=len, reverse=False)
for pw in sorted_passwords:
    print(pw, len(pw))
