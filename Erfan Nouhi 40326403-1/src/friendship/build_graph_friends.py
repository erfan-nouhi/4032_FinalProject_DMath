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

G = nx.Graph()

# Add nodes
G.add_nodes_from(names)

# Add edges based on the adjacency matrix
for i in range(len(adjoint_matrix)):
    for j in range(i + 1, len(adjoint_matrix)):  # Only upper triangle to avoid duplicates
        if adjoint_matrix[i][j] == 1:
            G.add_edge(names[i], names[j])

plt.figure(figsize=(14,10))
pos = nx.spring_layout(G, seed=42,k=0.5)  

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

plt.title("Friendship Graph", fontsize=16)
plt.axis('off')  
plt.tight_layout()
plt.show()

for member in members:
    print("name ",member["name"])
    for friend in member["friends"]:
        print('\t',friend)

    