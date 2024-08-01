names_list = [
    ["Alice", "Bob", "Charlie", "David", "Emily"],
    ["Frank", "Grace", "Henry", "Isabella", "Jack"],
    ["Kate", "Liam", "Mia", "Noah", "Olivia"],
    ["Penelope", "Quentin", "Riley", "Sophia", "Thomas"],
    ["Ursula", "Victor", "William", "Xander", "Yara"]
]

print(names_list[2][2])
print(names_list[3][3])
print(names_list[4][4])

for i, row in enumerate(names_list):
    for j, names_list in enumerate(row):
        print(f"{names_list} is in row {i+1}, seat{j+1}")
        