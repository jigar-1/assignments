rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

result = [num for num in rollNumber if num in sampleDict.values()]
print(result)