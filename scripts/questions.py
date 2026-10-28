#load the data and load the correct packages:prject set up.

import pandas as pd

df = pd.read_csv("data/speed-dating.csv")
# put your own path here in this case its a relative path to the data folder in the project directory.

## question 1: 
#What is the average number of matches per participant?

matches_per_person = df.groupby("iid")["match"].sum()
print(matches_per_person.mean())

