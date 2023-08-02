# G = (V, E)
# Graf = [(Stockholm, Göteborg)]

# Trafikljus:
# Go = [Red, green], Caution = [Green, Yellow], Stop = [Yellow, Red]

Nodes = range(1, 5)
Edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5)]

#                  2
#               /     /
#              /     /
#         1         /
#     /       \    /
#    /         \  /
# 5              3
#   \         /
#     \      /
#         4
