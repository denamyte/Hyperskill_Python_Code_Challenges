import ast

tree = ast.parse(code)
for node in tree.body:
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        print(*(n.name for n in node.names), sep='\n')
