
# Social Network Using Adjacency Matrix

users = ["Sneha", "Yash", "Priya", "Rahul", "Amit"]

# Create an empty adjacency matrix
n = len(users)
matrix = [[0 for _ in range(n)] for _ in range(n)]

# Add friendship connections
friendships = [
    ("Sneha", "Yash"),
    ("Sneha", "Priya"),
    ("Yash", "Rahul"),
    ("Priya", "Amit"),
    ("Rahul", "Amit")
]

# Represent friendships in the matrix
for user1, user2 in friendships:
    i = users.index(user1)
    j = users.index(user2)

    matrix[i][j] = 1
    matrix[j][i] = 1

# Display the adjacency matrix
print("SOCIAL NETWORK ADJACENCY MATRIX")
print("\nUsers:", ", ".join(users))

print("\nAdjacency Matrix:")
print("       " + " ".join(f"{user:>6}" for user in users))

for i in range(n):
    print(f"{users[i]:>6} " +
          " ".join(f"{value:>6}" for value in matrix[i]))

# Check whether two users are friends
user1 = "Sneha"
user2 = "Yash"

i = users.index(user1)
j = users.index(user2)

print(f"\nAre {user1} and {user2} friends?")
if matrix[i][j] == 1:
    print("Yes, they are friends.")
else:
    print("No, they are not friends.")
