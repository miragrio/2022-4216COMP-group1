import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("CrimeDataSet.csv")

# Bar chart to represent locations with most activity

# Combine Premis Code and Premis Description
PremisCdDesc = {}
for code, desc in zip(file['Premis Cd'], file['Premis Desc']):
    PremisCdDesc[code] = desc


# Collecting the Data
collect = {} 
for code in file['Premis Cd']:
    collect[code] = collect.get(code,0)
    collect[code] += 1

# Top 10 locations (Which location should you be more careful in?)
top = file['Premis Desc'].value_counts().nlargest(10)

# Design and Plot
titleFont = {"family":"sans-serif", "color":"black","size":30}
descFont = {"family":"serif","color":"green","size":15}
top.plot(kind="bar", color="blue")
plt.grid(visible = True, axis = 'y', linestyle='-')
plt.xticks(rotation=20, fontsize=5)
plt.subplots_adjust(bottom=0.25)
plt.title("Top 10 Locations for Criminal Activity", fontdict=titleFont)
plt.xlabel("Location Description", fontdict=descFont)
plt.ylabel("Crime Amount", fontdict=descFont)
plt.show()