import pandas as pd

data = {
    "Name" : ["Navneet", "Ranjan", "Kumar"],
    "Age" : [10, 15, 20],
    "Salary" : [10000, 15000, 20000],
    "Score" : [90, 92, 93],
}

df = pd.DataFrame(data)

# .loc[]
# d.loc[row_index, "Column Name"] = newValue

df.loc[0, "Salary"] = 12000
print(df)