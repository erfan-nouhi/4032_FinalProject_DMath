#Erfan Nouhi
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

def dfs(visited:list,vertext_index,component:list,vertices:list,adj_matrix:list):
    component.append(vertext_index)
    visited[vertext_index] = True

    for i in range(len(vertices)):
        if adj_matrix[vertext_index][i] and not visited[i]:
            dfs(visited,i,component,vertices,adj_matrix)


def find_components(visited:list,adj_matrix:list,vertices:list):

    result = []

    for i in range(len(vertices)):
        component = []
        if not visited[i] :
            dfs(visited,i,component,vertices,adj_matrix)
        if len(component):
            result.append(component)

    return result

visited = [False] * len(members)

components = find_components(visited,adjoint_matrix,names)
names_component = []

for component in components:
    if len(component):
        name_component = []
        for index in component:
            name_component.append(names[index])
        names_component.append(name_component)

print(names_component)


    
