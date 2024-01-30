import pandas

# Pandas Iteration

data = {
    "students": ["Angela", "James", "Lily"],
    "scores": [56, 76, 98]
}

data = pandas.DataFrame(data)

for i, row in data.iterrows():
    print(row['scores'])
