import ast

def read_user_input():
    return input()

def print_type(value):
    try:
        parsed_value = ast.literal_eval(value)
        # print(parsed_value)
        print(type(parsed_value))
    except (SyntaxError, ValueError):
        print("Invalid input. Please enter a valid literal value.")

if __name__ == "__main__":
    user_input = read_user_input()
    print_type(user_input)
