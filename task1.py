steps = list(map(int, input("Enter the number of steps taken each day, separated by spaces: ").split()))

highest_steps = max(steps)
lowest_steps = min(steps)

average_steps = sum(steps) / len(steps)

sorted_steps = sorted(steps, reverse=True)

print("\nDaily Steps Tracker Results:")
print(f"Highest step count: {highest_steps}")
print(f"Lowest step count: {lowest_steps}")
print(f"Average daily step count: {average_steps:.2f}")
print(f"Steps in descending order: {sorted_steps}")
# Test Case Input:
# 1200 1500 2000 2500 3000 2200 1800 2400 2600 2800 3200 3400 3600 3800 4000 4200 4400 4600 4800 5000 5200 5400 5600 5800 6000 6200 6400 6600 6800 7000

# Expected Output:
# Highest Step Count: 7000
# Lowest Step Count: 1200
# Average Step Count: 4133.33
# Steps in Descending Order:
# [7000, 6800, 6600, 6400, 6200, 6000, 5800, 5600, 5400, 5200, 5000, 4800, 4600, 
#  4400, 4200, 4000, 3800, 3600, 3400, 3200, 3000, 2800, 2600, 2500, 2400, 2200, 
#  2000, 1800, 1500, 1200]
