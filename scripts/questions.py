#load the data and load the correct packages:prject set up.

import pandas as pd
import matplotlib.pyplot as plt

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

# question 3:
#Are do variables relate? possible typo, but is this how do variables relate?
# correlation matrix of the numeric variables in the dataset.
people = df.drop_duplicates("iid")

attributes = ["importance_attractive", "importance_sincere", "importance_intelligent",
              "importance_fun", "importance_ambitious", "importance_shared_interests"]

corr = people[attributes].corr()

plt.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(6), attributes, rotation=90)
plt.yticks(range(6), attributes)
plt.title("Correlation between attribute weights")
plt.tight_layout()
plt.show()
# let on the side for the moment bc should be a typo
# question 4: 
# Do people that value attractivenesss also value ambition?
# correlation between importance_attractive and importance_ambitious
print(df["importance_attractive"].corr(df["importance_ambitious"]))
