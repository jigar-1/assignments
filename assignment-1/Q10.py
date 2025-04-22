# Upper part
for i in range(1, 6):
    print(''.join(map(str, range(i, 8))))
print(7)  # Middle line
# Lower part
for i in range(6, 0, -1):
    print(''.join(map(str, range(i, 8))))