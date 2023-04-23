import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("CrimeDataSet.csv")

""" Bar Chart Representing Crimes In Los Angeles (2020-2023) """

# A dictionary consisting of crime code (Crm Cd) descriptions (Crm Cd Desc).
codeDesc = {}
for code, desc in zip(file['Crm Cd'], file['Crm Cd Desc']):
    codeDesc[code] = desc

# Number of incidents (increment by 1 per incident).
get_amount = {}
for code in file['Crm Cd']:
    get_amount[code] = get_amount.get(code, 0)
    get_amount[code] += 1
        
# Printing the number of incidents and the crime code/desc.
for code, desc in codeDesc.items():
    amount = get_amount.get(code,0)
    print(f"{code}: {desc} -> ({amount} incidents)")

# Extracting the top ten crimes.
most_common = file['Crm Cd Desc'].value_counts().nlargest(10)

# Choosing font.
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':15}
        
# Plotting the top ten crimes
most_common.plot(kind='bar',color='green')
plt.grid(visible=True, axis='y', linestyle='--')
plt.xticks(rotation=10)
spacing = 0.500
plt.xticks(fontsize=5)
plt.subplots_adjust(bottom=spacing)
plt.xlabel('Crime Description', fontdict=font2)
plt.ylabel('Number of incidents', fontdict=font2)
plt.title('Top 10 Crime Codes', fontdict=font1)
    
plt.show()