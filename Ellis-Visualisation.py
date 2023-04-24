
import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("CrimeDataSet.csv")

def ellis_1():
    """ Bar Chart Representing Weapon Usage In Los Angeles (2020-2023) """

    # Extracting the top ten weapons.
    common_w = file['Weapon Desc'].value_counts().nlargest(10)

    # Choosing font.
    font1 = {'family':'Arial','color':'red','size':20}
    font2 = {'family':'Arial','color':'blue','size':15}
        
    # Plotting the top ten weapons.
    common_w.plot(kind='bar',color='purple')
    plt.grid(visible=True, axis='y', linestyle='--')
    plt.xticks(rotation=10)
    spacing = 0.500
    plt.xticks(fontsize=8)
    plt.subplots_adjust(bottom=spacing)
    plt.xlabel('Weapon Used', fontdict=font2)
    plt.ylabel('Number of incidents', fontdict=font2)
    plt.title('Top 10 Weapons', fontdict=font1)
    
    plt.show()

ellis_1()