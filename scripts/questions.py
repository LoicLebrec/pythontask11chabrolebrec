#load the data and load the correct packages:prject set up.

import pandas as pd

df = pd.read_csv("data/speed-dating.csv")
# put your own path here in this case its a relative path to the data folder in the project directory.

## question 1: 
# step 1 list variables, 
print(df.columns)
#step 2
#What is the average number of matches per participant?
matches_per_person = df.groupby("iid")["match"].sum()
print(matches_per_person.mean())
# group the data by participant id (iid) and sum the matches for each participant, then calculate the mean of those sums to get the average number of matches per participant.

## question 2:

# Step 1: list the six attributes
attributes = ["importance_attractive", "importance_sincere", "importance_intelligent",
              "importance_fun", "importance_ambitious", "importance_shared_interests"]
print(attributes)

# Step 2: average weight of each attribute by gender, top 3
means = df.groupby("gender")[attributes].mean()

print(means.loc[0].sort_values(ascending=False).head(3))
print(means.loc[1].sort_values(ascending=False).head(3))

# no def of the gender so we can only say 0 or 1.
