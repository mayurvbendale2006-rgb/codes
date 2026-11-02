
# 0/1 Knapsack using Dynamic Programming

# Function to solve Knapsack Problem
def knapsack(weights, values, capacity, n):

    # Create DP table
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main Program
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input("Enter weight of item " + str(i + 1) + ": "))
    value = int(input("Enter value of item " + str(i + 1) + ": "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter knapsack capacity: "))

if n <= 0 or capacity < 0 or any(w <= 0 for w in weights):
    print("Invalid input")
else:
    result = knapsack(weights, values, capacity, n)
    print("Maximum value:", result)
