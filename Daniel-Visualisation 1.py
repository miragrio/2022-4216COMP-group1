import matplotlib.pyplot as plt
import pandas as pd
file = pd.read_csv("CrimeDataSet.csv")

"""Graph comparing gender ratios"""
Male = 0
Female = 0
Other = 0
search = {}
chosen_data = "Vict Sex"

for code in file[chosen_data]:
    search[code] = search.get(code, 0)
    search[code] += 1

Male = (search["M"])
Female = (search["F"])
Other = (search["X"])

print(f"Male: {Male}")
print(f"Female: {Female}")
print(f"Other: {Other}")

names = ['Male', 'Female', 'Other']
values = [Male, Female, Other]

spacing = [0.01,0.01,0.01]
colors = ["#EC6B56", "#FFC154", "#47B39C"]

plt.title("Gender Ratio")
plt.pie(values, labels = names, startangle = 90, explode = spacing, colors = colors)
plt.show() 