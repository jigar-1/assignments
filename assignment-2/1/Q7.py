words = input("Enter a hyphen-separated sequence of words: ").split('-')
words.sort()
print('-'.join(words))