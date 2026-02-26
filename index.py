import pandas as pd

df = pd.read_csv("student_productivity_distraction_dataset_20000.csv")

print(df.head())
print(df.info())

print(df.isnull().sum())

#Estadística descriptiva#

print(df.describe())


#qué variables influyen más
#cuáles influyen menos
#cuáles afectan negativamente#

corr = df.corr(numeric_only=True)

print(corr["productivity_score"].sort_values(ascending=False))

