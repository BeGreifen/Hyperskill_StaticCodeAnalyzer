import ast
# Assume `code` contains the source code.


class ImportNameVisitor(ast.NodeVisitor):
    def visit_Import(self, node):
        for alias in node.names:
            print(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module is not None:
            print(f"From {node.module}:")
            for alias in node.names:
                print(f"  {alias.name}")
        self.generic_visit(node)


tree = ast.parse(code)

visitor = ImportNameVisitor()
visitor.visit(tree)
