def greedy(graph):
    colours = {}
    for node in graph:  # Iterate over each node in the graph
        neighbour_colours = set(colours[neighbour] for neighbour in graph[node] if neighbour in colours)
        colour = 0
        while colour in neighbour_colours:
            colour += 1
        colours[node] = colour
    return colours

graph = {
    0: [1, 4, 6],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 3, 5],
    5: [4, 6],
    6: [0, 5]
}

colours = greedy(graph)
print("Coloring of graph:")
for vertex, color in colours.items():
    print(f"Vertex {vertex} ---> Color {color}")
