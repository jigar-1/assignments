import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# ===== PART 1 =====
print("\n===== PART 1 =====")
# 1.1 Create dataframe
data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', "", 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, "", ""],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]
}
df = pd.DataFrame(data).replace(["", " "], np.nan)

# 1.2 Save to CSV
df.to_csv('q1.csv', index=False)

# 1.3 Read and print
print("\n1.3 DataFrame:")
print(pd.read_csv('q1.csv'))

# 1.4 Read without headers
print("\n1.4 Without headers:")
print(pd.read_csv('q1.csv', header=None))

# 1.5 Set index columns
print("\n1.5 With index columns:")
print(pd.read_csv('q1.csv', index_col=['first_name', 'last_name']))

# 1.6 Boolean null check
print("\n1.6 Null check:")
print(df.isna())

# 1.7 Skip first 3 rows
print("\n1.7 Skip rows:")
print(pd.read_csv('q1.csv', skiprows=3))

# 1.8 Read with thousands separator
print("\n1.8 With thousands separator:")
print(pd.read_csv('q1.csv', thousands=','))

# ===== PART 2 =====
print("\n===== PART 2 =====")
movies_df = pd.read_csv('Movies.csv')

# 2.1 Highest rated Quest movie
quest_movies = movies_df[movies_df['Story'] == 'Quest']
highest_rated_quest = quest_movies.loc[quest_movies['Profitability'].idxmax()]
print("Highest rated Quest movie:", highest_rated_quest['Mode'])

# 2.2 Genre with most releases
print("\n2.2 Genre with most releases:")
print(movies_df['Genre'].value_counts().idxmax())

# 2.3 Top 5 costliest movies
print("\n2.3 Top 5 by budget:")
print(movies_df.nlargest(5, 'Budget')[['Movie', 'Budget']])

# 2.4 Profitability vs Rating plot
plt.figure(figsize=(8,5))
plt.scatter(movies_df['RottenTomatoes'], movies_df['Profitability'])
plt.title('2.4 Profitability vs Ratings')
plt.xlabel('Rating')
plt.ylabel('Profitability')
plt.grid(True)
plt.show()

# ===== PART 3 =====
print("\n===== PART 3 =====")
# 3.1 Create Series
s1 = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])

# 3.2 Lower case
print("\n3.2 Lower case:")
print(s1.str.lower())

# 3.3 Upper case
print("\n3.3 Upper case:")
print(s1.str.upper())

# 3.4 Lengths
print("\n3.4 Lengths:")
print(s1.str.len())

# 3.5 Create Series with spaces
s2 = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])

# 3.6 Strip spaces
print("\n3.6 Stripped:")
print(s2.str.strip())

# 3.7 Left strip
print("\n3.7 Left strip:")
print(s2.str.lstrip())

# 3.8 Right strip
print("\n3.8 Right strip:")
print(s2.str.rstrip())

# ===== PART 4 =====
print("\n===== PART 4 =====")
# 4.1 Replace X or dog
s3 = pd.Series(['A', 'B', 'C', 'AabX', 'BacX', np.nan, 'CABA', 'dog', 'cat'])
print("\n4.1 Replace X/dog:")
print(s3.replace({'X': 'XX-XX', 'dog': 'XX-XX'}, regex=True))

# 4.2 Remove dollar signs
s4 = pd.Series(['12', '-$10', '$10,000'])
print("\n4.2 Remove $:")
print(s4.str.replace(r'\$', '', regex=True))

# 4.3 Reverse lowercase words
s5 = pd.Series(['france 1998', 'country', np.nan])
print("\n4.3 Reverse lowercase:")
print(s5.apply(lambda x: ' '.join([word[::-1] if word.islower() else word for word in str(x).split()]) if pd.notnull(x) else x))

# 4.4 Alphanumeric check
s6 = pd.Series(['1', '2', '1a', '2b', '2003c'])
print("\n4.4 Alphanumeric check:")
print(s6.apply(lambda x: bool(re.match(r'^(?=.*[a-zA-Z])(?=.*\d)', str(x)))))

# 4.5 Contains 'A' check
s7 = pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
print("\n4.5 Contains 'A':")
print(s7.str.contains('A', case=False, na=False))

# 4.6 One-hot encode a/b/c
s8 = pd.Series(['a', 'ajb', np.nan, 'ajc'])
print("\n4.6 One-hot encode:")
print(pd.get_dummies(s8).reindex(columns=['a','b','c'], fill_value=0))

# 4.7 Merge dataframes
left = pd.DataFrame({'key': ['One', 'Two'], 'lefttable': [1, 2]})
right = pd.DataFrame({'key': ['One', 'Two'], 'righttable': [4, 5]})
print("\n4.7 Merged tables:")
print(pd.merge(left, right, on='key'))