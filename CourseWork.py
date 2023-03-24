import matplotlib.pyplot as plt
import pandas as pd
file = pd.read_csv("CrimeDataSet.csv")

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