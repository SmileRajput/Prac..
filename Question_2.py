def min_shots_required(test_cases):
    results = []
    for n, k, heights in test_cases:
        # Count how many players are taller than Gi-Hun and Ali
        shots_required = sum(1 for h in heights if h > k)
        results.append(shots_required)
    return results


# Read the number of test cases
T = int(input().strip())

# Read each test case
test_cases = []
for _ in range(T):
    N, K = map(int, input().strip().split())
    heights = list(map(int, input().strip().split()))
    test_cases.append((N, K, heights))

# Get the number of shots required for each test case
results = min_shots_required(test_cases)

# Print the results
for result in results:
    print(result)
