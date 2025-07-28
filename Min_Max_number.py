s = {34,56,67,89,4,56,3,7,32,56789,456,76,3}

print(sorted(s))
print("Minimum Value:" , min(s))
print("Maximum Value:", max(s))


#using Loops:
s = {5, 3, 9, 1, 7}

# Initialize min and max with extreme values
min_val = float('inf')
max_val = float('-inf')

# Iterate through the set to find min and max
for ele in s:
    if ele < min_val:
        min_val = ele
    if ele > max_val:
        max_val = ele

print("Minimum element:", min_val)
print("Maximum element:", max_val)
