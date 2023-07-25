import json

# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
test_min = min(test_dict, key=test_dict.get)
test_max = max(test_dict, key=test_dict.get)
# Work with the 'test_dict'
print(f"min: {test_min}")
print(f"max: {test_max}")
