graph = {'A': ['B', 'F'],
         'B': ['A', 'C'],
         'C': ['B', 'D'],
         'D': ['C', 'E'],
         'E': ['D', 'F'],
         'F': ['E', 'A']}

# Hash tables vanligt för att bygga grafer. Nyckeln är nodnamnet och värdena är den nodens kopplingar.

#       A
#     /    \
#   B       F
#   |        |
#   C       E
#    \     /
#       D

# Traversera grafen:


def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:  # Exit strategy (to end recursion). Här tar stigen slut.
        print("Ending")
        return path

    # for loop to check each of the potential connections.
    for node in graph[start]:
        # Node is already in path; programme does not add node to path (again)
        print("Checking Node ", node)

        if node not in path:
            print("Path so far ", path)

            # Node was not in path; programme recursively calls function to locate the next node in the path.
            newp = find_path(graph, node, end, path)
            if newp:
                return newp


# Hitta stig mellan B och E (NB! Ingen hänsyn till längd på sträckan!)
find_path(graph, 'B', 'E')

# Checking Node  A
# Path so far  ['B']
# Checking Node  B
# Checking Node  F
# Path so far  ['B', 'A']
# Checking Node  E
# Path so far  ['B', 'A', 'F']
# Ending
