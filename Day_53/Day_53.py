#Perform various operations on sets (union, intersection, etc.).


# Define two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Perform set operations
print("Set A:", A)
print("Set B:", B)

# Union
print("Union (A ∪ B):", A | B)  # OR: A.union(B)

# Intersection
print("Intersection (A ∩ B):", A & B)  # OR: A.intersection(B)

# Difference
print("Difference (A - B):", A - B)  # OR: A.difference(B)
print("Difference (B - A):", B - A)  # OR: B.difference(A)

# Symmetric Difference
print("Symmetric Difference (A Δ B):", A ^ B)  # OR: A.symmetric_difference(B)

