#Erfan Nouhi
import matplotlib.pyplot as plt
import json
import networkx as nx

with open('C:\\Users\\0000\\OneDrive\\دسکتاپ\\git-hub work\\4032_FinalProject_DMath\\Erfan Nouhi 40326403-1\\src\\friendship\\friendship.json',"r") as file:
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
  
def bellman_ford(start_name):
    start_index = names.index(start_name)
    distances = [float('inf')] * len(names)
    distances[start_index] = 0

    for i in range(len(names)- 1):
        for u in range(len(names)):
            for v in range(len(names)):
                if adjoint_matrix[u][v] != 0:
                    if distances[u] + adjoint_matrix[u][v] < distances[v]:
                        distances[v] = distances[u] + adjoint_matrix[u][v]

    return distances

distances = bellman_ford("Ali")

for name,distance in zip(names,distances):
    print(f"{name} distance from Ali is {distance}")

    