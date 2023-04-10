import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("CrimeDataSet.csv")

def pat_1():
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
        
    # Plotting the top ten crimes.
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

def pat_2():
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

    # Taking the number of 'AREA NAME' instances, and gathering the top 5 and bottom 5 areas
    # by number of instances. Columns created with value_counts function.
    most_common = file['AREA NAME'].value_counts().nlargest(5).reset_index()
    most_common.columns = ['AREA NAME', 'COUNT']

    
    least_common = file['AREA NAME'].value_counts().nsmallest(5).reset_index()
    least_common.columns = ['AREA NAME', 'COUNT']

    # Readable font selection for graphs.
    font1 = {'family':'serif','color':'blue','size':30}
    font2 = {'family':'serif','color':'black','size':20}

    # Two figures to displaying safest and most dangerous regions.
    fig, (left,right) = plt.subplots(1, 2)

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

    # Adjusting the width between suplots and displaying them.
    plt.subplots_adjust(wspace=0.5)
    plt.show()

def dan_1():
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

    fig, ax = plt.subplots() 
    ax.set_title("Gender Ratio")
    ax.bar(names, values)
    plt.show()


def mat_1():
    # Bar chart to represent locations with most activity

    # Collecting the Data
    collect = {} 
    for i in file['Premis Cd']:
        collect[i] = collect.get(i,0)
        collect[i] += 1

    # Combine Premis Code and Premis Description
    PremisCD = {}
    for i,j in zip(file['Premis Cd', file['Premis Desc']]):
        PremisCD[i] = j 
    
    # Top 10 locations (Which location should you be more careful in?)
    top = file['Premis Desc'].value_counts().nlargest(10)

    # Design and Plot
    titleFont = {"family":"sans-serif", "color":(0,125,125),"size":30}
    descFont = {"family":"serif","color":"green","size":15}
    top.plot(kind="bar", color="blue")
    plt.grid(visible = True, axis = 'y', linestyle='-')
    plt.xticks(rotation=20, fontsize=5)
    plt.subplots_adjust(bottom=0.25)
    plt.title("Top 10 Locations for Criminal Activity", fontdict=titleFont)
    plt.xlabel("Location Description", fontdict=descFont)
    plt.ylabel("Crime Amount", fontdict=descFont)

    # Show the graph
    plt.show()

# Graph Selection.
user_menu = {
    "1": pat_1,
    "2": pat_2,
    "3": dan_1,
    "4": mat_1,
    "5": quit
    }

# Update when you upload your graph.
while True:
    print('''
Please select team member graph:
1) Patrick - MOST COMMON CRIMES
2) Patrick - CRIME IN LOS ANGELES AREAS
3) Daniel - CRIME BY GENDER
4) Matei - CRIME BY PREMISE
5) Quit
''')
    user_choice = input("Selection: ")

    if user_choice in user_menu:
        user_menu[user_choice]()
    else:
        ("You have entered an invalid choice.")
        