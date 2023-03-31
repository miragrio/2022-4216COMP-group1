import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("CrimeDataSet.csv")

def dan_1():
    """Graph comparing gender rations"""
    Male = 0
    Female = 0
    Other = 0
    chosen_data1 = "Vict Sex"

    x = 0
    data = file[chosen_data1]
    length = len(data)

    get_amount = {}

    for code in file[chosen_data1]:
        get_amount[code] = get_amount.get(code, 0)
        get_amount[code] += 1

    Male = (get_amount["M"])
    Female = (get_amount["F"])
    Other = (get_amount["X"])

    print(f"Male: {Male}")
    print(f"Female: {Female}")
    print(f"Other: {Other}")
    
    names = ['Male', 'Female', 'Other']
    values = [Male, Female, Other]

    fig, ax = plt.subplots() 
    ax.set_title("Gender Ratio")
    ax.bar(names, values)
    plt.show()


def pat_1():
    """ Bar Chart Representing Common Crimes """

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

# Graph Selection.
user_menu = {
    "1": dan_1,
    "2": pat_1,
    "3": quit
    }

# Update when you upload your graph.
while True:
    print('''
Please select team member graph:
1) Daniel
2) Patrick
3) Quit
''')
    user_choice = input("Selection: ")

    if user_choice in user_menu:
        user_menu[user_choice]()
    else:
        ("You have entered an invalid choice.")
        