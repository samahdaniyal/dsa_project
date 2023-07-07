# Graph Helper Functions
def addNodes(G, nodes):
    for n in nodes:
        G[n] = []
    return G


def addEdges(G, edges, directed):
    if directed == True:
        for i in range(len(edges)):
            if edges[i][0] in G.keys():
                G[edges[i][0]].append((edges[i][1], edges[i][2]))
        return G

    elif directed == False:
        for i in range(len(edges)):
            if edges[i][0] in G.keys():
                G[edges[i][0]].append((edges[i][1], edges[i][2]))
        for j in range(len(edges)):
            if edges[j][1] in G.keys():
                G[edges[j][1]].append((edges[j][0], edges[j][2]))
        return G


def listOfNodes(G):
    keyList = []
    for key in G.keys():
        keyList.append(key)
    return keyList


def listOfEdges(G, directed):
    final = []
    if directed == True:
        for vertex in G.keys():
            for i in range(len(G[vertex])):
                final.append((vertex, G[vertex][i][0], G[vertex][i][1]))
        return final
    else:
        for vertex in G.keys():
            for i in range(len(G[vertex])):
                if (G[vertex][i][0], G[vertex], G[vertex][i][1]) not in final:
                    final.append((vertex, G[vertex][i][0], G[vertex][i][1]))
        return final


def printIn_OutDegree(G):
    for vertex in G:
        outDegree = 0
        inDegree = 0
        for od in range(len(G[vertex])):
            outDegree += 1
        for i in G:
            for id in G[i]:
                if vertex == id[0]:
                    inDegree += 1
        print(vertex, "=> Out-Degree:", outDegree, ",", "In-Degree:", inDegree)


def printDegree(G):
    for vertex in G:
        outDegree = 0
        for od in range(len(G[vertex])):
            outDegree += 1
        print(vertex, "=>", outDegree)


def getNeighbors(G, nodes):
    d = {}
    for vertex in G:
        for node in nodes:
            if vertex == node:
                d[vertex] = []
                for degree in range(len(G[vertex])):
                    d[vertex].append(G[vertex][degree][0])

    return d


def getInNeighbors(G, node):
    lst = []
    for vertex in G:
        for i in range(len(G[vertex])):
            if node == G[vertex][i][0]:
                lst.append(vertex)
    return lst


def getOutNeighbors(G, node):
    lst = []
    for vertex in G:
        if vertex == node:
            for degree in range(len(G[vertex])):
                lst.append(G[vertex][degree])
    return lst


def getNearestNeighbor(G, node):
    lst = []
    for vertex in G:
        if vertex == node:
            for n in range(len(G[vertex])):
                lst.append(G[vertex][n][1])
    a = min(lst)
    for i in G.keys():
        if a == G[node][i][1]:
            return G[node][i][0]


def isNeighbor(G, Node1, Node2):
    for vertex in G:
        for i in G[vertex]:
            if (vertex, i[0]) == (Node1, Node2):
                return True
            else:
                return False


def removeNode(G, node):
    del G[node]
    for i in G.values():
        for j in i:
            if j[0] == node:
                i.remove(j)
    return G


def removeNodes(G, nodes):
    for i in nodes:
        del G[i]
        for j in G.values():
            for k in j:
                if k[0] == i:
                    j.remove(k)
    return G


def displayGraph(G):
    D = {}
    for vertex in G:
        D[vertex] = []
        for i in G[vertex]:
            D[vertex] += [i]
    return D


def display_adj_matrix(G):
    lst = [[0 for a in range(len(G))] for b in range(len(G))]
    for vertex in G:
        for i in G[vertex]:
            lst[vertex - 1][i[0] - 1] = i[1]
    print(lst)


import math


def heuristic(node1, node2):
    # coordinates = {'stairs':(0,6), 'music room':(0,11), 'linux lab':(0,13), 'graphics lab':(7,13), 'E-011 classroom':(10,13), 'E-012 classroom':(11,13), 'tapal cafeteria':(20,6), 'projects lab':(11,3), 'power lab':(6,3), 'circuits and electronics lab':(1,3), 'female lounge':(0,0)} #1
    # coordinates = {'stairs':(1,4), 'music room':(1,6.5), 'linux lab':(1,8.5), 'graphics lab':(8,8), 'E-011 classroom':(11,8), 'E-012 classroom':(13.5,8), 'tapal cafeteria':(17,5), 'projects lab':(15,3), 'power lab':(11.5,3), 'circuits and electronics lab':(8,3), 'female lounge':(0,0)} #2
    coordinates = {
        "stairs": (0, 3),
        "music room": (0, 5),
        "linux lab": (0, 8),
        "graphics lab": (4, 8),
        "E-011 classroom": (6, 8),
        "E-012 classroom": (8, 8),
        "tapal cafeteria": (11, 5),
        "projects lab": (9, 1),
        "power lab": (6, 1),
        "circuits and electronics lab": (3, 1),
        "female lounge": (0, 1),
    }  # 3
    x1, y1 = coordinates[node1]
    x2, y2 = coordinates[node2]
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)


