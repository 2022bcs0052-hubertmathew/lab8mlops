import pandas as pd

df = pd.read_csv("housing.csv")
df = df.head(5000)
df.to_csv("data/housing.csv", index=False)