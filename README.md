
# Social-Network-Adjacency-Matrix

A Python case study demonstrating how an adjacency matrix represents friendship connections between users in a social network.

# Social Network Using Adjacency Matrix

A social network consists of users connected through friendships. An adjacency matrix is a graph representation technique used to store and display connections between users.

This case study demonstrates how friendship connections can be represented using a two-dimensional matrix in Python.

## Features

- Represent users in a social network.
- Store friendship connections using an adjacency matrix.
- Display the matrix of friendship connections.
- Check whether two users are friends.
- Represent mutual friendships using an undirected graph.

## Data Structure Used

**Adjacency Matrix**

An adjacency matrix is a two-dimensional array used to represent a graph.

- `1` indicates that two users are connected.
- `0` indicates that no connection exists.
- `0` on the main diagonal indicates that a user is not connected to themselves in this example.

Since friendships are mutual, the matrix is symmetric.

## Requirements

- Python 3.7 or newer
- No external packages are required.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python social_network.py
   ```

## Sample Input

The program uses five users:

- Sneha
- Yash
- Priya
- Rahul
- Amit

Friendship connections:

- Sneha and Yash
- Sneha and Priya
- Yash and Rahul
- Priya and Amit
- Rahul and Amit

## Sample Output

```text
SOCIAL NETWORK ADJACENCY MATRIX

Users: Sneha, Yash, Priya, Rahul, Amit

Adjacency Matrix:
        Sneha   Yash  Priya  Rahul   Amit
 Sneha      0      1      1      0      0
   Yash      1      0      0      1      0
  Priya      1      0      0      0      1
  Rahul      0      1      0      0      1
   Amit      0      0      1      1      0

Are Sneha and Yash friends?
Yes, they are friends.
```

## Time and Space Complexity

Let `V` represent the number of users and `E` represent the number of friendship connections.

- Creating the adjacency matrix: O(V²)
- Adding a friendship using the matrix: O(1), after locating the users' indices.
- Checking whether two users are friends: O(1), after locating the users' indices.
- Space Complexity: O(V²)

The Python implementation uses list searches to locate users, which take O(V) time. The stated O(1) operation costs apply once the relevant indices are known.

## Advantages

- Simple and easy to understand.
- Quickly checks whether two users are friends.
- Suitable for representing dense networks.
- Makes mutual friendship connections easy to represent.

## Limitations

- Requires O(V²) memory, even when there are few friendship connections.
- Adding a new user requires expanding the matrix.
- Not memory-efficient for very large, sparse social networks.

## Applications

- Representing friendship connections in social networks.
- Modeling communication networks.
- Representing connections in graph-based applications.
- Checking direct connections between users.

## Conclusion

This case study demonstrates how an adjacency matrix can represent friendship connections in a social network.

Each row and column represents a user, while matrix values indicate whether two users are connected. Although an adjacency matrix is simple and supports fast connection checks, its memory requirement can become very large when representing millions of users.

For large, sparse social networks, an adjacency list may be more memory-efficient.

## Files Included

- `social_network.py` – Python source code.
- `output.txt` – Sample program output.
- `README.md` – Case study documentation.
