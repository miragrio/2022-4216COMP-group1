import matplotlib.pyplot as plt
import pandas as pd
file = pd.read_csv("CrimeDataSet.csv")

"""Graph comparing status of the cases"""
Adult_Arrest = 0
Invest_Cont = 0
Adult_Other = 0
search = {}
chosen_data = "Status Desc"

for code in file[chosen_data]:
    search[code] = search.get(code, 0)
    search[code] += 1

Adult_Arrest = (search["Adult Arrest"])
Invest_Cont = (search["Invest Cont"])
Adult_Other = (search["Adult Other"])

print(f"Adult Arrest: {Adult_Arrest}")
print(f"Invest Cont: {Invest_Cont}")
print(f"Adult Other: {Adult_Other}")

names = ['Adult Arrest', 'Adult Other', 'Invest Cont']
values = [Adult_Arrest, Adult_Other, Invest_Cont]

font1 = {'family':'Arial','color':'black','size':20}

spacing = [0.01,0.01,0.01]
colors = ["#EC6B56", "#FFC154", "#47B39C"]

plt.title("Case Status", fontdict=font1)
plt.pie(values, labels = names, startangle = 90, explode = spacing, colors = colors)
plt.show() 