nodes = [
    "stairs",
    "music room",
    "linux lab",
    "graphics lab",
    "E-011 classroom",
    "E-012 classroom",
    "tapal cafeteria",
    "projects lab",
    "power lab",
    "circuits and electronics lab",
    "female lounge",
]
edges = [
    ["stairs", "music room", 5],
    ["music room", "stairs", 5],
    ["music room", "linux lab", 3],
    ["linux lab", "music room", 3],
    ["linux lab", "graphics lab", 7],
    ["graphics lab", "linux lab", 7],
    ["graphics lab", "E-011 classroom", 3],
    ["E-011 classroom", "graphics lab", 3],
    ["E-011 classroom", "E-012 classroom", 1],
    ["E-012 classroom", "E-011 classroom", 1],
    ["E-012 classroom", "tapal cafeteria", 14],
    ["tapal cafeteria", "E-012 classroom", 14],
    ["tapal cafeteria", "projects lab", 7],
    ["projects lab", "tapal cafeteria", 7],
    ["projects lab", "power lab", 5],
    ["power lab", "projects lab", 5],
    ["power lab", "circuits and electronics lab", 5],
    ["circuits and electronics lab", "power lab", 5],
    ["circuits and electronics lab", "stairs", 5],
    ["stairs", "circuits and electronics lab", 5],
    ["stairs", "tapal cafeteria", 15],
    ["tapal cafeteria", "stairs", 15],
    ["stairs", "female lounge", 8],
    ["female lounge", "stairs", 8],
]
G = {}
addNodes(G, nodes)
addEdges(G, edges, True)

# takes input
# start = input()
# end = input()
start = "E-011 classroom"
end = "projects lab"


def navigating_habib(G, start, end):
    distance = 0
    closed_list = []
    open_list = [(start, 0, heuristic(start, end))]
    visited = []

    # uses A* algorithm to find the shortest path
    while open_list:
        current_node = min(open_list, key=lambda t: t[2])  # finds the node with the minimum heuristic value
        closed_list.append(current_node[0])
        distance += current_node[1]  # counts the steps it will take to reach the destination
        idx = open_list.index(current_node)  # finds the index of the node with minimum heuristic value
        open_list.pop(idx)

        if current_node[0] == end:
            return closed_list, distance, "steps"

        # BFS search to search for the adjacent nodes
        else:
            visited.append(current_node[0])
            queue = [current_node]
            while queue:
                x = queue.pop(0)
                neighbors = getOutNeighbors(G, x[0])
                for i in range(len(neighbors)):
                    if neighbors[i][0] not in visited:
                        open_list.append((neighbors[i][0],neighbors[i][1],heuristic(neighbors[i][0], end),))
    return None


print(navigating_habib(G, start, end))

# print(navigating_habib(G,start,end)) #-> this will output a list [[path==start node to end node], number of steps taken by that path]

""" Turtle Function """

turtle_coordinates = {
    "stairs": [-500, -95],
    "music room": [-520, 40],
    "linux lab": [-500, 240],
    "graphics lab": [-140, 225],
    "E-011 classroom": [10, 225],
    "E-012 classroom": [190, 225],
    "tapal cafeteria": [270, -40],
    "projects lab": [280, -175],
    "power lab": [80, -175],
    "circuits and electronics lab": [-300, -175],
    "female lounge": [-570, -320],
    "learn courtyard": [-530, -320],
}
lst = navigating_habib(G, start, end)[0]
steps = navigating_habib(G, start, end)[1]


def display_map():
    import turtle

    tr = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width=1500, height=700)  # sets the width and height of the turtle screen.
    wn.bgpic("LG aerial view.gif")  # sets the background image of the turtle screen
    tr.penup()  # lifts the turtle pen up
    tr.write(f"steps:{steps}", font=("Arial", 20, "bold"))  # writes a string to the turtle screen
    for i in lst:  # iterates through the list of path provided by navigating_habib function
        tr.goto(turtle_coordinates[i])  # it moves the turtle to a coordinate
        tr.pendown()  # puts the turtle pen down
        tr.shape("circle")  # sets the shape of the turtle (can be square, arrow, circle, turtle, triangle, classic)
        tr.color("orange")  # sets the color of the turtle
        tr.width(5)  # sets the width of the turtle pen
        tr.speed(2)  # sets the speed of the turtle

    wn.mainloop()  # keeps the turtle window open


print(display_map())
