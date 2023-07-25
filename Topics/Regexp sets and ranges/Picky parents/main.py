import re

# your code here
regex = r'^[B-Nb-n][aeiouAEIOU]'
test = input()
if re.match(regex, test):
    print("Suitable!")
