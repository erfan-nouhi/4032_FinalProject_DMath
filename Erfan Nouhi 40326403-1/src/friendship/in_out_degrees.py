#Erfan Nouhi

import json

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


for member in members:
    print("name ",member["name"])
    print(len(member['friends']))
    
print("\n")

def in_out_deg(name):
    name_index = names.index(name)

    print(sum(adjoint_matrix[name_index]),"this graph is undirected")

in_out_deg("Hossein")
    