sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = len(sampleList) // 3

chunks = [sampleList[i:i + chunk_size] for i in range(0, len(sampleList), chunk_size)]
for chunk in chunks:
    print(chunk[::-1])