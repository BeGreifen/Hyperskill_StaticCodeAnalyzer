import ast

expression = "(34 + 6) * (23**2 - 7 + 45**2)"


def build_ast(expr):
    return ast.parse(expr)


def collect_nodes(ast_node):
    n_list = []

    for node in ast.walk(ast_node):
        n_list.append(node)

    return n_list


if __name__ == "__main__":
    ast_tree = build_ast(expression)
    nodes_list = collect_nodes(ast_tree)
    
    print(len(nodes_list))
