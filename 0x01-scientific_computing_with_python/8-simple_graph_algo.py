graph = {
    "a": ["b", "d"],
    "b": [],
    "c":[],
    "d": ["e", "g"],
    "e":["c"],
    "f":[],
    "g":['f']
}

def dfs(graph, source):
    stack = []
    stack.append