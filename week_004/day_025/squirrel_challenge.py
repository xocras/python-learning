import pandas

data = pandas.read_csv("squirrel_data.csv")

fur_colors = data['Primary Fur Color'].dropna().unique()

table = {
    'Primary Fur Color': [color for color in fur_colors],
    'Count': [data['Primary Fur Color'].value_counts()[color] for color in fur_colors]
}

table = pandas.DataFrame(table)

table.to_csv("squirrel_count.csv", index=False)