import pandas as pd

# read data from CSV file into a datafram
df = pd.read_csv("C:/Users/navneet ranjan/OneDrive/Desktop/station_hour.csv", low_memory=False)
print(df)

# rows in pandas
print("Display 10rows from start")
print(df.head(n=10))

print("Display 5 rows from last")
print(df.tail(n=5))

# info method in pandas
print("Displaying the info of data set")
print(df.info()) 
"""
    info method properties: 
        1> number of rows and columns 
        2> column name
        3> data type of each column
        4> non null counts
        5> memory usage of the data frame
"""

# describe method in pandas
print("Discription of the data set")
print(df.describe())