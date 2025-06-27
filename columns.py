import pandas as pd

data = {
    "Name" : ["Navneet", "Ranjan", "Kumar"],
    "Age" : [10, 15, 20],
    "Salary" : [10000, 15000, 20000],
    "Score" : [90, 92, 93],
}

df = pd.DataFrame(data)

# squre brakcets df["Column Name"] = some_data
df["Bonus"] = df["Salary"] * 0.1

#using insert method df.insert(location, "Column name", data)
df.insert(2, "emp_id", [23, 3,4])


print(df)