import re

w1 = input()
w2 = input()
if not re.mach(w1, w2):
    print(len(w) * 2)
else:
    print('no matching')