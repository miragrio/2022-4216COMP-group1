def joe_1():
    """Graph comparing dates of crimes committed"""
    january = 0
    february = 0
    march = 0
    april = 0
    may = 0
    june = 0
    july = 0
    august = 0
    september = 0
    october = 0
    november = 0
    december = 0
    search = {}
    chosen_data = "Date Rptd"

    for code in file[chosen_data]:
        search[code] = search.get(code, 0)
        search[code] += 1

    for date,count in search.items():
        if date[0:2] == "01":
            january+=1
        if date[0:2] == "02":
            february+=1
        if date[0:2] == "03":
            march+=1
        if date[0:2] == "04":
            april+=1
        if date[0:2] == "05":
            may+=1
        if date[0:2] == "06":
            june+=1
        if date[0:2] == "07":
            july+=1
        if date[0:2] == "08":
            august+=1
        if date[0:2] == "09":
            september+=1
        if date[0:2] == "10":
            october+=1
        if date[0:2] == "11":
            november+=1
        if date[0:2] == "12":
            december+=1

    names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    values = [january, february, march, april, may, june, july, august, september, october, november, december]

    fig, ax = plt.subplots() 
    ax.set_title("Crimes Committed in each month")
    ax.bar(names, values, color='red')
    ax.set_facecolor('#000')
    plt.show()