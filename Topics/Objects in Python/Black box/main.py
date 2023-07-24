# use the function blackbox(lst) that is already defined
dummy_list = [1, 2, 3]
new_list = blackbox(dummy_list)
if id(dummy_list) == id(new_list):
    print("same")
else:
    print("new")