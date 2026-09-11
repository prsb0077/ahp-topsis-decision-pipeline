import numpy as np
import math
#================AHP====================
RI_DICT = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 
           6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}

# ask for Criteria

n = int(input("Enter number of criteria: "))


# Initialize an n * n matrix with 1.0
matrix = np.ones((n,n))

# ask for comparisons
print(f"Paste all {n * n} values separated by space:")
raw_input = input()

# Split string into floats and reshape to (n, n)
matrix = np.array([float(x) for x in raw_input.split()]).reshape(n, n)

print("\nThe Criteria Matrix: ")
print(matrix)

# list to store geo mean of each row
geomMean = []

for i in range(n):
    rowProduct = 1.0
    for j in range (n): 
        rowProduct *= matrix[i,j]


    #calculate nth root and put it inside list
    r_i = rowProduct ** (1.0 / n)
    geomMean.append(float(r_i))


total_sum = sum(geomMean)
weights = [r / total_sum for r in geomMean]

print("Row Geometric Means:", geomMean)
print("Normalized Weights :", weights)

w = np.array(weights)

ws = np.dot(matrix, w)

lambda_max = np.mean(ws / w)


# Calculate CI and CR
ci = (lambda_max - n) / (n - 1)
ri = RI_DICT.get(n, 1.49)
cr = ci / ri

# Output the verification
print(f"\nλ_max: {lambda_max:.4f}")
print(f"CI   : {ci:.4f}")
print(f"CR   : {cr:.4f}")

if cr < 0.10:
    print("Result: Consistent (CR < 0.10)")
else:
    print("Result: Inconsistent! User must revise judgments.")

#================================================
#Topsis Calculations
#================================================

# Note that n is number of criteria

print("============== TOPSIS ==============")
# creating decision matrix
m = int(input("Enter the number of alternatives: "))

print(f"You can paste all {m * n} decision matrix values separated by space:")
rawDM = input()
decisionMatrix = np.array([float(x) for x in rawDM.split()]).reshape(m,n)

print("Enter Criteria type separated by space(+1 for benefit, -1 for cost)")
typeOfCriteria = np.array([int(x) for x in input().split()])

# normalize vector
VecNorm = np.sqrt(np.sum(decisionMatrix ** 2, axis=0))
Rmatrix = decisionMatrix / VecNorm

# weighted  normalized matrix (V) * w is the array type initialized in AHP

Vmatrix = Rmatrix * w

# finding ideal solutions (A+ A-)

Aplus = np.zeros(n) # generates array containing n
Aminus=np.zeros(n)

for j in range(n):
    if typeOfCriteria[j] == 1:
        Aplus[j] = np.max(Vmatrix[:, j])
        Aminus[j] = np.min(Vmatrix[:, j])
    else:
        Aplus[j] = np.min(Vmatrix[:, j])
        Aminus[j] = np.max(Vmatrix[:, j])

# euclidean Distances (d+ d-)

Dplus = np.sqrt(np.sum((Vmatrix - Aplus) ** 2, axis=1)) 
Dminus = np.sqrt(np.sum((Vmatrix - Aminus) ** 2, axis=1))


#closeness ocefficient
cc = Dminus/ (Dplus + Dminus)
rank = np.argsort(cc) [::-1]

print("RESULT:")
for ranking, idx in enumerate(rank,1):
    print(f"Rank {ranking}: Alternative {idx + 1} (Score = {cc[idx]:.4f})")