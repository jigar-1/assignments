sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
unique_items = list(set(sampleList))
unique_tuple = tuple(unique_items)
min_value = min(unique_tuple)
max_value = max(unique_tuple)

print("Unique items:", unique_items)
print("Tuple:", unique_tuple)
print("Min:", min_value)
print("Max:", max_value)