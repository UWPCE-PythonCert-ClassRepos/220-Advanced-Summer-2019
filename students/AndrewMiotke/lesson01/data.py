import pandas as pd

# takes a url or a path to a csv file
data = pd.read_csv("http://data.teleona.com/iris.csv")

len(data)

data.head(10)
data.tail(10)


