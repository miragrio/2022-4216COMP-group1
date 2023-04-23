import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("CrimeDataSet.csv")


""" Depicitng Los Angeles Areas By Number Of Crimes (2020-2023) """
    
# A dictionary to store area code and area name.
areaName = {}
for area_code, area_name in zip(file['AREA'], file['AREA NAME']):
    areaName[area_code] = area_name

# Number of crime incidents, calculated from the 'AREA' column and incremented by 1.
get_amount = {}
for area_code in file['AREA']:
    get_amount[area_code] = get_amount.get(area_code, 0)
    get_amount[area_code] += 1
        

# Looping through areaName dictionary, and printing the number of crime incidents
# with area code and area name included, with appropriate formatting.
for area_code, area_name in areaName.items():
    amount = get_amount.get(area_code,0)
    print(f"{area_code}: {area_name} -> ({amount} incidents of crime)")

# Gathering the MODE value.
data_area = ""
data_mode = 0
for area, count in get_amount.items():
    if count > data_mode:
        data_area = area
        data_mode = count

desc1 =  get_amount.get(data_area)
print(f"The MODE is: {data_mode} with area code: {data_area}")

# Gathering the lowest value.
min_code = ""
min_count = float('inf')
for area,count in get_amount.items():
    if count < min_count:
        min_code = area
        min_count = count
            
desc2 = get_amount.get(min_code)
print(f"The lowest value is: {min_count} with area code: {min_code}")
    

# Taking the number of 'AREA NAME' instances, and gathering the top 5 and bottom 5 areas
# by number of instances. Columns created with value_counts function.
most_common = file['AREA NAME'].value_counts().nlargest(5).reset_index()
most_common.columns = ['AREA NAME', 'COUNT']

    
least_common = file['AREA NAME'].value_counts().nsmallest(5).reset_index()
least_common.columns = ['AREA NAME', 'COUNT']

# Readable font selection for graphs.
font1 = {'family':'serif','color':'blue','size':30}
font2 = {'family':'serif','color':'black','size':20}

# Three figures to displaying safest and most dangerous regions + additional comparison graph.
fig, (left,right,compare) = plt.subplots(1, 3)

# Plotting the most dangerous areas in the left bar chart.
left.bar(most_common['AREA NAME'], most_common['COUNT'],color='red')
left.grid(visible=True,linestyle='--')
left.set_facecolor('#E6E6FA')
spacing = 0.200
left.set_title("Dangerous Regions", fontdict=font1)
left.set_xlabel("Area Name",fontdict=font2)
left.set_ylabel("Amount of Crime (ALL CRIME INCLUDED!)", fontdict=font2)
    

# Plotting the safest areas in the right bar chart.
right.bar(least_common['AREA NAME'], least_common['COUNT'],color='green')
right.grid(visible=True,linestyle='--')
right.set_facecolor('#E6E6FA')
spacing = 0.200
right.set_title("Safest Regions",fontdict=font1)
right.set_xlabel("Area Name",fontdict=font2)
right.set_ylabel("Amount of Crime (All CRIME INCLUDED!)",fontdict=font2)
    
# Comparing the mode and lowest value by number of incidents.
compare.bar(data_area, data_mode, color='red', width=10.5, label='Mode')
compare.bar(min_code, min_count, color='green',width=10.5, label='Least')
compare.grid(visible=True,linestyle='--')
compare.set_facecolor('#E6E6FA')
compare.set_xlabel("AREA CODE", fontdict=font2)
compare.set_ylabel("Amount of Crime (All CRIME INCLUDED!)", fontdict=font2)
compare.set_xticks([data_area, min_code])
compare.set_title("Mode/Lowest Comparison", fontdict=font1)
spacing = 0.100
plt.subplots_adjust(bottom=spacing)
    
compare.legend()

# Adjusting the width between suplots and displaying them.
plt.subplots_adjust(wspace=0.3)
plt.show()