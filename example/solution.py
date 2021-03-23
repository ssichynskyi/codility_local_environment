# Replace the code below with solution function from Codility platform
def solution(X, A):
    # check minimum conditions to make sure frog's trip is possible
    if len(A) < X or max(A) < X:
        return -1
    sum = X * (X + 1) // 2
    covered_positions = set()
    spare = len(A) - X

    for i in range(len(A)):
        if A[i] not in covered_positions and 1 <= A[i] <= X:
            covered_positions.add(A[i])
            sum -= A[i]
        else:
            spare -= 1
        if sum <= 0:
            return i
        if spare < 0:
            return -1
    return -1
