#Erfan Nouhi
#distance centrality
import matplotlib.pyplot as plt
import json
import networkx as nx

with open("C:\\Users\\0000\\OneDrive\\دسکتاپ\\git-hub work\\4032_FinalProject_DMath\\Erfan Nouhi 40326403-1\\src\\friendship\\friendship.json","r") as file:
    members = json.load(file)


adjoint_matrix = [[0 for _ in range(len(members))] for _ in range(len(members))]

names = []
for member in members:
    names.append(member["name"])

for i in range(len(members)):
    current_name_index = i
    current_name = names[i]
    current_friends = members[i]["friends"]
    for friend_name in current_friends:
        friend_index = names.index(friend_name)

        adjoint_matrix[current_name_index][friend_index] = 1


def dijkstra(start_name):
    start_index = names.index(start_name)
    distances = [float('inf')] * len(names)
    distances[start_index] = 0
    visited = [False] * len(names)

    for _ in range(len(names)):
        min_distance = float('inf')
        u = None
        for i in range(len(names)):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        if u is None:
            break

        visited[u] = True

        for v in range(len(names)):
            if adjoint_matrix[u][v] != 0 and not visited[v]:
                alt = distances[u] + adjoint_matrix[u][v]
                if alt < distances[v]:
                    distances[v] = alt

    return distances

distances_sum = []

for name in names:
    distances = dijkstra(name)
    sum_distances = sum(distances)
    distances_sum.append(sum_distances)


for name,distance_sum in zip(names,distances_sum):
    print(f"{name} sum of distances from rest nodes is {distance_sum}")

min_sum_distance = 100000
for i in range(len(distances_sum)):
    if distances_sum[i] < min_sum_distance:
        min_sum_distance = distances_sum[i]


print(f"the graph centrality according to distace from others is {min_sum_distance}")
print(f"central node is {names[distances_sum.index(min_sum_distance)]}")


    

