import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("CrimeDataSet.csv")

def dan_1():
        ## Setting variables
    D =[]
    E =[]

    ## Printing the titels and getting the user to select data to compare
    print(file.keys())
    chosen_data1 = input("Select a first data: ")
    chosen_data2 = input("Select a second data: ")

    ## Collecting the data for option 1
    x = 0
    data = file[chosen_data1]
    #data = file.sort_values(by=chosen_data1)
    length = len(data)
    while (x < length):
        temp = file[chosen_data1][x]
        D.append(temp)
        print("Data 1: %d/%d" % (x,length))
        x = x + 1

    ## Collecting the data for option 2
    x = 0
    data = file[chosen_data2]
    #data = file.sort_values(by=chosen_data2)
    length = len(data)
    while (x < length):
        temp = file[chosen_data2][x]
        E.append(temp)
        print("Data 2: %d/%d" % (x,length))
        x = x + 1

    ## Creating and dispalying a line graph if inputs are the same length
    if len(D) == len(E):
        fig, ax = plt.subplots()
        #Formating
        fig.suptitle("Crime data comparison", fontsize=20)
        #ax.set_title("Sub Title", fontsize=14)
        ax.set_xlabel(chosen_data1, fontsize=12)
        ax.set_ylabel(chosen_data2, fontsize=12)
        #ax.plot(D, E, 'mD:', label="D-E")
        ax.plot(D, E, label="%s - %s" % (chosen_data1, chosen_data2))
        ax.legend()
        ax.grid(True)
        plt.show()
    else:
        print("Error. Input lengths must match. Input1 = %d, Input2 = %d" % (len(D), len(E)))


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
