nums = []
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    nums.append(num)

if not nums:
    print("No numbers entered")
else:
    max_num = max(nums)
    count = nums.count(max_num)
    print(f"The largest number is {max_num}")
    print(f"The occurrence count is {count}")